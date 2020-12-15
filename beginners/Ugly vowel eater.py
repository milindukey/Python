#Your task here is very special: you must design a vowel eater! Write a program that uses:

#a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement.

#Your program must:
#ask the user to enter a word;
#use userWord = userWord.upper() to convert the word entered by the user to upper case;
#we'll talk about the so-called string methods and the upper() method very soon - don't worry;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen, each one of them on a separate line.

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A" :
        continue
    elif letter == "E" :
        continue
    elif letter == "I" :
        continue
    elif letter == "O" :
        continue
    elif letter == "U" :
        continue
    else:
        print(letter)




#Your program must:

#ask the user to enter a word;
#use userWord = userWord.upper() to convert the word entered by the user to upper case;
#we'll talk about the so-called string methods and the upper() method very soon - don't worry;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#assign the uneaten letters to the wordWithoutVovels variable and print the variable to the screen.
#Look at the code in the editor. We've created wordWithoutVovels and assigned an empty string to it.
#Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the wordWithoutVovels variable.

wordWithoutVovels = ""

userWord = input("Enter Your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A" :
        continue
    elif letter == "E" :
        continue
    elif letter == "I" :
        continue
    elif letter == "O" :
        continue
    elif letter == "U" :
        continue
    else:
        wordWithoutVovels += letter
        
print(wordWithoutVovels)
    
