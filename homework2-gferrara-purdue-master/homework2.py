#!/usr/bin/python3
def histogram(data, n, l, h):
    hist = list()
    for i in data:
        if not (isinstance(i,float) or isinstance(i,int)):
            print('Error in format of data. Non-float element found.')
            return hist
    if not (isinstance(n, int) and (n > 0)):
        print('Variable "n" is not a positive integer.')
        return hist
    if not (h >= l):
        print('Upper bound is not greater than lower bound.')
        return hist

    hist = [0] * n
    w = (h - l) / n
    for i in data:
        if (i <= l) or (i >= h):
            continue
        test = int((i - l) // w)
        hist[int((i - l) // w)] += 1
    return hist

def addressbook(name_to_phone, name_to_address):
    address_to_all = dict()
    for name,address in name_to_address.items():
        number = name_to_phone[name]
        if not address in address_to_all.keys():
            address_to_all[address] = ([name], number)
        else:
            address_to_all[address][0].append(name)
            print(f'Warning: Multiple names found for {address}.  ', end="")
            print(f'Discarding the number for {name} and keeping {address_to_all[address][0][0]}.')
    return address_to_all


if __name__ == "__main__":
    data = [-2, -2.2, 0, 5.6, 8.3, 10.1, 30, 4.4, 1.9, -3.3, 9, 8]
    hist = histogram(data, 10, -5, 10)
    print('Test 1: ', end="")
    print(hist)

    name_to_phone = {'alice': 5678982231, 'bob': '111-234-5678', 'christine': 5556412237, 'daniel': '959-201-3198',
                     'edward': 5678982231}
    name_to_address = {'alice': '11 hillview ave', 'bob': '25 arbor way', 'christine': '11 hillview ave',
                       'daniel': '180 ways court', 'edward': '11 hillview ave'}
    address_to_all = addressbook(name_to_phone, name_to_address)
    print(address_to_all)
