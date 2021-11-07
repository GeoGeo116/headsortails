from random import randint

import time

result = randint(0,1)

print("Press A Key To Flip")
input()

print("Flipping...")
time.sleep(1)

if result == 0:
    print("\nHeads")
else:
    print("\nTails")

input()