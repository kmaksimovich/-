my_dict = {'гена': 1999}
print(my_dict)
my_dict["гена"] = 2000
my_dict['кещ'] = 2003
print(my_dict)
my_dict.update({'слизар' : 1997, 'шерк' : 1999, 'вова' : 1999})
print(my_dict)
del my_dict ['слизар']
print(my_dict)

my_set = {'tron', 7, 'yula', 8}
my_set.update({'home' , 1})
print(my_set)
print(my_set.discard(7))
print(my_set)
