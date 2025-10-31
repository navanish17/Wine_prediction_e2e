import os
import urllib.request as request
import zipfile
from Wine_prediction_e2e import logger
from Wine_prediction_e2e.utils.common import get_size
import rarfile
import gdown
from src.Wine_prediction_e2e.entity.config_entity import *

class DataIngestion:
    def __init__(self, config: DataIngestinConfig):
        self.config = config

    def download_file(self):
        """Downloads file from Google Drive safely."""
        file_url = self.config.source_URL
        local_path = self.config.local_data_file

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        print("⬇️ Downloading file from Google Drive...")
        gdown.download(url=file_url, output=local_path, quiet=False)
        print("✅ Download completed:", local_path)

    
    def extract_rar_file(self):
        """
        Extracts the .rar file into the data directory.
        Function returns None.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        rar_path = self.config.local_data_file

        # check file extension (optional safety)
        if not rar_path.endswith(".rar"):
            raise ValueError("❌ File is not a .rar file!")

        # open and extract rar file
        with rarfile.RarFile(rar_path, 'r') as rar_ref:
            rar_ref.extractall(unzip_path)

        print(f"✅ RAR file extracted successfully to: {unzip_path}")