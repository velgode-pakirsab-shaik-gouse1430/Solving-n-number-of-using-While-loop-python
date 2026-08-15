# Solving-n-number-of-using-While-loop-python
# i=0
# while i<5:
#     print('vcube')
#     i+=1

#from 0 t0 10
# i=0
# while i<=10:
#     print(i)
#     i+=1

#from 10 to 1
# i=10
# while i>=0:
#     print(i)
#     i-=1

#1 to 10 even numbers
# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i=i+2

#to print sum of natural numbers from upto 10
# n=int(input("enter n value"))
# i=1
# count=0#1
# while i<=n:
#     count=count+i
#     i+=1
# print(count)
# n=int(input("enter n value"))
# i=1
 
# while i<=n:
#     s=0
#     s=i
#     i+=1
# print(s)


# i=2
# while i<=100:
#     print(i)
#     i=i**2

# i=0
# while i<=3 or i%2==0:
#     print(i,end=" ")#0 1 2 3 4 
#     i=i+1

# i=0
# while i<=3 or i%2==0:
#     print(i,end=" ")#0  
#     i=i+2

# i=1500
# while i<=2026:
#     if (i%4==0 or i%400==0) and i%100!=0:
#         print(i,end=" ")
#     i=i+1

# i=1
# while i<=10:
#     if i%2==0:
#         i=i+1
#     else:
#         i=i+3
#     print(i)

# print(10 or 9)
# print(0 or 9)

#to print number is a prime or not6
# num=int(input("enter a number"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#      print('prime')
# else:
#     print("not prime")

#Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.
# i=0
# while i <=10:
#     print(i)
#     i+=1
 
#Create a program that asks the user to enter a number, 
# and then use a while loop to count down from that number to 1, printing each value.

# num=int(input("enter the number:"))
# while num>0:
#     print(num)
#     num-=1

# #Write a while loop that calculates the sum of even numbers from 1 to 100.
# i=0
# while i<=100:
     
#     print(i)
#     i+=2

#Use a while loop to calculate the factorial of a given number.
# num=int(input("Enter the number"))
# i=1
# factorial=1
# while i<=num:
#     factorial=factorial*i
#     i+=1
# print(factorial)

#Write a while loop that prints all even numbers between 1 and 50.
# num=int(input('enter the number'))
# i=1
# while i<=num:
#     if i%2==0:
#         print(i)
#     i=i+1

#Create a program that calculates the sum of the digits of a given integer using a while loop.
# num=int(input("enter the number"))
# remainder=0
# while num>0:
#     remainder=remainder+num%10
#     num=num//10
# print(remainder)

#Generate a multiplication table for a given number using a while loop.
# num=int(input("enter the number"))
# i=0
# while i<=10:
#     print(f"{num} * {i} = {num*i}")
#     i+=1

#Write a program to find all the factors of a given number using a while loop
# num=int(input("enter the number"))
# i=1
# while i<=num:
#     if num%i==0:
#         print(i)
#     i+=1

#Implement a program to reverse a given number using a while loop.
# num=int(input("enter the number"))
# rev=0
# while num>0:
#     remainder=num%10
#     rev=(rev*10)+remainder
  
#     num=num//10
# print(rev)

#Create a program that prompts the user to enter a password.
#  Keep asking until they enter the correct password
# password1=""
# password="123456"
# while password1 != password:
#     password1=input("enter your password")
#     if password==password1:
#         print("access granted")
#     else:
#         print("Try again")


# num=int(input("enter the number"))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime")

# Input number
# num = int(input("Enter an integer: "))

# if num == 0:
#     print("zero")
# else:
#     # Lists for word mapping
#     units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#     result = ""
    
#     # Using a while loop to process the number (handling up to hundreds for this example)
#     while num > 0:
#         if num >= 100:
#             hundreds_digit = num // 100
#             result += units[hundreds_digit] + " hundred "
#             num %= 100
#             if num > 0:
#                 result += "and " # Optional "and" for British English style
#         elif num >= 20:
#             tens_digit = num // 10
#             result += tens[tens_digit]
#             num %= 10
#             if num > 0:
#                 result += "-" + units[num]
#             num = 0 # Break loop
            
