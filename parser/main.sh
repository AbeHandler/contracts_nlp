#sudo python setup.py develop
#py find_data_to_parse.py > training_data.txt
parserator label trainer.csv training/labeled.xml contract_parser
parserator train training/labeled.xml contract_parser
