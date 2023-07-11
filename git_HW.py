def palyndrom(data):
    fail = 0
    atad = [i for i in data]
    for syn in atad:
        if atad[1] != atad[-1]:
            fail +=1
    if(fail > 0):
        print(False)
    else:
        print(True)

palyndrom("aabbaa")