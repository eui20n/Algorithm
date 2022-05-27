a,b = input().split()
a_list = []
b_list = []
for x in range(len(a)):
    a_list.append(a[x])
    b_list.append(b[x])

list_a = []
list_b = []
for _ in range(3):
    list_a.append(a_list.pop())
    list_b.append(b_list.pop())
    
    

a = ''.join(list_a)
b = ''.join(list_b)

if int(a) > int(b):
    print(a)
else:
    print(b)


