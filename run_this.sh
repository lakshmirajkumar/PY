#!/bin/sh

a=500001

while [ $a -lt 500100 ]
do
   echo $a
#   python code_filter.py filtered_data/voda_pre/vodafone_prepaid.txt $a > filtered_data/voda_pre/$a.txt   
    python zip.py filtered_data/airtell_pre/airtell_prepaid.txt $a > filtered_data/airtell_pre/$a.txt   
   a=`expr $a + 1`
done

