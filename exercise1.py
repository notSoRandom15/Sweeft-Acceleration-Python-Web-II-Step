n = int(input('input anything'))
words = []
count = {}
for i in range(n):
    word = input().strip()
    words.append(word)
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(len(set(words)))
for word in words:
    if count[word] >0:
        print(count[word], end='')
        count[word] = 0

print()