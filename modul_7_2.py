def custom_write(file_name, strings):
    rezult = {}
    file = open(file_name, 'a', encoding='UTF-8')
    for i in range(len(strings)):
        key = (i + 1, file.tell())
        rezult[key] = strings[i]
        file.write(strings[i] + '\n')
    file.close()
    return rezult

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
