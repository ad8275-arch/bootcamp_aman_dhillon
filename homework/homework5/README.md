Data Storage:

.env file is used to store paths for data directories:

DATA_DIR_RAW=data/raw

DATA_DIR_PROCESSED=data/processed

data/raw/ → stores CSV files (raw, unmodified data)

data/processed/ → stores Parquet files (cleaned/processed data)

Validation ensures that:

DataFrame shapes are the same after saving and reloading

Column data types remain consistent