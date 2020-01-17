import json
import shutil
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

seed = 42   
engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)

datasetName = 'dataset1.json'

with open("/k3rnel-pan1c.asec/NLU/dataset/json/"+datasetName, encoding='utf-16', errors='ignore') as f:
    dataset = json.load(f, strict=False)
# with open("/home/twinstar/projects/k3rnel-pan1c.asec/NLU/dataset/json/"+datasetName, encoding='utf-8', errors='ignore') as f:
#     dataset = json.load(f, strict=False)

print("TRAINING THE ENGINE...")

engine.fit(dataset)

shutil.rmtree("/k3rnel-pan1c.asec/NLU/trained_model")
engine.persist("/k3rnel-pan1c.asec/NLU/trained_model")
# shutil.rmtree("/home/twinstar/projects/k3rnel-pan1c.asec/NLU/trained_model")
# engine.persist("/home/twinstar/projects/k3rnel-pan1c.asec/NLU/trained_model")

print("ENGINE TRAINED.")