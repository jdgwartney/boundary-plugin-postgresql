#!/usr/bin/env python
import sys
import json
from postgresql import PgInfo
from os import path
from pprint import pprint

paramFile="param.json"

if path.isfile(paramFile):
	print "File exists and is readable"
	with open(paramFile) as data_file:    
		data = json.load(data_file)
	print(data["host"])

else:
    print "Either file is missing or is not readable"


