def getPairs(text):
    app, char_list, target=text.split(' ')
    int_list = list(map(int,char_list.split(',')))
    black_list = []
    print('\n'+text)
    print('List: '+str(int_list))
    print('Target: '+target)
    for x in int_list:
        if x not in black_list:
            index = int_list.index(int(target)-x) if int(target)-x in int_list else -1
            if index > -1:
                print('+ '+ str(int_list[index]) +', '+str(x))
                black_list.append(x)
                black_list.append(int_list[index])
                
file = open('tests.txt')
lines = file.readlines()
for line in lines:
    getPairs(line)