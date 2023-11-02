import pandas as pd

# Function to read the data file
def read_data(file_path, **kwargs):
    """
    Read a JSON data file using Pandas and return the raw data as a DataFrame.

    :param file_path: The path to the JSON data file.
    :param **kwargs: Additional keyword arguments for reading the data.
    :return: The raw data as a Pandas DataFrame.
    """
    raw_data = pd.read_json(file_path, **kwargs)
    return raw_data

# Location to save and access the model directory
model_directory = "../models/current/Spacy_model/default/model_20230210-091453/"

# Client ID
client_id = 4
