if [[ $@ == --h ]]
then
	jobpy "$@"
else
	eval `jobpy --project "$@"`
fi
