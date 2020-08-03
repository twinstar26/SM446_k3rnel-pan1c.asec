from gen import synonymous
from ruamel import yaml
import os
from gen import synonymous

def update_utterances(intent, query, file_name):
    input_filename = "yaml/" + str(file_name) + ".yaml"
    output_filename = "yaml/" + str(file_name) + "_temp.yaml"
    inp =  open(input_filename, 'r+')
    op = open(output_filename, 'w+')
    input = yaml.load_all(inp, yaml.RoundTripLoader)
    go = False
    utterances = []
    expand = synonymous(query)
    for s in expand:
        utterances.append(s[0])
    bk = False
    for i in input:
        for k, v in i.items():
            if(v == intent):
                go = True
            if(k == "utterances" and go):
                v.extend(utterances)
                bk = True
            if(bk):
                break
        yaml.dump(i, op, Dumper=yaml.RoundTripDumper, explicit_start=True)
        if(bk):
            break

    inp.close()
    op.close()

    clean_up(output_filename, input_filename)


def clean_up(file_a, file_b):
    inp = open(file_a, "r")
    op = open(file_b, "w+")

    input = inp.readlines()
    op.writelines(input)

    inp.close()
    op.close()

    os.remove(file_a)

# update_utterances("commentById", [["Give me pull-request made by josh"]],"comments")