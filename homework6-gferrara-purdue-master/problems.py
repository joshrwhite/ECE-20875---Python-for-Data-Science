import re

#Match phone numbers. Return True or False. See README for details.
def problem1(searchstring) :
    #fill in
    p = re.compile(r'((^((\(\d{3}\)\s)|(\d{3}\-)))\d{3}\-\d{4}$)|(^(\d{3})\-(\d{4})$)')
    if p.search(searchstring): return True
    else: return False

#Extract street name from address. See README for details.
def problem2(searchstring) :
    #fill in
    p = re.compile(r'((\d)+\s)(([A-Z][a-z]*\s)+)((Rd.)|(Dr.)|(Ave.)|(St.))')
    a = p.search(searchstring)
    s = a.group(3)
    s = s[0:-1]
    return s


#Garble street name. See README for details
def problem3(searchstring) :
    p = re.compile(r'((\d)+\s)(([A-Z][a-z]*\s)+)((Rd.)|(Dr.)|(Ave.)|(St.))')
    a = p.search(searchstring)
    s = a.group(3)
    s_rev = s[-2::-1]
    su = p.sub(f'{a.group(1)}{s_rev} {a.group(5)}', searchstring)
    return su

if __name__ == '__main__' :
    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True    
    print(problem1('494-4600')) #True
    
    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First
    
    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))