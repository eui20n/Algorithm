num = []
while len(num) != 9:
    a = int(input())
    num.append(a)
    
print(max(num))
print(num.index(max(num))+1)