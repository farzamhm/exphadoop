#!/usr/bin/env python

# from operator import itemgetter
import sys
import numpy as np

cr_key_loc = None
pr_key_loc = None
lst = []
loc = []
i = 0
# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace
    # line = line.strip()
    # print line
    loc = line.split(":\t")
    # print loc
    # print loc[0]
    cr_key_loc = loc[0]
    value = loc[1]
    f_value = float(value)
    lst.append(f_value)
    i = i + 1
    if cr_key_loc == pr_key_loc:
        continue
    # print key_loc, value
    # print f_value
    else:
        min_value = min(lst)
        max_value = max(lst)
        median_value = np.median(lst)
        std_dev_value = np.std(lst)
		#print "Location year: minimum value maximum value median Standard deviation"
        print cr_key_loc + "==> MIN: " + str(min_value)+" MAX: "+ str(max_value)+" Median: "+str(median_value)+" STD-DEV: "+str(std_dev_value)
        lst = []
        pr_key_loc = cr_key_loc
print i
