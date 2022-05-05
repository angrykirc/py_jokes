# "obfuscated" string generator
import string
import random

print("enter text")
text = input()
print("enter start pos")
n_start = int(input())
print("enter step")
n_step = int(input())
n_step = n_step if n_step >= 1 else 1

result = ""
c = 0
lt = len(text)

for i in range(0, n_start + (lt * n_step)):
    if (i - n_start) % n_step == 0 and i >= n_start and c < lt:
        result += text[c]
        c += 1
    else:
        result += random.choice(string.ascii_lowercase)
    
    pass
    
print(result)
