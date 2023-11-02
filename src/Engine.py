# Import necessary modules and functions
from ML_Pipeline.utils import read_data
from ML_Pipeline.training import train_rasa
from ML_Pipeline.infer import infer_message
from ML_Pipeline.dialog import process_message
from ML_Pipeline.utils import client_id
import uuid

# Read data from a JSON file
initial_data = read_data("../data/data.json")

# Train the Rasa model using the specified data
train_rasa()
print("Training completed successfully")

# Infer Rasa intent and entity for a single message
message = "Can you tell me about television"
response = infer_message(message)
print(response)

# Start a dialog conversation and manage context
if __name__ == "__main__":
    chat_id = uuid.uuid4()
    while True:
        message = input(">>")
        response = process_message(message, client_id, chat_id)
print("Done")
