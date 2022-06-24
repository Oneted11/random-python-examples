# part2.py

# Questionumber2


# def runningAverage(user_input, num, avg):

#     user_input = input("input a number :  ")
#     while user_input:
#         avg = user_input+(avg*num)/num
#         num = num+1
#         print("the average is : ", avg)
#         runningAverage(user_input, num, avg)


# runningAverage(0, 1, 0)

# runningAverage()
# Question 4

# def playGame():
#     play_again = input("Would you like to play odds or evens?")
#     while play_again:
#         # Your code here
#         ...
#         play_again = input("Would you like to play again?")


# def oddsOrEvens():
#     # Implement a single game following the pseudocode from class
# 3
# def income_tax(tax, income):
#     tax = (income*tax)/100
#     print(tax)


# def tax_bracket():
#     income = int(input("Please enter your income: "))
#     if income > 9950:
#         income_tax(10, income)
#     if income > 40525:
#         income_tax(12, income)
#     if income > 86375:
#         income_tax(22, income)
#     if income > 164925:
#         income_tax(24, income)
#     if income > 209425:
#         income_tax(32, income)
#     if income > 523600:
#         income_tax(35, income)
#     if income > 523601:
#         income_tax(37, income)


# tax_bracket()

# gcd() function to calculate gcd for the given two numbers
# def gcd(a, b):

#     while b:
#         a, b = b, a % b
#         return a

#     while True:

#         # getting input for the first number
#         number1 = int(input('\nEnter a number '))

#         # checking for validity of the number,must be greater than zero
#         if number1 == 0 or number1 < 0:
#             print('Enter a valid number greater than zero')
#             continue
#         else:
#             break

#         while True:

#             # getting input for the second number
#             number2 = int(input('Enter another number '))

#         # checking for validity of the number, must be greater than zero
#             if number2 == 0 or number2 < 0:
#                 print('Enter a number greater than zero')
#                 continue
#             else:
#                 break

#         # checking for first number must be greater than the second number

#         if number1 < number2:
#             print('First number should be greater than second number')
#         continue

#         # calling the gcd function with input arguments
#         r = gcd(number1, number2)

#         # displaying the result
#         print('gcd(%d,%d) is %d \n' % (number1, number2, r))

#         # getting input from the uesr to continue to process or not

#         while True:

#             choice = input('Do you want to continue? (Yes/Y or No/N) ')

#         if choice.lower() == 'yes' or choice.lower() == 'y':
#             break
#         elif choice.lower() == 'no' or choice.lower() == 'n':
#             break
#         else:
#             print('Enter an valid character Yes,Y,No,N')
#             continue

#         if choice.lower() == 'yes' or choice.lower() == 'y':
#             continue
#         elif choice.lower() == 'no' or choice.lower() == 'n':
#             break


# gcd(3, 5)


# Destruct the words into cahracters
# Create set of cahracters from both //makes unique
# Add them to an object ie
# -object[key=char]:number of occurrences

# Count objects keys with values higher than 1
# AVG=count/length of longest word

def main():
    word1 = input("type first word : ")
    word2 = input("type second word : ")

    arr1 = list(word1)
    arr2 = list(word2)

    dict = {}
    set1 = set(arr1)
    set2 = set(arr2)
    addtodict(set1)
    print(dict)
    addtodict(set2)
    print(dict)


def addtodict(arr):
    if len(arr) < 1:
        return
    dict[arr.pop()]: 1 if dict[arr.pop()] else dict[arr.pop()]+1
    print(dict)
    addtodict(arr)


main()
