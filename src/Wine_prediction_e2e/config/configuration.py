from src.Wine_prediction_e2e.constants import *
from src.Wine_prediction_e2e.utils.common import  read_yaml, create_directories
from src.Wine_prediction_e2e.entity.config_entity import *


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = Config_yaml_path,
        params_filepath = schema_yaml_path,
        schema_filepath = params_yaml_path):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestinConfig:
            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestinConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir 
            )

            return data_ingestion_config
