import json
import sys
import pathlib
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

seed = 42
engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)

with open(str(pathlib.Path().absolute()) + '/dataset/json/dataset1.json', errors='ignore') as f:
     dataset = json.load(f, strict=False)

engine.fit(dataset)

parsing = engine.parse(sys.argv[1])
intents = engine.get_intents(sys.argv[1])

print(json.dumps(parsing, indent=2))
print(json.dumps(intents, indent=2))