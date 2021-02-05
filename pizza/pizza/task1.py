customers = ['brad','jolie','johny','sooronbai','sooronbai','sadyr','sadyr','emma','sooronbai',
         'brad','almazbek','roza','roza','kurmanbek','toby','tony','robert','askar','robert','chris','chris']



dict1 = {}

for i in customers:
    dict1[i] = customers.count(i)
print(dict1)


import random

r = random.sample(range(1,100000),60000)

if r.index(max(r)) > r.index(min(r)):
    print(r.index(max(r)) - (r.index(min(r))))
else:
    print((r.index(min(r))) - (r.index(max(r))))


vip_clients = []
potential_vip = ''
for customer in customers:
    if customer == potential_vip:
        vip_clients.append(customer)
    potential_vip = customer
print(vip_clients)