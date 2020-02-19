#!/bin/bash
for num in {1..100} ; do
  out=""
     if [ $(($num % 3)) -eq 0 ] 
then    
     out="Fizz"
fi
     if [ $(($num % 5)) -eq 0 ] 
then    
     out="${out}Buzz"
fi
     echo ${out:-$num}
done