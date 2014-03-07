#!/usr/bin/env python2.7
 
import sys
 
from collections import Counter

# Dict of country-counters
cnt = {}
total_cnt = [0.0, 0.0, 0.0, 0.0]

def float_zero(str):   # Floatify string, 0 if error
    try:
        return float(str)
    except:
        return 0.0

# Read countrycodes and load into hashtable
countries = {}
f = open('../countrycodes.csv')
for line in f:
    toks = line.split(',')
    countries[toks[3].strip()] = [s.strip() for s in toks[0:2]]


# Reading from standard input (layout from Telecommunication Telecom Italy)
for line in sys.stdin:
   l = line.strip() + "\t".join(["0"]*6)
   squareid, dt, country, smsin, smsout, callin, callout = l.split('	')[0:7]

   # Check country in countries-counter, if not, initialize
   country = country.strip()
   if not cnt.get(country):
       cnt[country] = [0.0, 0.0, 0.0, 0.0]

   # Increase country counters
   cnt[country][0] += round(float_zero(smsin),5)
   cnt[country][1] += round(float_zero(smsout),5)
   cnt[country][2] += round(float_zero(callin),5)
   cnt[country][3] += round(float_zero(callout),5)

   # Increase global counters 
   total_cnt[0] += round(float_zero(smsin),5)
   total_cnt[1] += round(float_zero(smsout),5)
   total_cnt[2] += round(float_zero(callin),5)
   total_cnt[3] += round(float_zero(callout),5)

# Heading
print "country,iso2,countrycode,smsin,smsout,callin,callout,rat_smsin,rat_smsout,rat_callin,rat_callout,allcomms,in_to_all,sms_to_all,flag,importance" 
for i in sorted(cnt):
   if countries.get(i):
       importance = sum(cnt[i])/sum(total_cnt)  # ratio of activity for country

       if importance > 0.005:
           flag = "XLARGE"
       elif importance > 0.0005:
           flag = "LARGE"
       elif importance > 0.0001:
           flag = "MEDIUM"
       else:
           flag = "SMALL"

       print ",".join(str(s) for s in countries[i] + [i,] + cnt[i] + [round(cnt[i][j]/total_cnt[j], 4) for j in range(4)] 
                                      + [round(sum(cnt[i]),2), round((cnt[i][0] + cnt[i][2])/ sum(cnt[i]), 4), round((cnt[i][0] + cnt[i][1])/ sum(cnt[i]), 4), 
                                         flag, round(importance, 6)])

# Dump a quick summary
print "Summary: " + ",".join(str(round(s, 2)) for s in total_cnt + [sum(total_cnt), (total_cnt[0]+total_cnt[2])/sum(total_cnt), (total_cnt[0]+total_cnt[1])/sum(total_cnt)])
