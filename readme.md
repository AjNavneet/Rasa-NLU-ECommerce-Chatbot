# Rasa NLU Chatbot for E-Commerce

## Business Objective

A chatbot is a powerful tool for simulating and processing human conversation, which can be as simple as answering questions based on predefined rules or as complex as using machine learning to understand context and provide more natural responses. In this project, we aim to build an AI-based chatbot for an E-Commerce business scenario using the Rasa NLU model.

---

### Types of Chatbots

There are two main types of chatbots:

- Rule-based chatbots: These bots follow predefined rules and are suitable for handling structured queries.
- AI-based chatbots: AI chatbots, like the one we're building, use machine learning to understand context and provide natural language responses.

The effectiveness of AI-driven chatbots depends on understanding two core concepts:

- **Intent**: The intention or purpose of the user's message.
- **Entity**: A specific data point or value that can be extracted from a conversation.

---

## Data Description

The data for our E-Commerce chatbot can be curated from sources such as the Rasa NLU Trainer and Chatito. For our business case, we consider:

- Intents: product_info, ask_price, cancel_order
- Entities: product, location, order_id

---

## Tech Stack

- Language: `Python`
- Libraries: `pandas`, `matplotlib`, `Rasa`, `pymongo`, `TensorFlow`, `spaCy`

---

## Approach

1. Data Curation: Collect data from relevant sources.
2. Import Required Packages and Libraries.
3. Import the Data.
4. Convert Data into Training and Testing Dataframes.
5. Convert Dataframes to JSON Files.
6. Exploratory Data Analysis (EDA):
   - Data Visualization.
7. Create Configuration Files (.yaml) for spaCy and TensorFlow.
8. Model Building:
   - Define a function to train the Rasa NLU model.
9. Model Evaluation:
   - Define a function to evaluate the model on test data.
10. Train the Data using spaCy as the pipeline.
11. Train the Data using TensorFlow as the pipeline.
12. Plot Confusion Matrix for Both Models.
13. Model Interpretation.
14. Install MongoDB and Import pymongo.
15. Create an IntentFlow class.
16. Create a ContextManager class.
17. Create a Function for Processing Messages.
18. Test the Chatbot.

---

## Modular Code Overview

1. **Input**: Contains data files and configuration files.
2. **Src**: Contains modularized code in the `Engine.py` and `ML_Pipeline` folders.
3. **Output**: Contains the best-fitted model, which can be loaded and used for future deployments.
4. **Lib**: Includes reference IPython notebook.

---

## Key Concepts Explored

1. Chatbot development and its applications.
2. Understanding different chatbot types.
3. Core concepts of intent and entity.
4. Data curation and preprocessing.
5. Training and evaluating the Rasa NLU model.
6. Model interpretation and evaluation using confusion matrices.
7. Integration with MongoDB.
8. Creating an effective chatbot for E-Commerce scenarios.

---

