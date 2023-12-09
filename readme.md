# E-Commerce Chatbot Development using Rasa NLU

## Business Goal

This project focuses on constructing an advanced chatbot for an E-Commerce platform using Rasa NLU. A chatbot serves as a versatile tool for emulating and handling human-like conversations, ranging from rule-based responses to sophisticated machine learning-driven interactions.

---

### Chatbot Categories

1. **Rule-based Chatbots:** Designed for structured queries, adhering to predefined rules.
2. **AI-based Chatbots:** Incorporating machine learning, our project falls into this category, emphasizing understanding context and delivering natural language responses.

The efficacy of AI-driven chatbots hinges on grasping two fundamental elements:

- **Intent:** User message's intention or purpose.
- **Entity:** A specific extractable data point or value from a conversation.

---

## Data Insight

Our E-Commerce chatbot derives data from sources like the Rasa NLU Trainer and Chatito. The critical aspects considered for our business case are:

- **Intents:** product_info, ask_price, cancel_order
- **Entities:** product, location, order_id

---

## Technological Arsenal

- **Language:** `Python`
- **Libraries:** `pandas`, `matplotlib`, `Rasa`, `pymongo`, `TensorFlow`, `spaCy`

---

## Strategic Approach

1. **Data Collection:** Gather relevant data from diverse sources.
2. **Library Integration:** Import necessary packages and libraries.
3. **Data Integration:** Import and structure the acquired data.
4. **Data Transformation:** Convert data into training and testing dataframes.
5. **Data Serialization:** Convert dataframes to JSON files.
6. **Exploratory Analysis:**
   - Visualize data for insights.
7. **Configuration Setup:** Create YAML files for spaCy and TensorFlow configurations.
8. **Model Development:**
   - Establish a function for Rasa NLU model training.
9. **Performance Evaluation:**
   - Develop a function for model evaluation using test data.
10. **Training Iterations:**
   - Train the model using spaCy and TensorFlow pipelines.
11. **Evaluation Metrics:**
   - Construct confusion matrices for both models.
12. **Model Understanding:**
   - Interpretation of model decisions.
13. **Database Integration:**
   - Install MongoDB and integrate pymongo.
14. **Chatbot Components:**
   - Implement IntentFlow and ContextManager classes.
15. **Message Processing:**
   - Develop a function for message processing.
16. **Testing and Deployment:**
   - Validate the chatbot's functionality.

---

## Code Structure

1. **Input Folder:** Holds data and configuration files.
2. **Src Folder:** Encompasses modular code in `Engine.py` and `ML_Pipeline` directories.
3. **Output Folder:** Stores the optimized model for future deployment.
4. **Lib Folder:** Houses reference IPython notebook.

---
