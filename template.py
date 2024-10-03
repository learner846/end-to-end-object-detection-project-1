import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Sign language"



list_of_the_files = [
    "data/.gitkeep",
    "{project_name}/__init__.py",
    "{project_name}/components/__init__.py",
    "{project_name}/components/data_ingestion.py",
    "{project_name}/components/data_validation.py",
    "{project_name}/components/model_trainer.py",
    "{project_name}/components/model_pusher.py",
    "{project_name}/configuration/__init__.py",
    "{project_name}/configuration/s3_operations.py",
    "{project_name}/constant/__init__.py",
    "{project_name}/constant/training_pipeline/__init__.py",
    "{project_name}/constant/application.py",
    "{project_name}/entity/__init__.py",
    "{project_name}/entity/artifacts_entity.py",
    "{project_name}/entity/config_entity.py",
    "{project_name}/exception/__init__.py",
    "{project_name}/logger/__init__.py",
    "{project_name}/pipeline/__init__.py",
    "{project_name}/pipeline/training_pipeline.py",
    "{project_name}/utils/__init__.py",
    "{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "Setup.py"
]

for filepath in list_of_the_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already created")