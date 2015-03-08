#copy(select * from family_log where is_true=True) To '/tmp/test.csv' With CSV; get the data out of postgres
if [ -f "test.csv" ]
then
	echo "Already have test data from the server"
else
	scp abe@projects.thelensnola.org:/tmp/test.csv .
fi

csvcut -c 2,5 test.csv > labels.csv
