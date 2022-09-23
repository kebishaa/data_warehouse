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
    def get_columns_and_rows(self,file_path)->tuple:
        try:
            with open(f'../data/{file_path}','r') as f:
                lines=f.readlines()

            columns=lines[0].replace('\n','').split(';')
            data=lines[1:]
            return columns,data
        except Exception as e:
            # the try excepts here are for the airflow
            try:
                self.logger.error(f"Failed to read data: {e}")
            except:
                pass
            sys.exit(1)
    def chunk_list(self,list,chunk_size,default_first_val=None)->list:
        chunked_list=[]
        for i in range(0, len(list), chunk_size):
            if default_first_val:
                values=[default_first_val]
                values.extend(list[i:i+chunk_size])
                chunked_list.append(values)
            else:
                chunked_list.append(list[i:i+chunk_size])

        return chunked_list

    