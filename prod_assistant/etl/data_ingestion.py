import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from prod_assistant.utilis.model_loader import ModelLoader
from prod_assistant.utilis.config_loader import load_config

class DataIngestion:
    """class to handle data transformation and ingestion"""
    def __init__(self):
        if os.getenv("ENV", "local").lower() != "production":
            load_dotenv()
            log.info("Running in LOCAL mode: .env loaded")
        else:
            log.info("Running in PRODUCTION mode")

        self.api_key_mgr = ApiKeyManager()
        self.config = load_config()
        log.info("YAML config loaded", config_keys=list(self.config.keys()))


    def_load_env_variable(self):
        pass

    def _get_csv_path(self):
        pass

    def _load_csv(self):
        pass

    def transform_data(self):
        pass

    def store_in_vector_db(self):
        pass

    def run_pipeline(self):
        pass
   
