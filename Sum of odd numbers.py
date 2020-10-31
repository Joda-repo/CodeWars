def find_missing_letter(chars):
    i = -1
    for chars[i] in chars:
        i += 1
        if (ord(chars[i])+1) == ord(chars[i+1])
            pass
        else: found = chr(ord(chars[i])+1)
    return found

find_missing_letter(["a","b","c","d","f"])