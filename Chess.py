size = 8
for row in range(size):
    for col in range(size):
        if(row + col )% 2 == 0:
            print('\u25A0',end=' ')
        else :
            print('B',end = ' ')
    print()