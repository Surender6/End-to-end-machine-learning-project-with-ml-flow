from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = 'data ingestion stage'
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed successfully <<<<<<<<\\nx=======")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'data validation stage'
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed successfully <<<<<<<<\\nx=======")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation stage'
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed successfully <<<<<<<<\\nx=======")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = 'Model Training Stage'
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed successfully <<<<<<<<\\nx=======")
except Exception as e:
    logger.exception(e)
    raise e