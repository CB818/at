# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher
 from rasa_sdk.forms import FormAction


 class ActionSaveData(Action):
    
     def name(self) -> Text:
         return "action_save_data"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         DataStore(tracker.get_slot("name"),
            tracker.get_slot("email"),
            tracker.get_slot("Address"),
            tracker.get_slot("City"),
            tracker.get_slot("State"),
            tracker.get_slot("Zip"),
            tracker.get_slot("Phone"))
         dispatcher.utter_message(text="Data Stored Successfully")
        return []
 
  class FormDataCollect(FormAction):
        def name(self) -> Text:
            return "Form_Info"
        @staticmethod:
        def required_slots(tracker: "Tracker") -> List[Text]:
            return ["name","email","Address","City","State","Zip","Phone"]
        def slot_mapping(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
            return{
                "name":[self.from_text()],
                "email":[self.from_entity(entity="email")],
                "Address":[self.from_entity(entity="Address")],
                "City":[self.from_entity(entity="City")],
                "State":[self.from_entity(entity="State")],
                "Zip":[self.from_entity(entity="Zip")],
                "Phone":[self.from_entity(entity="Phone")],
            }
        def submit(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: Dict[Text, Any],
        ) -> List[EventType]:
            dispatcher.utter_message("Here is the information that you provided. Is this correct?\nname: {0},\nemail: {1},\nAddress: {2},\nCity: {3},\nState: {4},\nZip: {5},\nPhone: {6})
            tracker.get_slot("name"),
            tracker.get_slot("email"),
            tracker.get_slot("Address"),
            tracker.get_slot("City"),
            tracker.get_slot("State"),
            tracker.get_slot("Zip"),
            tracker.get_slot("Phone")
            return[]
            

