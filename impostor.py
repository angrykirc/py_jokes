who = "impostor"
c = "qce("
l = int(len(who) / 2)
who += " is "

for i in range(l):
    a = who[i * 2]
    b = who[i * 2 + 1]
    pa = ord(c[i])
    pb = ord(a) + ord(b)
    who += chr(int(pb * pa / 200) + 1)
    
print(who)