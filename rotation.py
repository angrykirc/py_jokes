import string

def barrel(t, k):
    asc = string.ascii_lowercase + "-"
    asc2 = asc[k:] + asc[0:k]
    r = ""
    for c in t: r += asc2[asc.index(c)]
    return r

key = 9
print(barrel("testing", key))