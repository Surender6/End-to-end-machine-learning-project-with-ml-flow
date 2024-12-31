from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'data ingestion stage'
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed successfully <<<<<<<<\\nx=======")
except Exception as e:
    logger.exception(e)
    raise e