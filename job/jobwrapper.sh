if [[ $@ == *edit* ]]
then
	jobpy "$@"
else
	eval `jobpy "$@"`
fi
