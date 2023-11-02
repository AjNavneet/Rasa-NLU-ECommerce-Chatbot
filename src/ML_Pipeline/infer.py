from ML_Pipeline.utils import model_directory
from rasa_nlu.model import Metadata, Interpreter
import spacy

# Specify language as "en" for Spacy pipeline
nlp = spacy.load("en_core_web_sm")

# Load the model directory in memory using the interpreter
interpreter = Interpreter.load(model_directory)

def infer_message(message):
    """
    Infer intents and entities from the given message using the model.
    :param message: Message to be processed by the model.
    :return: Predicted intents and entities.
    """
    response = interpreter.parse(message)
    return response