#         elif num >= 10:
#             result += teens[num - 10]
#             num = 0 # Break loop
            
#         else:
#             result += units[num]
#             num = 0 # Break loop

#     print(result.strip())

#Write a program to reverse a given string using a while loop.
# s1="Hello"
# s2=""
# index=len(s1)-1
# while index>=0:
#     s2+=s1[index]
#     index-=1
# print(s2)

# s="gouse"
# i=0
# res=""
# while i<len(s):
#      
#     res=s+res
#     i+=1
# print(res)


#Write a program that prints all prime numbers between 1 and 100 using a while loop
# i=1
# while i<=100:
#     cnt=0
#     d=1
#     while d<=i:
#         if i%d==0:
#             cnt+=1
#             d=d+1
#             if cnt==2:
#                 print(i)
#         i=i+1


# m = int(input("Enter first positive number"))
# n = int(input("Enter second positive number"))
# if m == 0 and n == 0:
#     print("Invalid Input")
# if m == 0:
#     print(f"GCD is {n}")
# if n == 0:
#         print(f"GCD is {m}")
# while m != n:

#         if m > n:

#             m = m - n

#         if n > m:

#             n = n - m

# print(f"GCD of two numbers is {m}")

# num=123456
# sum=0
# while num!=0:
#     remainder=num%10
#     sum=sum+remainder
#     num=num//10
# print(sum)

# print(120//2)

# string_tisko=input("enter the string you want")
# targeted_word=input("enter the targeted word")
# i=0
# while True:
#     if string_tisko[i]==targeted_word:
#         print(i)
#         break
#     i+=1

# n=int(input("enter the number"))
# i=0
# while i<n:
#     square=i**2
#     print(square)
#     i+=1



# #password validator
# pswd=input('enter the password=')
# i=0
# up,lc,spe,spa,digit=0,0,0,0,0
# while i<len(pswd):
#     char=pswd[i]
#     if char.isupper():
#         up+=1
#     elif char.islower():
#         lc+=1
#     elif char.isspace():
#         spa+=1
#     elif char.isdigit():
#         digit+=1
#     else:
#         spe+=1
#     i+=1
# #print(up,lc,spe,spa,digit)
# if len(pswd)>=8:
#     if len(pswd)<=16:
#         if up>=1:
#             if lc>=1:
#                 if spe>=1:
#                     if spa==0:
#                         if digit>=1:
#                             print('password is valid')
#                         else:
#                             print('there should be one digit atleast')
#                     else:
#                         print('there will be no space in the password')
#                 else:
#                     print("password must have one special characeter")
#             else:
#                 print('password must have one lowercase')
#         else:
#             print('password must have one uppercase')
#     else:
#         print('password must be less than or equal to 16')
# else:
#     print('password must be eight or greater than 8 characters')

# n=int(input("enter the number:"))
# while n>0:
#     k=n//2
#     if k ==1:
#         print("square")
#         break
#     else:
#         k=k//2
# print('not square')
 

# n=int(input("enter the n value"))
# while n>0:
#     if n/2!=1:
#         n=n//2
#         print('not square of 2')
#         break
         
#     else:
#         print("square of 2")


        
# n=int(input('enter the number'))

# count=0
# while n>0:
    
#     count=count+1
#     n=n//10
# print(count)

# n=int(input("enter the number:"))
# number_of=0
# i=1
# while n<=100:
#     count=0 # to count no of divisor
#     d=1 #itreation to divide the given value
#     while d<=i:
#         if i%d==0:
#             count+=1
#         d+=1
    
    
    
# if count==2:
#     number_of=number_of+1
#     i=i+1
# print("number_of")
     
# s=input("enter the string")
# res=""
# i=0
# while i<len(s):
#     char=s[i]
#     res=s[i]+res
#     i=i+1
# print(res)


# s="Python is a best language"
# i=0
# while i<len(s):
#     if s[i].isspace():
#         print(s[i])
#     i=i+1


#Prime number
# n=int(input("enter the number:"))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("it is prime number:")
# else:
#     print('not')        



