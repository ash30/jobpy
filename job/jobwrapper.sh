if [[ $@ == --h ]]
then
	jobcmd "$@"
else
	eval `jobcmd.py "$@"`
fi
