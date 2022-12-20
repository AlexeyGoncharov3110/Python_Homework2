size=int(input('Введите размер списка :'))
my_list=[]
from random import randint
for i in range(size):
   i=randint(0,10)
   my_list.append(i)
print(my_list)
for i in range(len(my_list)):
   m=randint(0,len(my_list)-1)
   temp=my_list[i]
   my_list[i]=my_list[m]
   my_list[m]=temp 
print(my_list)
