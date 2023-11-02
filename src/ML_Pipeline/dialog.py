from ML_Pipeline.db import ContextManager, IntentFlow
from ML_Pipeline.infer import interpreter

def process_message(message, client_id, chat_id):
    """
    Process a chat message using ML models and provide a response or prompt for unfulfilled slots.
    :param message: Chat message from the user.
    :param client_id: Client identifier.
    :param chat_id: Chat identifier for storing context.
    :return: Response or prompt for unfulfilled slots.
    """
    # Predict intent from the message using Rasa NLU pipeline
    response = interpreter.parse(message)
    intent_pred = response['intent']['name']
    intent_conf = response['intent']['confidence']

    # Check if confidence is greater than 90% to consider it as the intent
    intent = None
    if intent_conf > 0.90:
        intent = intent_pred

    entities_pred = response['entities']

    # Initialize the context object by client and chat id
    context_manager = ContextManager(client_id, chat_id)

    # Check if there is an existing intent in the context
    try:
        context = context_manager.get_context()
        if "intent" in context.keys():
            intent_context = context['intent']
            # Check if the predicted intent and the intent stored in the context are the same
            if intent_context == intent:
                intent = intent_context
            else:
                if intent:
                    return "Do you want to change the intent?"
                else:
                    intent = intent_context
    except:
        # No context has been saved yet for this chat
        if intent:
            context_manager.update_slots(intent=intent)

    if entities_pred:
        for each_ent in entities_pred:
            # Push each entity label and text if the confidence is greater than 0.60 to the context
            entity = each_ent['entity']
            value = each_ent['value']
            conf = each_ent['confidence']
            if conf > 0.60:
                context_manager.update_slots(entity=entity)

    # Get the slots for that intent given the chat_id
    response = context_manager.get_slots(intent)

    if response:
        prompt_question = response[0]['prompt']
        return prompt_question
    else:
        # Get the API response for the specified client and intent
        intent_obj = IntentFlow(client_id)
        response = intent_obj.extract_api(intent)
        return response
