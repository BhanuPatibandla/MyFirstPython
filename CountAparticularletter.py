def count():
    word=raw_input()
    x=0
    for letter in word:
        if letter=='a':
            x=x+1
    return x
print(count())


