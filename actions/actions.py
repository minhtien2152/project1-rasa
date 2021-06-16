# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_check_keyword"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category = tracker.get_slot("category")
        keyword = tracker.get_slot("keyword")


        if category is None and keyword is None:
            dispatcher.utter_message(response="utter_ask_for_keyword")
        
        return []

class ActionCheckPriceRange(Action):

    def name(self) -> Text:
        return "action_check_price_range"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        money = tracker.get_slot("amount-of-money")

        if money is None:
            dispatcher.utter_message(response="utter_ask_for_price_range")

        return []

class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        money = tracker.get_slot("amount-of-money")
        category = tracker.get_slot("category")
        keyword = tracker.get_slot("keyword")

        response = requests.get(url="http://localhost:8088/api/courses/", params={'keyword':keyword})
        res = response.json()
        if res['results'] > 0:
            dispatcher.utter_message(text=res['data'][0]['title'])
        else:
            dispatcher.utter_message(text=f"Hiện không có khóa học về {keyword}")
        dispatcher.utter_message(text=f"{category}, {keyword}, {money}, {response.status_code}")

        return []

