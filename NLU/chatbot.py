import json
import sys
from snips_nlu import SnipsNLUEngine

engine = SnipsNLUEngine.from_path("/k3rnel-pan1c.asec/NLU/trained_model")

parsing = engine.parse(sys.argv[1])
intents = engine.get_intents(sys.argv[1])

print(json.dumps(parsing, indent=2))
print(json.dumps(intents, indent=2))