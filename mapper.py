#!/usr/bin/env python

import sys
list1 = []
linespliter= []
# input comes from STDIN (standard input)
for line in sys.stdin:
     
     #key1,key2,value = line.split(',')
     linespliter=line.split(',')
    # print linespliter
     key1=linespliter[0]
     key2=linespliter[2]
     value=linespliter[7]	
     #print  key1,key2,value
     L= len(key2) 
     cnt=1
     list1=[]
     for i in key2:
	  if cnt>L-4:
  	      list1.append(i)
	  cnt=cnt+1
     #print list1
     strlist1 =''.join(list1)
     #print strlist1
     key = key1+","+str(strlist1)+":"
     print '%s\t%s' % (key,value)     
    
 
    
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
     #   print '%s\t%s' % (word, 1)

