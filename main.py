from Wine_prediction_e2e import logger
from Wine_prediction_e2e.pipeline.Data_ingestion_stage import DataIngestionTrainingPipeline

STAGE_NAME = "<<<<<<<Data Ingestion stage>>>>>>>>>"


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e