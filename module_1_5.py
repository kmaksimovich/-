immutable_var = ([1, 2], 'a', 'b') # кортеж не поддерживает обращение по элементам
print(immutable_var)
immutable_var[0][0] = 7
immutable_var[0][1] = 9
print(immutable_var)
immutable_tupe = (1 , 2, [3], 'a' , ['b'])
print(immutable_tupe)
immutable_tupe[2][0] = 'b'
immutable_tupe [4][0] = 0
print(immutable_tupe)
