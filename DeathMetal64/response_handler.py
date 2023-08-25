import command_handler
import random
import json


def response_handler(trigger: str) -> str:
    with open('responses.json', 'r') as json_file:
        responses_data = json.load(json_file)

    triggers = responses_data["prompts"]
    response = triggers[trigger]["response"]
    if trigger in triggers:
        return response