#to print the prime numbers from 1 to 100
# number=2
# while number<=100:
#     i=1
#     count=0
#     while i<=number:
#         if number%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         print(number)
#     number=number+1

#to print fibonacci series:
# i=0
# n=7
# series=0
# while i<=n:
#     series=series+i
#     i=i+1
# print(series)

# to count no.of digits in a number:
# n=123456789
# count=0
# while n>0:
#     remainder=n%10
#     count=count+1
#     n=n//10
# print(count)


#to reverse the number
# n=1235
# res=0
# while n>0:
#     remainder=n%10
#     res=res*10+remainder
#     n=n//10
# print(res)

# n=111
# res=0
# while n>0:
#     remainder=n%10
#     res=res+remainder
#     n=n//10
# print(res)


# n=int(input("enter the number to check whether the given number is palindrome or not"))
# temp=n
# palindrome=0
# while temp>0:
#     remainder=temp%10
#     palindrome=palindrome*10+remainder
#     temp=temp//10

# if palindrome == n:
#     print('palindrome')
# else:
#     print('it is not')


#wap to find the given number is strong number or not 
# n=int(input("enter the number:"))
# temp=n
# total=0
# while temp>0:
#     product=1
#     i=1
#     remainder=temp%10
#     while i<=remainder:
#         product=product*i
#         i=i+1
#     total=total+product
#     temp=temp//10
# if n == total:
#     print('IT IS STRONG NUMBER')
# else:
#     print('not a strong number')


#write a programme to print strong numbers from 1 to 100
# i=1
# while i<=100:
#     n=i
#     total=0
#     while i>0:

#         remainder=i%10
#         j=1
#         product=1
#         while j<=remainder:
#             product=product*i
#             j=j+1
         
#         total=total+product
#         i=i//10
#     if total==n:
#         print(n)
#     i=n+1

#write a python programming to print smallest digit in the given number
# n=int(input("enter the number:"))
# smallest=9
# while n>0:
#     remainder=n%10
#     if  remainder<smallest:
#         smallest=remainder
#     n=n//10
# print(smallest)


# wap to print the perfect number using while loop
# n=int(input("enter the number:"))
# temp=n
# i=1
# sum=0
# while i<temp:
#     if temp%i==0:
#         sum=sum+i
#     i=i+1
# if sum == n:
#     print('it is a perfect number')
# else:
#     print("it is not a perfect number:")

#to print the given number is automorphic or not
# n=int(input("enter the n value ="))
# j=n*n
# while j>0:
#     remainder=j%10
#     if remainder==n:
#         print('automorphic')
#     else:
#         print('not automorphic')
#     break

#to print the given number is spy number
# n=int(input('enter the number: '))
# temp=n
# product=1
# sum=0
# while temp>0:
#     remainder=temp%10
#     sum=sum+remainder
#     product=product*remainder
#     temp=temp//10
# # print(sum)
# # print(product)
# if sum==product:
#     print('spy number')
# else:
#     print('not a spy number.Try with another number🤞')

#to print the given number is magic number or not
# n=int(input('enter the number: '))
# sum=0
# while n>0:
#     remainder=n%10
#     sum=sum+remainder
#     n=n//10
# sum2=0
# while sum>0:
#     remainder=sum%10
#     sum2=sum2+remainder
#     sum=sum//10
# if sum2==1:
#     print('magic number')
# else:
#     print('not')

#to check the given number is magic number or not
# n=int(input('enter the numer:'))
# while n>9:
#     sum=0
#     while n>0:
#         sum=sum+(n%10)
#         n=n//10
#     n=sum
# if n==1:
#     print('yes')
# else:
#     print('no')
    
# i=1
# while i<=100:
#     while i>9:
#         sum=0
#         while i>0:
#             sum=sum+(i%10)
#             i=i//10
#         i=sum
#     if sum == 1:
#         print(i)
#     i=i+1

# lcd of two given numbers
# n1=int(input("enter the number 1: "))
# n2=int(input("enter the number 2:"))
# if n1<n2:
#     i=2
#     l=[]
#     while i<=n1:
#         if n1%i==0 and n2%i==0:
#             l.append(i)
             
