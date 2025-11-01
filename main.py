from Wine_prediction_e2e import logger
from Wine_prediction_e2e.pipeline.Data_ingestion_stage import DataIngestionTrainingPipeline
from Wine_prediction_e2e.pipeline.Data_validation_stage import DataValidationTrainingPipeline
from Wine_prediction_e2e.pipeline.Data_transformation_stage import DataTransformationTrainingPipeline
from Wine_prediction_e2e.pipeline.Model_trainer_stage import ModelTrainerTrainingPipeline
from Wine_prediction_e2e.pipeline.Model_evaluation_stage import ModelEvaluationTrainingPipeline

STAGE_NAME = "<<<<<<<Data Ingestion stage>>>>>>>>>"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e