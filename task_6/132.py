def index(s): #ok 5
    if(len(s)!=6):
        return False
    ind = 1
    for i in s:
        if(ind % 2 == 1 and (i>='A' and i<='Z') == False):
            return False
        elif(ind % 2 == 0 and (i>='0' and i<='9') == False):
            return False
        ind += 1
    return True
province = {'A':'Newfoundland',
         'B':'Nova Scotia',
         'C':'Prince Edward Island',
         'E':'New Brunswick',
         'G':'Quebec',
         'H':'Quebec',
         'J':'Quebec',
         'K':'Ontario',
         'L':'Ontario',
         'M':'Ontario',
         'N':'Ontario',
         'P':'Ontario',
         'R':'Manitoba',
         'S':'Saskatchwan',
         'T':'Albertia',
         'V':'British Columbia',
         'X':'Nunavut',
         'X':'Northwest Territories',
         'Y':'Yukon'}
s = input()
if(index(s) == False):
    print("Wrong postal code")
else:
    if(s[1] == '0'): print("Rural", end=' ')
    else: print("Urban", end=' ')
    print("address in ", end='')
    print(province[s[0]])
 