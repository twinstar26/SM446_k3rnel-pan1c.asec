import os
import json
import sys
from snips_nlu import SnipsNLUEngine

get_current_working_directory = os.getcwd()
splitted_current_working_directory = os.path.split(get_current_working_directory)
directory_index = splitted_current_working_directory.index('NLU')
root_directory_path = os.path.join(*splitted_current_working_directory[:directory_index+1])

engine = SnipsNLUEngine.from_path(os.path.join(root_directory_path, 'trained_model'))

if __name__=="__main__":
    user_intent_text = input()

    parsing = engine.parse(user_intent_text)
    intents = engine.get_intents(user_intent_text)

    print(json.dumps(parsing, indent=2))
    print(json.dumps(intents, indent=2))