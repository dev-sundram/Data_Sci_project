import os 
import sys
from src.ds_project.exception import CustomException
from src.ds_project.logger import logging
import pandas as pd
# from src.ds_project.utils import read_sql_data
from sklearn.model_selection import train_test_split


from dataclasses import dataclass 

@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
            try:
                ## reading the data from mysql 
                # df = read_sql_data()
                # df = pd.read_csv("C:\\Users\\shivam\\OneDrive\\Desktop\\DataSci_project\\dataset.csv")
                df = pd.read_csv("C:\\Users\\shivam\\OneDrive\\Desktop\\DataSci_project\\project_1\\artifacts\\dataset.csv")
                

                logging.info("Reading Completed from mysql database")
                 # Create folder if not exists
                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

                # Save raw data
                df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

                # Split data
                train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

                # Save train and test
                train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
                test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

                logging.info("Data INgestion completed successfully ")
                return (
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )

            except Exception as e:
                raise CustomException(e, sys) 