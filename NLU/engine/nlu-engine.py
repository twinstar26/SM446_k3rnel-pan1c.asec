import json
import os
import shutil
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

seed = 42   
engine = SnipsNLUEngine(config=CONFIG_EN, random_state=seed)

dataset_name = 'dataset1.json'

get_current_working_directory = os.getcwd()
splitted_current_working_directory = os.path.split(get_current_working_directory)
directory_index = splitted_current_working_directory.index('NLU')
root_directory_path = os.path.join(*splitted_current_working_directory[:directory_index+1])

dataset_path = os.path.join(root_directory_path, 'dataset', 'json', dataset_name)

with open(dataset_path, encoding='utf-16', errors='ignore') as f:
    dataset = json.load(f, strict=False)

print("TRAINING THE ENGINE...")

engine.fit(dataset)

shutil.rmtree(os.path.join(root_directory_path, 'trained_model'))
engine.persist(os.path.join(root_directory_path, 'trained_model'))

print("ENGINE TRAINED.")