T = int(input())
word = []
for x in range(T):
    a = input()
    word.append(a)

new_word = []
for x in word:
    if x not in new_word:
        new_word.append(x)
        
new_word.sort(key = lambda x:(len(x),x))
for x in new_word:
    print(x)
    
