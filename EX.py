# Ex1 - String 
# Enter text and display it one by one
# text="Hello"
# for char in text:
#     print(char)
# Ex2 - String
# Enter text and display number of letter
# text="Hello"
# for i in range(len(text)):
#     print(i)

# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter
#1way
# text=input("Enter your text: ")
# result="No"
# for i in range (len(text)):
#     if text[i].upper()==text[i]:
#         result="Yes"
# print(result)
#2way
# text = input("Enter text: ")
# contains_capital = False
# for char in text:
#     if char.isupper():
#         contains_capital = True
# if contains_capital:
#     print("Yes")
# else:
#     print("No")
# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)
#1way
# text = input("Enter Text : ")
# output = 0
# letter = ""
# for i in range(len(text)):
#     if text[i] == " ":
#         letter += ""
#     else:
#         letter += text[i]
#         output += int(text[i])
# print(letter)
# print("Total :",output)
#2way
# text = "3 4 5 6"
# total = 0
# for char in text.replace(" ", ""):
#     print(char)
#     total += int(char)
# print(total)
#3way
# text = "3 4 5 6"
# new_text = ""
# sum = 0 
# for char in text:
#     if char != ' ':
#         new_text += char
#         sum += int(char)
# print(new_text)
# print(sum)
# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 
#1way
# number = input("Enter your number : ")
# result = 0
# num_even = 0
# num_odd = 0
# result_all=0
# lastindex = len(number) - 1
# num_recvers = ""
# for i in range(len(number)):
#     num_recvers += number[lastindex -i]
#     result_all=int(number[i])
#     if i % 2 == 0:
#         num_even += 1
#         result += int(number[i])
#     else:
#         num_odd += 1
# print("letter even:", num_even)
# print("letter odd", num_odd)
# print("Total :",result)
# print("Letter revers", num_recvers)
#2way
# text = "454639"
# count_odd = 0
# count_even = 0
# for i in range(len(text)):
#     total = int(text[i])
#     if total % 2 == 0:
#         count_odd += 1
#     if total % 2 == 1:
#         count_even += 1
# print("Count of even :", count_even)
# print("Count of odd :", count_odd)
# print("sum all number:",count_even+count_odd)
# print("Reverse",text[::-1])

# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"
# number=int(input("enter your num: "))
# if number%2==1:
#     print("Odd")
# else:
#     print("Even")
# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
# isfound_num=False
# while not isfound_num:
#     num=int(input("enter your num: "))
#     if num >=10 and num <=20:
#         print("Continue")
#     else:
#         isfound_num=True
# print("Out of range")
# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
# text = "9394884039"
# number_eight = 0
# first_index_of_eight = 0
# isfound = False
# for i in range(len(text)):
#     if text[i] == "8":
#         number_eight += 1
#         if text[i] == "8" and not isfound:
#             first_index_of_eight = i
#         isfound = True
# print(number_eight)
# print(first_index_of_eight)
# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
# text = "3 4 5 6"
# no_space = ""
# total_x_two = 0
# for i in range(len(text)):
#     if text[i] != " ":
#         no_space += text[i]
#         total_x_two += int(text[i]) * 2
#         print(total_x_two)
#     else:
#         no_space += ""
# print(no_space)
# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
# big_number = 0
# small_number = 0
# for i in range(5):
#     number = int(input("Enter number : "))
#     if big_number == 0 and small_number == 0:
#         big_number = number
#         small_number = number
#     else:
#         if number > big_number:
#             big_number = number
#         if number < small_number:
#             small_number = number
# print("Big number : ", big_number)
# print("Small number : ", small_number)