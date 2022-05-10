a = input()
a = a.upper()
count_word = []
word_count = []
max_word = []

for x in range(len(a)):
    if a[x] not in count_word:
        count_word.append(a[x])
    word_count.append(a[x])

for x in count_word:
    max_word.append(word_count.count(x))
    
if max_word.count(max(max_word)) != 1:
    print('?')
else:
    print(count_word[max_word.index(max(max_word))])
