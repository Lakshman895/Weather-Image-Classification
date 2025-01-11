import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_transformation import DataTransformatioPipeline
from src.pipeline.stage_03_data_splitting import DataSplittingPipeline
from src.pipeline.stage_04_model_trianing import ModelTrainingPipeline
from src.pipeline.state_05_evaluate_model import ModelEvaluatePipeline

STAGE_NAME = 'Data Ingestion'

try:
    logging.info(f'>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logging.info(f'<<<<<<<<<<<<<<< Stage {STAGE_NAME} Ended <<<<<<<<<<<<<<<')
    
except Exception as e:
    logging.error(f'Error Occurred: {e}')
    raise CustomException(e, sys)

STAGE_NAME = 'Data Transformation'

try:
    logging.info(f'>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>')
    data_transformation = DataTransformatioPipeline()
    data_transformation.main()
    logging.info(f'<<<<<<<<<<<<<<< Stage {STAGE_NAME} Ended <<<<<<<<<<<<<<<')
    
except Exception as e:
    logging.error(f'Error Occurred: {e}')
    raise CustomException(e, sys)

STAGE_NAME = 'Data Splitting'

try:
    logging.info(f'>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>')
    data_splitting = DataSplittingPipeline()
    data_splitting.main()
    logging.info(f'<<<<<<<<<<<<<<< Stage {STAGE_NAME} Ended <<<<<<<<<<<<<<<')
    
except Exception as e:
    logging.error(f'Error Occurred: {e}')
    raise CustomException(e, sys)

STAGE_NAME = 'Model Training'

try:
    logging.info(f'>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>')
    model_training = ModelTrainingPipeline()
    model_training.main()
    logging.info(f'<<<<<<<<<<<<<<< Stage {STAGE_NAME} Ended <<<<<<<<<<<<<<<')
    
except Exception as e:
    logging.error(f'Error Occurred: {e}')
    raise CustomException(e, sys)

STAGE_NAME = 'Model Evaluation'

try:
    logging.info(f'>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>')
    model_evaluation = ModelEvaluatePipeline()
    model_evaluation.main()
    logging.info(f'<<<<<<<<<<<<<<< Stage {STAGE_NAME} Ended <<<<<<<<<<<<<<<')
    
    logging.info(f'All stages have been executed successfully.')
    
except Exception as e:
    logging.error(f'Error Occurred: {e}')
    raise CustomException(e, sys)