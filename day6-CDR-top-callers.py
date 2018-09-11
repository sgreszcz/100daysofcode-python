#!python3

from collections import defaultdict, namedtuple, Counter
import csv
import os

# Directory Path of Cisco UCM (Unified Communication Manager) CDR (Call Data Record) files
path_to_cdr = './cdr/'

# Named Tuple to describe caller data
Caller = namedtuple('Caller', 'callId timeUTC origIPAddr destIpAddr originalCalledPartyNumber')

# Initialise Dictionary / List
caller_dictionary = defaultdict(list)

# Function to Parse the CDR (in CSV file)
def get_calls_by_callid(cdr, caller_dict):
    """Extracts values from csv and stores them in a dictionary
       where keys are callid, and values is a list of call data (named tuples)"""

    with open(cdr, encoding = "utf-8") as f:
        for line in csv.DictReader(f):
            # Only look at records (csv lines) with completed call data
            if line['cdrRecordType'] == '1':
                try:
                    callingPartyNumber = line['callingPartyNumber']
                    callID = line['globalCallID_callId']
                    time = int(line['dateTimeOrigination'])
                    origIPAddr = line['origIpAddr']
                    destIpAddr = line['destIpAddr']
                    originalCalledPartyNumber = line['originalCalledPartyNumber']
                except ValueError:
                    continue

                c = Caller(callId=callID, timeUTC=time, origIPAddr=origIPAddr, destIpAddr=destIpAddr, originalCalledPartyNumber=originalCalledPartyNumber)
                caller_dict[callingPartyNumber].append(c)

    return caller_dict

for filename in os.listdir(path_to_cdr):
    caller_dictionary = get_calls_by_callid(path_to_cdr+filename, caller_dictionary)

# Find top 5 callers by number of calls placed
counting = Counter()
for caller, call_info in caller_dictionary.items():
    counting[caller] += len(call_info)

print (counting.most_common(5))





