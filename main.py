abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '?', '!', '.', ',', ';', ':', '+', '-', '/', '=', ' ']
morse = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___',
         '.__.',
         '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '.____', '..___', '...__', '...._',
         '.....', '_....', '__...', '___..', '____.', '_____', '..__..', '_._.__', '._._._', '__..__', '_._._.',
         '____...', '._._.', '_...._', '_.._.', '_..._', '.......']

print("Welcome to the Morse Code Converter")
go_on = True
while go_on:
    answer = input(
        "If you want to convert phrase to the Morse Code, type 1 or type 2 if you want decode your Morse Code: ")

    output = ''
    if answer == '1':
        input_characters = input("Input your phrase: ").lower()

        for item in input_characters:
            if item not in abc:
                print(f"You've entered wrong character: {item}")
                output += item + " "
            else:
                index = abc.index(item)
                output += morse[index] + " "
    else:
        input_characters = input("Input your Morse Code with spaces between letters, numbers or symbols: ")
        character = ''
        morse_list = []
        for item in input_characters:
            if item != ' ':
                character += item
            elif item == ' ':
                morse_list.append(character)
                character = ''
        morse_list.append(character)
        for item in morse_list:
            if item not in morse:
                print(f"You've entered wrong character: {item}")
            else:
                index = morse.index(item)
                output += abc[index]

    print(f"Your input: {input_characters}")

    print(f'Here is your output: {output}')
    shell_continue = input('Type Y if you want convert something else or N for exit. ')
    if shell_continue != 'Y':
        go_on = False