#         i=i+1
#     if len(l)==0:
#         print("there is no common factor")
#     else:
#         print("lcd",l[0])
#     # print("hcd",l[(l(len)-1)])
# else:
#     n1>n2
#     i=2
#     l=[]
#     while i<=n1:
#         if n1%i==0 and n2%i==0:
#             l.append(i)
                 
#         i=i+1
#     print("lcd",l[0])
#     # print("hcd",l[l(len)-1])


#gcd
# n1=int(input('enter the number 1: '))
# n2=int(input('enter the number 2: '))
# if n1<n2:
#     small=n1
# else:
    
#     small=n2
# i=small
# while i>=2:
#     if n1%i==0 and n2%i==0:
#         print("GCD",i)
#         break
#     i=i-1
# else:
#     print("no gcd")


#guessing the number game
# import random
 
# a=random.randint(1,9)
# print(a)
# i=1
# while i<=3:
#     n=int(input('enter the guessing number:'))
#     print(a)
#     if n == a:
#         print('you guess the right number')
#         break
#     else:
#         print('wrong guess')
#     i=i+1
# else:
#     print('you lost the game')


#ATM Transactions
#pin validation
# pin=1430 #pin
# balance=20000#amount in bank
# i=1
# while i<=3:
#     mypin=int(input('enter your pin :'))
#     if pin == mypin:
#         while True:
#             print("     welcome 🙏     ")
#             print("-----select the given Services-----")
#             print("1.withdrawl\n2.deposit\n3.checkbalance\n4.exit")
     
#             choose=int(input('enter the respective number for the services or select 4 for exit : '))
             
#             if choose==1:
#                 if balance!=0:
#                 # print('you dont have money to withdraw')
             
#                     amount_to_be_withdraw=int(input('enter the amount to withdraw '))
#                     if amount_to_be_withdraw >=100:
#                         if amount_to_be_withdraw % 5==0 and amount_to_be_withdraw %10==0:
#                             balance=balance-amount_to_be_withdraw
#                             print(f"your currrent balance is {balance}")
                            
#                         else:
#                             print('invalid amount')
#                     else:
#                         print('The limit withdrawl is 100 or above')
#                 else:
#                     print('you dont have sufficient amount to withdraw')


                        


             
#             elif choose==2:
#                 amount_to_be_diposited=int(input("enter the amount to be diposited"))
#                 if amount_to_be_diposited>=100:
#                     if amount_to_be_diposited%5==0 and amount_to_be_diposited%10==0:
#                         balance=balance+amount_to_be_diposited
#                         print(f"your balance is{balance}")
#                     else:
#                         print('invalid amount,please enter the valid amount')
#                 else:
#                     print('enter the amount 100 or above')
#             elif choose==3:
#                 print(balance)
#             elif choose==4:
#                 print("Thank you for choosing us.Bye Bye")
#                 break
#             else:
#                 print('select correct services between 1 to 4')
         
#         #print('valid')#for validation
         
#     else:
#         print('invalid')
#     i=i+1
# else:
#     print('Congragualations! You ATM has blocked')

#to print palindrom numbers between the two given numbers
# n1=int(input("enter the number from where you want to start: "))
# n2=int(input("enter the number where you want to stop : "))
# if n1>=0 and n2>=0:
#     while n1<=n2:
#         sum=0
#         temp=n1
#         while temp>0:
#             remainder=temp%10
#             sum=sum*10+remainder
#             temp=temp//10
#         if sum == n1:
#             print(n1)
#         n1=n1+1
#     else:
#         print('no palindrome found between the numbers you entered')
# else:
#     print('enter the number above or equal to zero')


# n=int(input('enter the number:'))
# a=int(input('enter the number:'))
# l=[]

# if n>=0 and a>=0:
#     while n<=100:
#         temp=n
#         i=2
#         while i<=(temp//2)+1:
#             if temp%i==0:
                
#                 break
#             # else:
#             #     l.append(temp)


#             i=i+1
#         else:
#             l.append(temp)

