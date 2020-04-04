# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from py2neo import Graph

class SerachMedicaldb(Action):

    def name(self) -> Text:
        return "search_medicaldb"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 提取疾病类型
        disease = tracker.get_slot("Disease")

        ng = Graph(
            host="127.0.0.1",
            http_port=7474,
            user="admin",
            password="admin")
        # 查询疾病有哪些症状
        sql = "MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where m.name = '{}' return m.name, r.name, n.name".format(disease)
        ress = ng.run(sql).data()
        answer = disease + "的主要症状有："
        for symptom in ress:
            answer = answer + symptom['n.name'] + '、'

        dispatcher.utter_message(answer)

        return []
