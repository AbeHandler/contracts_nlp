#copy(select * from family_log where is_true=True) To '/tmp/test.csv' With CSV; get the data out of postgres
if [ -f "test.csv" ]
then
	echo "Already have test data from the server"
else
	scp abe@projects.thelensnola.org:/tmp/test.csv .
fi

csvcut -c 2,5 test.csv > labels.csv

#COPY (select * from amount_string_log where is_true=True or is_true=False) TO '/tmp/amounts.csv' DELIMITER ',' CSV;
#COPY (select * from amount_string_log where is_true is NULL) TO '/tmp/amounts_unknown.csv' DELIMITER ',' CSV;
scp abe@projects.thelensnola.org:/tmp/amounts.csv .
scp abe@projects.thelensnola.org:/tmp/amounts_unknown.csv .
csvcut -c 2,3,4 amounts.csv > amounts.tmp
csvcut -c 2,3 amounts_unknown.csv > amounts_unknown.tmp
mv amounts_unknown.tmp amounts_unknown.csv
mv amounts.tmp amounts.csv