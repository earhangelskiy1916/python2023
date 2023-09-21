poem = input('введите стихотворение ')
volwes = ['а', 'о', 'и', 'е', 'ё', 'ы', 'у', 'э', 'ю', 'я']
parts = poem.split()
result = list()
for item in parts:
    q = 0
    for letter in item:
        if letter in volwes:
            q += 1
    result.append(q)
if len(set(result)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')