# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import datetime
import xlrd
from typing import Text, List, Optional, Union
from rasa_sdk.forms import FormAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import ReminderScheduled, ReminderCancelled

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class SetAntecedentesSi(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_antecedentes_si"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("antecedentes", "si")]

class SetAntecedentesNo(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_antecedentes_no"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = 'no'

        return [SlotSet("antecedentes", "no")]
class SetChatbotBien(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_chatbot_bien"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = 1
        res_fin = tracker.slots.get("res_final")
        resultado_final = (res_fin + 1)
        return [SlotSet("res_chatbot", res), SlotSet("res_final", resultado_final)]

class SetChatbotMal(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_chatbot_mal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = -1
        res_fin = tracker.slots.get("res_final")
        resultado_final = (res_fin - 1)
        return [SlotSet("res_chatbot", res), SlotSet("res_final", resultado_final)]



class ActionSessionStart(Action):
    # return the name of the action
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("utter_bienvenida"))
        dispatcher.utter_message(response="utter_bienvenida")


        return events

class SetResultadoDefs(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_defs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("res_def")

        resultado = (int(res)+1)
        print(resultado)
        res_fin = tracker.slots.get("res_final")
        resultado_final = (int(res_fin) + 1)
        return [SlotSet("res_def", resultado), SlotSet("res_final", resultado_final)]



class SetResultadoListaDespues(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_lista_despues"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("lista_compra")
        print(res)
        resultado = 0
        resultado = len(tracker.get_slot("lista_compra"))
        print(resultado)
        res_fin = tracker.slots.get("res_final")
        resultado_final = (res_fin + resultado)
        return [SlotSet("res_lista_despues", resultado), SlotSet("res_final", resultado_final)]



class SetResultadoListaInmediata(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_lista"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("lista_compra")
        dispatcher.utter_message(res)
        print(res)
        resultado = 0
        dispatcher.utter_message("Hemos llegado hasta LISTA", res)
        resultado = len(tracker.get_slot("lista_compra"))
        dispatcher.utter_message("Hemos llegado hasta RESULTADO", resultado)
        print(resultado)
        res_fin = tracker.slots.get("res_final")
        resultado_final = (res_fin + resultado)
        return [SlotSet("res_lista_inmediata", resultado), SlotSet("res_final", resultado_final)]



class SetResultadoPropios(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_propios"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("res_propios")
        resultado = (int(res)+1)
        print(resultado)
        res_fin = tracker.slots.get("res_final")
        resultado_final = (res_fin + 1)
        return [SlotSet("res_propios", resultado), SlotSet("res_final", resultado_final)]



class SetResultadoObjetos(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_obj"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("res_objetos")
        resultado = (int(res)+1)
        res_fin = tracker.slots.get("res_final")
        resultado_final = (res_fin + 1)
        print(resultado)
        print(resultado_final)
        return [SlotSet("res_objetos", resultado), SlotSet("res_final", resultado_final)]



class ProbabilidadInicial(Action):
    # return the name of the action
    def name(self) -> Text:
        return "probabilidad_inicial"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get all the entities extracted by rasa
        name= tracker.slots.get("name")
        ages= tracker.slots.get("age")
        antecedentes= tracker.slots.get("antecedentes")
        prob = 1

        # sanity check to ensure that it was filled by rasa
        if name and ages and antecedentes:
            json = ''.join([name, ages, antecedentes])
            age = int(ages)

            if age < 65 and antecedentes:
                prob = 0
            elif (age > 65 and age < 75):
                if antecedentes == "no":
                    prob = 0
                elif antecedentes == "si":
                    prob = 1
            elif age > 75:
                if antecedentes == "no":
                    prob = 1
                elif antecedentes == "si":
                    prob = 2
            # dispatcher.utter_message("Hemos llegado hasta NOMBRE", name)
        else:
            prob=1

        print("PROB",prob)
        json = json.join(str(prob))
        return [SlotSet("prob", prob), ("json", json)]


class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Tiempo puesto")
        print("Tiempo puesto")

        date = datetime.datetime.now() + datetime.timedelta(seconds=30)

        reminder = ReminderScheduled(
            "hacer_preg2",
            trigger_date_time=date,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:


        dispatcher.utter_message("Tiempo!")

        return []

class ActionSetFinalResult(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_set_final_result"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        prob = tracker.slots.get("prob")
        resultado_final = tracker.slots.get("res_final")
        res = resultado_final - prob
        #dispatcher.utter_message("El resultado es", res)
        SlotSet("res_final", res)
        # Use a service account 
        #cred = credentials.Certificate('prueba-e35e9-effc66479193.json')
        #firebase_admin.initialize_app(cred)
        #doc_ref = db.collection('datos').document('alovelace232')
        #db = firestore.client()
        if res < 21:
            # dispatcher.utter_message(text = "Hemos llegado hasta PROB 2")
            # dispatcher.utter_message(response="utter_res2")
            texto = "Los resultados del test son más bajos de lo esperado. Esto podría llegar a indicar los primeros síntomas de un trastorno cognitivo como la enfermedad del Alzheimer. Los resultados de este test no son definitivos pero le recomiendo que consulte con personal sanitario cualificado."
            # dispatcher.utter_message(text=texto)
            return [SlotSet("resultado_final",  texto)]

        elif 20 < res < 29:
            # dispatcher.utter_message(text ="Hemos llegado hasta PROB 1")
            # dispatcher.utter_message(response="utter_res1")
            return [SlotSet("resultado_final","Los resultados del test no son tan altos como lo esperado. Esto podría llegar a indicar los primeros síntomas de un trastorno cognitivo como el Deterioro Cognitivo leve. Los resultados de este test no son definitivos pero le recomiendo que consulte con personal sanitario cualificado.")]
        elif res > 28:
            # dispatcher.utter_message(text = "Hemos llegado hasta PROB 0")
            # dispatcher.utter_message(response="utter_res0")
            return [SlotSet("resultado_final", "Los resultados del test son satisfactorios. No muestran ningún síntoma de algún trastorno cognitivo.")]

        return []











