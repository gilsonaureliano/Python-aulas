from time import sleep
import emoji

print('{:+^40}'.format('CONTAGEM REGRESSIVA'))
for c in range(10, -1, -1):
    sleep(1)
    print(c)

print(emoji.emojize('FIM :couple_with_heart:', use_aliases=True))
