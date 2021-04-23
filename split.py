array = ['Ini adalah tes kalimat']

def split(sentence):
    sentence = ''.join(array)
    split_list = []
    tmp = ''
    for s in sentence:
        if s == ' ':
            split_list.append(tmp)
            tmp = ''
        else:
            tmp += s
    if tmp:
        split_list.append(tmp)
    return split_list

print(split(array))