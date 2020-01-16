import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

seed = 42
engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)


# with io.open("dataset.json") as f:
#     dataset = json.load(f)

with open("dataset.json",encoding='utf-16', errors='ignore') as f:
     dataset = json.load(f, strict=False)

engine.fit(dataset)

parsing = engine.parse("Hey, lights on in the lounge !")
print(json.dumps(parsing, indent=2))