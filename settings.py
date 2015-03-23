import ConfigParser

class Settings():


    def __init__(self):
    	self.CONFIG_LOCATION = "/configs/contracts_ml.cfg"
        self.corpus_location = self.get_from_config('corpus_location')
        self.connection_string_contracts = self.get_from_config('connection_string_contracts')
        self.lens_dir = self.get_from_config('lens_dir')
    

    def get_from_config(self, field):
        config = ConfigParser.RawConfigParser()
        config.read(self.CONFIG_LOCATION)
        return config.get('Section1', field)