#         n=n+1
#     # print(l)
# else:
#     print('enter the number above or equal to zero')
# i=0
# while i<len(l):
#     if i%2==0:
#         print(l[i])
#     i=i+1


#to print the given strings are anagram or not
# n=set(input("enter the string1"))
# n1=set(input('enter the string2'))

# if len(n ^ n1)==0:
#     print('Anagram')
# else:
#     print('Not a anagram')


#to check the given number is strong number or not
# n=int(input('enter the number:'))
# i=1
# sum=0
# while i<=(n//2):
#     if n%i==0:
#         sum=sum+i
#     i=i+1
# if sum == n:
#     print('perfect')
# else:
#     print('not perfect')

#to print to sum of digits in given number
# n=int(input("enter the number"))
# sum=0
# while n>0:
  
#     remainder=n%10
#     sum=sum+remainder
#     n=n//10
     
# print(sum)


# n=153
# while n%10>0:
#     print(n)
#     n = n//10
# """
# 153
# 15
# 1
# """


# num=int(input('enter the number: '))
# while True:
#     s=0
#     while num>0:
#         d=num%10
#         s=s+d
#         num=num//10
#     if s>9:
#         num = s
#     else:
#         pass
#         break
# if s == 1:
#     print('magic number')
# else:
#     print('not a magic number')


# n=int(input('enter the number : '))
# largest=9
# while n>0:
#     r=n%10
#     if r<largest:
#         largest=r
#     n=n//10
# print(largest)

#strong number
# sum=0
# n=int(input('enter the number : '))
# temp=n
# while n>0:
#     remainder=n%10
#     product=1
#     i=1
#     while i<=remainder:
#         product=product*i
#         i=i+1
#     sum=sum+product
# n=n//10
# if sum == temp:
#     print('strong')
# else:
#     print('not strong')

# i=0
# while i<=1000:
#     if i%2==0 and i%3==0:
#         print(i)
#     i=i+1

#to print the prime numbers from 25 to 100 and skip the next prime number
# n1=int(input('enter the number : '))
# n2=int(input('enter the number : '))
# l=[]
# while n1<=n2:
#     i=1
#     count=0
#     while i<=n1:
#         if n1%i==0:
#             count=count+1
#         i=i+1
#     if count ==2 :
#         l.append(n1)
            
        
#     n1=n1+1
# i=0
# while i<len(l):
#     if i%2==0:
#         print(l[i])
#     i=i+1

#to print the highest number and and smallest and find the difference between them
# n=int(input('enter the number: '))
# temp=n
# smallest=9
# largest=0

# while temp>0:
#     remainder=temp%10
#     if remainder>largest:
#         largest=remainder
#     temp=temp//10
# while n>0:
#     remainder=n%10
#     if remainder<smallest:
#         smallest=remainder
#     n=n//10
# print('the largest number in the number is ',largest)
# print('the smallest number in the number is',smallest)
# span = largest-smallest
# print('the span number of number is ',span)

#to print the respective multiplied value from the given number to the given number
# n1=int(input('enter the number n1'))
# n2=int(input('enter the number n2'))
# while n1<=n2:
#     value=n1*(n1+1)
#     print(value)
#     n1=n1+1

#to print the divisble of 11 between any two numbers
# n=int(input('enter the number: '))
# n1=int(input('enter the number: '))
# while n<=n1:
#     if n%11==0:
#         print(n)
#     n=n+1

# n1=int(input('enter the 1st number:'))
# n2=int(input('enter the 2nd number:'))
# l=[]
# while n1<=n2:
#     i=1
#     count=0
#     while i<=n1:
#         if n1%i==0:
#             count=count+1
#         i=i+1
#     if count == 2:
#         l.append(n1)
#     n1=n1+1
# i=0
# l1=[]
# while i<len(l):
#     if i%2==0:
#         l1.append[l[i]]
#     i=i+1
# j=0
# while i<len(l1):

# num=1
# count=0
# while True:
#     cnt2=0
#     d=1
#     while d<=num:
#         if num%d==0:
#             cnt2=cnt2+1
#         d=d+1
#     if cnt2==2:
#         print(num)
#         count=count+1
#         if count==100:
#             break 

        