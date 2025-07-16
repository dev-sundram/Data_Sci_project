from src.ds_project.logger import logging
from src.ds_project.exception import CustomException
import sys
from src.ds_project.components.data_ingestion import DataIngestion
from src.ds_project.components.data_ingestion import DataIngestionConfig



if __name__ == "__main__":
    logging.info("Starting the ds project")
    # Add more code here to run your ML project

    try: 
       # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys) 
