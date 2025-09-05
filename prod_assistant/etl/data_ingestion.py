import os
import pandas as pd
from dotenv import load_dotenv
from typing import List
from langchain_core.documents import Document
from prod_assistant.utilis.model_loader import ModelLoader
from prod_assistant.utilis.config_loader import load_config

class DataIngestion:
    
