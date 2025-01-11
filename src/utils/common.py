import os
from src.logger import logging
from src.exception import CustomException
import yaml
import sys
import pandas as pd
import pickle

def read_yaml(filepath):
    # Load the yaml file
    try:
        with open(filepath, 'r') as file_obj:
            content = yaml.safe_load(file_obj)
            logging.info(f'Loaded yaml file {file_obj} successfully')
            return content
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
    
def create_directories(filepath):
    # Creating directories
    try:
        if not os.path.exists(filepath):
            logging.info(f'Creating directory: {filepath}')
            os.makedirs(filepath, exist_ok=True)
        else:
            logging.info(f'Directory already exists: {filepath}')
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
    
def load_csv_data(filepath):
    # Load csv data
    try:
        if not os.path.exists(filepath):
            logging.info(f'Data filepath {filepath} does not exist')
        else:
            data = pd.read_csv(filepath)
            logging.info(f'Loaded csv data from {filepath}')
            return data
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
    
def save_csv_data(data, filepath):
    # Save csv data
    try:
        data.to_csv(filepath, index=False)
        logging.info(f'Saved csv data to {filepath}')
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
    
def save_into_pickle_file(model, model_path):
    # Save model into pickle file
    try:
        logging.info(f'Saving model to {model_path}')
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)
            logging.info(f'Model saved successfully to {model_path}')
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
    
def load_from_pickle_file(model_path):
    #Load the pickle file
    try:
        logging.info(f'Loading the model from {model_path}')
        with open(model_path, 'rb') as file:
            object = pickle.load(file)
        return object
    except Exception as e:
        logging.error(f'Error Occured: {e}')
        raise CustomException(e,sys)
        