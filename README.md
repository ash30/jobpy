# jobpy
Small python script for setting up env vars 

./.job should be config file holding sets of common env vars you want to set

    [DEFAULTS]
    project=project1
    var1=HELLO
    var2=WORLD
    
    [project1]
    var2=UK
    
    [project2]
    var2=ALL

DEFAULTS will always be set, other headings are set based on the project specified (either via defaults or commandline).

Project settings override defaults. You can overide any variable at commandline via flag of same name e.g --project, --var1

Install via pip, and jobpy entry point will return a list of export statements you can eval to setup your environment
