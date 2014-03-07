#!/usr/bin/env python2.7
 
import sys
from datetime import datetime

def float_zero(str):
    try:
        return float(str)
    except:
        return 0.0



countries = {}
f = open('../countrycodes.csv')
for line in f:
    toks = line.split(',')
    countries[toks[3].strip()] = toks[0:2]
countries['inter'] = ['inter', 'inter']


curves_dict = {}
total_sums = {}

# List of country-codes to keep
seq_tags = ['49', '39', 'inter', '40', '48', '420', '44', '41', '34', '43', '373', '212', '380', '221', '86', '1', '91', '46']

for x in seq_tags:
    curves_dict[x] = {}
    total_sums[x] = [0.0]*4


for line in sys.stdin:
   l = line.strip() + "\t".join(["0"]*6)
   squareid, dt, country, smsin, smsout, callin, callout = l.split('	')[0:7]

   # Round to hour
   try:
       dt = datetime.fromtimestamp(int(dt)/1000).replace(minute=0)
   except:
       continue

   for x in seq_tags:
       if not curves_dict[x].get(dt):
           curves_dict[x][dt] = [0.0]*4 


   activity = [float_zero(smsin), float_zero(smsout), float_zero(callin), float_zero(callout)]

   if country in curves_dict:
       for i in range(4):
           curves_dict[country][dt][i] += activity[i]
           total_sums[country][i] += activity[i]

   if country != "0" and country != "39":
       for i in range(4):
           curves_dict['inter'][dt][i] += activity[i]
           total_sums['inter'][i] += activity[i]


print "dt,date,hour,weekday,type,smsin,smsout,callin,callout,smsin_r,smsout_r,callin_r,callout_r,smsin_m,smsout_m,callin_m,callout_m"
for country in curves_dict:
    total_max = [0.0000001]*4
    for e in curves_dict[country]:
        for x in range(4):
            total_max[x] = max(total_max[x], curves_dict[country][e][x])

    for e in curves_dict[country]:
        print ",".join(str(s) for s in [e, e.strftime("%Y-%m-%d,%H,%a"), countries[country][0].strip()] + [round(i, 5) for i in curves_dict[country][e]]
                    + [round(curves_dict[country][e][j]/max(total_sums[country][j], 0.0000001), 6) for j in range(4)]
                    + [round(curves_dict[country][e][j]/total_max[j], 6) for j in range(4)] )


