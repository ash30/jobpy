"""
Job Tool 
Setup a standard set of environmental variables based on project keyword

"""
from __future__ import print_function
import os,sys,argparse,ConfigParser

TOOL_NAME="job"
DESCRIPT="export set of env vars based on project keyword"
PROJ_KEY="project"
DEFAULT_HEADER_NAME="DEFAULTS"

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def create_parser_from_default_configs(key_val_pairs):
    parser = argparse.ArgumentParser(description=DESCRIPT)

    for arg,initial_val in key_val_pairs:
        parser.add_argument("--{}".format(arg))

    # Default args if not present
    if "project" not in { arg for arg,_ in key_val_pairs}:
        parser.add_argument("--project")
    return parser
            
def terminal_cusor_text(project_name):
    return '\"[{}] \h:\W \u$ \"'.format(project_name)

def terminal_command_string(mapping):
    cmd_list = ["export {}={}".format(k,v) for k,v in mapping.iteritems()]
    return ";".join(cmd_list)
    
def main():
    # Setup config reader
    config_file_path = os.path.join(os.environ['HOME'], '.' + TOOL_NAME)
    config = ConfigParser.ConfigParser()
    config.optionxform = str # case sensitive
    config.read(config_file_path)
    if not config.has_section(DEFAULT_HEADER_NAME):
        eprint("ERROR reading config file ~/.job")
        sys.exit(1)

    # Setup commandline parser
    parser = create_parser_from_default_configs(
        config.items(section=DEFAULT_HEADER_NAME)
    )
    args = {k:v for k,v in vars(parser.parse_args()).iteritems() if v}

    # Settings start life as copy of config defaults
    settings = {}
    settings.update(config.items(section=DEFAULT_HEADER_NAME))

    # Also get optional project section in config
    project = args.get(PROJ_KEY, settings.get(PROJ_KEY,""))
    project_name_without_quotes = project.replace('"',"")
    if project and config.has_section(project_name_without_quotes):
        settings.update(
            {k:v for k,v in config.items(section=project_name_without_quotes)}
        )
    elif project:
        eprint("WARNING: project specified doesn't exist")

    # Finally merge in commandline args (they override everything else)
    settings.update(args)

    # Filter blank settings
    settings = {k:v for k,v in settings.iteritems() if v}

    # add alittle setup to terminal
    settings['PS1'] = terminal_cusor_text(project_name_without_quotes)

    print(terminal_command_string(settings))

if __name__ == "__main__":
    print(main())
