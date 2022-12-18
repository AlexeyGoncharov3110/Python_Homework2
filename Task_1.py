number=input('Введите число : ')
sum=0
for i in number:
     if i != '.':
        sum+=int(i)
print(sum)