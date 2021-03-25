import random

ePool = 500

a = random.randint(0, ePool)
ePool -= a
b = random.randint(0, ePool)
c = ePool -b

print ("a = {}  b = {}  c = {}".format(a, b, c)) 

