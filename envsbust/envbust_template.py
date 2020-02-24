#!/usr/bin/env python3
import string
import sys


dict_paramameters= {'Mobile':'+38099999999',
'Office': 'Grid Dynamics',
 'Position':'Intern'}


def export():
    file_name = sys.argv[1]
    new_file_name = "upt_" + file_name
        with open(file_name,"r") as f:
            content = f.read()
        t = string.Template(content).substitute(values)
        with open(new_file_name,"w+") as f:
            f.write(str(t)+'\n')
        
    


if __name__ == '__main__':
     main()