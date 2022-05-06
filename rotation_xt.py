# Available key space is [0, 0xFFF]
# this is because we are using 6 bits for each key part (32 characters in alphabet, 2^6)
# making a grand total of 12 bits, or 2^12 possible key values
def r(t, key, reverse=False):
    p1, p2 = (key & 63, (key & 4032) >> 6)
    if reverse:
        p1, p2 = (-p1, -p2)
    
    asc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + "abcdefghijklmnopqrstuvwxyz" + ".,_?!"
    r = ""
    for i in range(len(t)):
        if i % 2 == 0:
            r += (asc[p1:] + asc[0:p1])[asc.index(t[i])]
        else:
            r += (asc[p2:] + asc[0:p2])[asc.index(t[i])]
    return r

text = "test_абырвалг"
text = r(text, 32)
print(text)
text = r(text, 32, True)
print(text)
