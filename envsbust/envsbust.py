#!/usr/bin/env python3

import sys 
from subprocess import run


dict_paramameters= {'Mobile':'+38099999999',
'Office': 'Grid Dynamics',
 'Position':'Intern'}


def main():
    read_line=[]
    file_name = sys.argv[1]
    new_file_name = "upt_" + file_name
    k=[]
    with open(file_name, 'r') as f :
        for i in f :
            read_line+=[i.format(**dict_paramameters)]
            k=[read_line.replace('$','') for read_line in k]
            read_line=k
    with open(new_file_name,"w") as f:
            for i in read_line:
                f.write(i+'\n')
                

if __name__ == '__main__':
     main()