#import platform

'''print(platform.system())
print(platform.release())
print(platform.processor())

import math

print(math.gcd(8,24))
print(math.log(8))
print(math.cos(0))
print(math.tan(45))
print(math.)'''

import random

print(random.random())
print(random.randint(1, 12))
print(random.uniform(1, 13))


names = ['varun', 'chaitu', 'rasool', 'tarit', 'sriram']
print(random.choice(names))
print(random.choices(names, k=2))
random.shuffle(names)
print(names)