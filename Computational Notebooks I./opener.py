
#! /usr/bin/env python
import sys
import os
import json



print("Your argument: ", sys.argv[1])

nb_path = os.path.abspath("01.ipynb")
nb = open(nb_path,"r")
content = json.load(nb)
nb.close()

content["cells"][0]["source"][0] = content["cells"][0]["source"][0] + ' ' + sys.argv[1][2:]

with open(nb_path, "w") as outfile:  
    json.dump(content, outfile)


