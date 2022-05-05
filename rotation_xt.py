def r(t, k):
    p1, p2 = (key & 63, (key & 4032) >> 6)
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
print(r(text, 32))
