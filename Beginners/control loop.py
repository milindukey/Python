largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

    

#Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word,
#in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

#Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

while True :
    word = input("You're stuck in an infinite loop. Enter secret word to exit the loop ")
    if word == "chupacabra" :
        break
print("You've successfully left the loop.")
