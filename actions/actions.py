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
from rasa_sdk.events import AllSlotsReset,SlotSet
from search_course import Searcher
class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        money = tracker.get_slot("amount-of-money")
        category = tracker.get_slot("category")
        keyword = tracker.get_slot("keyword")
        res = Searcher(keyword,3)
        if res['results'] > 0:
            dispatcher.utter_message(text="Đây là gợi ý của tôi dành cho bạn:")
            for x in res['data']:
                dispatcher.utter_message(image=x['thumbnail'],text=x['title'])
        else:
            dispatcher.utter_message(text=f"Hiện không có khóa học về {keyword}")

        return [SlotSet("knowledge",  res['data'][0]['knowledge'] if res['data'][0]['knowledge'] is not None else [])]

class ActionCheckKnowledge(Action):

    def name(self) -> Text:
        return "action_check_knowledge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        knowledge = tracker.get_slot("knowledge")
        if knowledge is None:
            dispatcher.utter_message(response="utter_no_course")
        else:
            dispatcher.utter_message(text="Trong khóa học này bạn sẽ học được:")
            dispatcher.utter_message(text=f"{knowledge}")

        return []

