import os

DATA_DIR: str = os.getenv("DATA_DIR", os.path.join(os.getcwd(), "..", "data"))