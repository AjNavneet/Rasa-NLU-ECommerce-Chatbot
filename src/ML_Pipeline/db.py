from pymongo import MongoClient
import requests

class IntentFlow:
    def __init__(self, client_id):
        """
        Initialize the IntentFlow object for managing client-specific intent flows.
        :param client_id: Client identifier to store intent flow per client.
        """
        # Initialize MongoDB client
        self.mongo_client = MongoClient('localhost:27017')
        self.db = self.mongo_client.chatflowdb
        self.intent_table = self.db['chatflow']
        self.client_id = client_id

    def add_flows(self, flow):
        """
        Inserts a specified flow per client.
        :param flow: Flow to insert.
        :return: None
        """
        self.intent_table.insert_one({
            "client_id": self.client_id,
            "flow": flow,
        })

    def resolve_api(self, url):
        """
        Calls an API to resolve data.
        :param url: URL of the API.
        :return: Response from the API.
        """
        response = requests.request("GET", url)
        return response.json()

    def extract_api(self, intent_name):
        """
        Extracts API details for a specific intent.
        :param intent_name: Name of the intent to extract API details for.
        :return: Response from the resolved API.
        """
        response = self.intent_table.find_one({"client_id": self.client_id, "flow.intent": intent_name})
        api_url = response['flow']['api_data']['url']
        response = self.resolve_api(api_url)
        return response

    def get_flows(self):
        """
        Returns flows associated with the given client id.
        :return: List of flows.
        """
        response = self.intent_table.find({
            "client_id": self.client_id,
        })
        return list(response)

    def get_slots_by_intent(self, intent_name):
        """
        Returns slots that need to be fulfilled before triggering an API for a given intent.
        :param intent_name: Name of the intent.
        :return: List of slots.
        """
        response = self.intent_table.find_one({
            "client_id": self.client_id,
            "flow.intent": intent_name})
        slots = None
        if response:
            slots = response['flow']['entities']
        return slots

class ContextManager:
    def __init__(self, client_id, chat_id):
        """
        Initialize the ContextManager for managing chat-specific context.
        :param client_id: Client identifier.
        :param chat_id: Chat identifier to store context per chat window.
        """
        # Initialize MongoDB client
        self.mongo_client = MongoClient('localhost:27017')
        self.db = self.mongo_client.chatflowdb
        self.chat_session = self.db['chatsession']
        self.client_id = client_id
        self.chat_id = chat_id

    def get_context(self):
        """
        Returns the context stored for a given chat_id.
        :return: Chat context.
        """
        response = self.chat_session.find_one(
            {"chat_id": self.chat_id})
        return response

    def update_slots(self, intent=None, entity=None):
        """
        Updates intent and entity for a given chat_id.
        :param intent: Intent to update.
        :param entity: Entity to update.
        :return: None
        """
        if intent:
            self.chat_session.find_one_and_update(
                {"chat_id": self.chat_id},
                {"$set": {"intent": intent}},
                upsert=True
            )
        if entity:
            self.chat_session.find_one_and_update(
                {"chat_id": self.chat_id},
                {"$push": {"entity": entity}},
                upsert=True
            )

    def get_filled_slots(self):
        """
        Returns all the filled slots in the given context for a given chat_id.
        :return: List of filled slots.
        """
        response = self.chat_session.find_one(
            {"chat_id": self.chat_id})
        filled_slots = None
        if response and "entity" in response:
            filled_slots = response['entity']
        return filled_slots

    def get_slots(self, intent_name):
        """
        Returns slots that are not filled for a given intent.
        :param intent_name: Name of the intent.
        :return: List of not-filled slots.
        """
        intent_flow_obj = IntentFlow(self.client_id)
        slots = intent_flow_obj.get_slots_by_intent(intent_name)

        if slots:
            filled_slots = self.get_filled_slots()
            not_filled_slots = [ent for ent in slots if ent['entity'] not in filled_slots]
            return not_filled_slots
        else:
            print("No flow found for this intent")
