def string_a():
    string = str(input('Type a sentence: ')).upper()
    if string[-1] == 'A' and string[0] == 'B':
        print('The sentence ends with the letter A and starts with letter B')
    else:
        print('The sentence does not end with the letter A and does not start with the letter B')
    print(string)

string_a()
