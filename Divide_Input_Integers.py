#Write a program that reads integers user_num and div_num as input, 
#and outputs user_num divided by div_num three times using floor divisions

user_num = int(input())
div_num = int(input())

quotient1 = user_num // div_num
quotient2 = quotient1 // div_num
quotient3 = quotient2 // div_num

print(f'{user_num}, {quotient1}, {quotient2}, {quotient3}')