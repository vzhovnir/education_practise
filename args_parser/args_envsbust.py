#!/usr/bin/env python3
import string
import sys
import argparse
from jproperties import Properties
parser = argparse.ArgumentParser(description="T")
parser.add_argument("env", type=open,help="env file ")
parser.add_argument("template", type=open,help="template file ")
parser.add_argument("out", type=open, nargs='?',help="out file")
args = parser.parse_args()
def export(file_name,dict_paramameters,new_file_name):
    t=""
    content=file_name.read()
    t = string.Template(content).substitute(dict_paramameters)
    print(t)  
    with open(new_file_name.name,"w+") as f:
        f.write(str(t)+'\n')
def Parser():
    dict_paramameters=Properties()
    dict_paramameters.load(args.env)
    export(file_name=args.template,dict_paramameters=dict_paramameters,new_file_name=args.out)
    print ("Success")    

    


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        Parser()
    else: 
        print("Call {} -h".format(argv[0]))     