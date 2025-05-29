import os
from pathlib import Path
import logging


project_name = "telekom_forecast"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/assign_revenue.py",
    f"src/{project_name}/generate_monthly_data.py",
    f"src/{project_name}/forecast_revenue.py",
    f"src/{project_name}/ml_model_training.py",
    f"src/{project_name}/logging/logger.py",
    "streamlit_app/app.py",
    "notebooks/EDA_Financial_KPIs.ipynb",
    "data/.gitkeep",
    "models/.gitkeep",
    "logs/.gitkeep",
    "Dockerfile",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            f.write("")  # creates an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
