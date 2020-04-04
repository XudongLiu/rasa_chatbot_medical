

## ask disease symptom
* greet
  - utter_ask_for_what
* ask_for_disease_symptom
  - slot{"Disease":"高血压"}
  - search_medicaldb
* confirm
  - utter_goodbye


## only greet 
* greet
  - utter_greet
  - utter_ask_for_what

