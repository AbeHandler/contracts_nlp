#sudo python setup.py develop
py find_data_to_parse.py
csvcut -c 1 data.csv > trainer.csv
parserator label trainer.csv training/labeled.xml contract_parser
parserator train training/labeled.xml contract_parser