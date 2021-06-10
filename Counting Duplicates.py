def duplicate_count(text):
    dupl = 0
    text = text.lower()
    for char in text:
        i = 0
        if ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
            while i != len(text):
                if ord(char) == ord(text[i+1]):
                    i +=1
                    dupl +=1
                    break
                else:
                    i +=1
        else:pass
    return f' Количество дупликатов равно : {dupl}'


print(duplicate_count("abrakaDabra"))