#LZW decoder

#takes a codified message and its dictionary and decode it

code = input("Insert the codified message separeted by whitespace for each number: ").split() #lists the code with each number in an element
code = [int(value) for value in code] #converts the list elements as integers
letters = input("Insert the letters of the dictionary of radicals separeted by whitespace in the same order they appear in the dictionary: ").split() #lists only the letters of the dictionary
rad_dict = dict() #opens a dictionary for the dictionary of radicals
for letter in range(len(letters)): #iterates with the letters and for each letters, input a number in order, starting by 1
    rad_dict.update({letters[letter]:letter+1})

#if you want to add the code and the dictionary by hardcoding this script instead of input, just uncomment the
#code block below and comment the code block above

'''code = [1, 2, 4, 3, 5, 8, 1, 10, 11] #need to be integers and separeted by comma, each number is an element
rad_dict = {"A":1, "B":2, "C":3} #the key letter must be a string, the value code must be an integer, insert only the radical letters, not the entire dictionary
'''

def lzw_decoder(code, dictionary):
#Decodification of a LZW code, getting only the code and its dictionary of radicals, writing a file with the message and returning the message
    message, values, cw = list(), list(dictionary.values()), code[0] #opens a list to append the letters of the message, opens a list with the values of the dictionary of radicals to be used as a counter and start the LZW algorithm with cw definition
    message.append([key for key in dictionary.items() if key[1] == cw][0][0]) #appends the cw letter to the message using a dictionary comprehension with a conditioner to get the key of its value
    for i in range(1, len(code)): #now the LZW algorithm looping starts, won't comment it, only some specifications of this script
        pw, cw = cw, code[i]
        if cw in values:
            message.append([key for key in dictionary.items() if key[1] == cw][0][0])
            p = [key for key in dictionary.items() if key[1] == pw][0][0]
            c = [key for key in dictionary.items() if key[1] == cw][0][0][0] #gets only the first character of the cw string
            dictionary.update({p+c:len(dictionary)+1})
            values.append(len(values)+1) #appends the value to be used as a counter
        else:
            p = [key for key in dictionary.items() if key[1] == pw][0][0]
            c = [key for key in dictionary.items() if key[1] == pw][0][0][0] #gets only the first character of the cw string
            dictionary.update({p+c:len(dictionary)+1})
            values.append(len(values)+1) #appends the value to be used as a counter
            message.append(p+c)
    with open(f'{"".join(str(value) for value in (code))}_decompressed.txt', 'w') as file: #writes a file with the message
        file.write(f'Message: {"".join(message)}\nDictionary: {dictionary}')
    return ''.join(message) #returns the message as a string

lzw_decoder(code, rad_dict)