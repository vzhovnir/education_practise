#!/bin/bash
usage_a(){
    echo "Usage: $0 < -a key> <envfile> <inputfile> <output file >" 1>&2
    exit 1
}
usage_b(){
    echo "Usage: $0 < -b key> <envfile> <inputfile>" 1>&2
    exit 1
}
envfile=$2
inputfile=$3
    while getopts ":ab:" opt; do
                case "${opt}" in 
                    a)
                        outputfile=$4
                        echo $#  
                        if [[ $# -ge 3 ]] && [[ $# -le 4 ]];then 
                        
                            if [[ -e ${envfile} && -r ${envfile} && -s ${envfile} ]]; then
                                 export $(grep -v "^#" ${envfile} | xargs -0)
                                 if [[ -e ${inputfile} && -r ${inputfile} && -s ${inputfile} ]]; then
                                     (echo "cat <<EOF";cat "${inputfile}";) | sh 2>/dev/null 1>$outputfile
                                     echo "Good Job"
                                 else 
                                     usage_a            
                                 fi
                            else 
                            usage_a            
                            fi

                        else 
                            usage_a
                        fi
                          ;;
                    
                    b)
                        if [[ -e ${envfile} && -r ${envfile} && -s ${envfile} ]]; then
                             export $(grep -v "^#" ${envfile} | xargs -0)
                             if [[ -e ${inputfile} && -r ${inputfile} && -s ${inputfile} ]]; then
                                (echo "cat <<EOF";cat "${inputfile}";) | sh 2>/dev/null 
                                echo "Good Job"
                                
                            else 
                            usage_b            
                            fi

                        else 
                            usage_b
                        fi
                          ;;
                    *)
                        echo "Please choose key -a or -b"
                        ;;
                esac
            done
