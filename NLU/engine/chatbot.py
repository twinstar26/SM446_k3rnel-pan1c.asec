import json
import sys
from snips_nlu import SnipsNLUEngine

#engine = SnipsNLUEngine.from_path("/k3rnel-pan1c.asec/NLU/trained_model")
engine = SnipsNLUEngine.from_path("/home/twinstar/projects/k3rnel-pan1c.asec/NLU/trained_model")

if __name__=="__main__":
    user_intent_text = input()

    parsing = engine.parse(user_intent_text)
    intents = engine.get_intents(user_intent_text)

    print(json.dumps(parsing, indent=2))
    print(json.dumps(intents, indent=2))