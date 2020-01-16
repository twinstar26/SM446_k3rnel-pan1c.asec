import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
import sys

seed = 42
engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)


# with io.open("dataset.json") as f:
#     dataset = json.load(f)

with open("dataset/json/jira.json",encoding='utf-16', errors='ignore') as f:
     dataset = json.load(f, strict=False)

engine.fit(dataset)

parsing = engine.parse(sys.argv[1])
intents = engine.get_intents(sys.argv[1])

print(json.dumps(parsing, indent=2))
print(json.dumps(intents, indent=2))