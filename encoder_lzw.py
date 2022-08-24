#LZW encoder

#takes a message, create a dictionary and encode the message

message = str(input("Insert the message to be codified: ")) #asks the message to be codified

#if you want to insert the message by hard coding instead of by input, just comment the statement above and 
#uncomment the statement below

#message = '' #must be a string

def radicals(message):
#The dictionary of coded radicals of the message
    message, radicals, counter = list(message), dict(), list() #lists the message as every character as a list element, opens a dictionary for radicals and opens a list fo each radical
    for char in message: #creates a list for each radical of the message
        if not char in counter:
            counter.append(char)
    for char in range(len(counter)): #creates a dictionary with the code for each radical, from the first symbol in the messate to the last one
        radicals.update({counter[char]:char+1})
    return radicals #returns the dictionary of radicals

def lzw_encoder(message):
#The message codified by LZW algorithm, the dictionary of radicals and its entire dictionary and creates a file with the code and the dictionary of radicals
    dictionary, letters, p, code = radicals(message), list(message), '', list() #gets the dictionary of radicals, lists the message as every character as a list item, defines p as empty value and opens a list to codify the message 
    for letter in range(len(letters)): #The LZW algorithim (I won't describe it, search for that)
        c = letters[letter]
        pc = p + c
        if pc in dictionary:
            p = pc
        else:
            code.append(dictionary.get(p))
            dictionary.update({pc:len(dictionary)+1})
            p = c
    code.append(dictionary.get(p))
    with open(f'{message}_compressed.txt', 'w') as file: #writes a file with the dictionary of radicals and the code
        file.write(f'Dictionary of radicals: {radicals(message)}\nComplete Dictionary: {dictionary}\nCode: {" ".join(str(value) for value in code)}')
    return ' '.join(str(value) for value in code), radicals(message), dictionary #returns a tuple with the codified message separeted by whitespace, the dictionary of radicals and the entire dictionary

lzw_encoder(message)