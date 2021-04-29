word = input()
letters = []

for chartacter in word:
    if chartacter in letters:
        print('yes')
        exit()

    letters.append(chartacter)

print('no')
