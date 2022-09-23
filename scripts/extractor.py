import pandas as pd
from logger import Logger
import sys
from datetime import datetime
class DataExtractor():
    def __init__(self)->None:
        try:
            self.logger=Logger().get_app_logger()
            self.logger.info('Data extractor object Initialized')
        except:
            pass