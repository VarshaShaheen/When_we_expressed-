def poocha_function(read):
    txt = [112, 111, 111, 99, 104, 97]
    ot = [107, 110, 117, 100, 116, 49]
    out = ""

    for i, c in enumerate(read):
        out += chr(ord(c) // txt[i] + ot[i])

    return out


print(poocha_function(input("Who are you ? : ")))
