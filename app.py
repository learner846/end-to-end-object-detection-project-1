# from signlanguage.pipeline.training_pipeline import TrainPipeline

# obj = TrainPipeline()
# obj.run_pipeline()

import logging
import os
from signlanguage.pipeline.training_pipeline import TrainPipeline

# Create a logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Log file path
log_file_path = os.path.join(log_dir, "app.log")

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    filemode='a',  # Append mode ('w' for overwrite)
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,  # Set the minimum log level to INFO
)

# Run the pipeline
if __name__ == "__main__":
    obj = TrainPipeline()
    obj.run_pipeline()

    logging.info("Pipeline run completed.")