# print ("hello")
# print ("hello world")
# *x, y, z = 10, 20, 30, 40, 50
# print(x)
# print(y)
# print(z)
# a= 5
# b= 6
# c= a
# print(id(a))
# print(id)


# p= float(input("enter principal amount: "))
# r= float(input("enter the annual interest rate: "))
# t= float(input("enter time period(in years): "))
# interest= (p*t*r)/100
# print("The simple interest is" interest)

# write a computer code which calculates
# the tax of an employee with given conditons:
# salary                           tax rate

# # below 20,000                     15%
# # 20,000 to 50000                  25%
# # 50,000 to 1,00,000               30%
# # above 1,00,000                   35%

# salary = 80000
# tax_rate = 0
# if(salary < 20000):
#     tax_rate = 15
# elif(salary >= 20000 and salary < 50000):
#     tax_rate = 25
# elif(salary >= 50000 and salary < 100000):
#     tax_rate = 30
# else:
#     tax_rate = 35

# real_tax = (salary * tax_rate)/100

# print(f'Salary is {salary}')
# print(f'Tax rate is {tax_rate}')
# print(f'Total tax amount is {real_tax}')
       

# print odd number from 1 to 20

# for x in range(1,20,2):
#     print(x)
from typing import Self


i = 1
# while i < 20:
#     print(i)
#     i = i+2

# display all the numbers 0 to 1000 which
#  is divisible by 11

# for x in range(11,1000,11):
#     print(x)

# i = 11
# while i < 1001:
#   if i % 11 == 0:
#     print(i)
#   i += 11

# for i in range(11,1000):
#     if i % 11 == 0:
#         print(i)

# cars =["Honda", "Toyota", "Bmw", "Audi", "Suzuki"]
# print(cars)
# cars.append("Hyundai")
# print(cars)

# cars.insert(3, "Test")
# print(cars)

# cars.remove("Honda")
# print(cars)

# cars.sort()
# print(cars)
 
# cars.reverse()
# print(cars)

# nums = [2, 4, 6, 8, 10]
# print(nums)
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(10 in nums)
#  print(nums.count(10))
#  print(nums.index(8))


# print("===Computer Bazaar===")
# print("1. Dell(Rs:20000) 2. Toshiba(Rs: 30000) 3. Mac: 50000")
# computer_option = int(input("select any option: "))
# quantity =int(input("enter quantity: "))
# print("Delivery option: ")
# print("1. Home(Rs:1000) 2. Pickup(Rs:0)")
# delivery_option = int(input("select delivery option: "))
# print("packing options: ")
# print("1. Plastic bag(Rs:1000) 2.Bag(Rs:2000) 3. Gift box(Rs:5000) 4. None(Rs.0)")
# packing_option = int(input("select packing option: "))
# print("location option: ")
# print("1. KTM(13% tax) 2. LTP(0) 3. BKT(0)")
# location_option = int(input("select location: "))
# price = 0
# if computer_option == 1:
#     price = 20000
# elif computer_option == 2:
#     price = 30000
# elif computer_option == 3:
#     price = 50000

# delivery_cost = 0
# if delivery_option == 1:
#   delivery_cost = 1000

# packing_cost = 0
# if packing_option == 1:
#     packing_cost = 1000
# elif packing_option == 2:
#     packing_cost = 2000
# elif packing_option == 3:
#     packing_cost = 5000

# tax_rate = 0
# if location_option == 1:
#     tax_rate = 0.13

# total_cost = price * quantity
# tax_amount = total_cost * tax_rate
# grand_total = total_cost + delivery_cost + packing_cost + tax_amount

# print("Total cost: Rs", total_cost)
# print("tax amount:", tax_amount)
# print("grand total: Rs", grand_total)

# num = 1
# while num <= 10:
#     i = 1
#     print(f"Multiplication Table Of {num}: ")
#     while i <= 10:
#         print(f"{num} x {i} = {num * i}")
#         i += 1
#         print()
#         num += 1
# def register():
#      username = input("Enter your email: ")
#      password = input("Enter your password: ")
#      with open("students.txt", "a") as obj:
#          obj.write(f"{username},{password}\n")


# def login():
#      username = input("Enter email: ")
#      password = input("Enter password: ")
#      with open('students.txt', 'r') as sObj:
#          data = sObj.readlines()
#          for line in sObj:
#              username, password = line.strip().split(",")
#          if username == username and password == password:
#                 print("Login successful")
#                 return
#          print("Invalid username or password")      

# import os
# import getpass

# if not os.path.exists('record.txt'):
#     with open('record.txt', 'w') as f:
#         pass


# def register():
#     print("========Register=========")
#     username = input("Enter your username: ")
#     username = username.strip()
#     if username in open('record.txt').read():
#         print('Username already exists')
#         exit()
#     password = getpass.getpass(prompt="Enter password: ")
#     password = password.strip()
#     confirm_password = getpass.getpass('confirm password: ')
#     confirm_password = confirm_password.strip()
#     if password != confirm_password:
#         print('Password do not match')
#         exit()
#     with open("record.txt", "a") as f:
#         f.write(f"username:{username}, password:{password}")
#         f.write("\n")
#     print("Registration successful")


# def login():
#     print("========Login=========")
#     username = input("Enter username: ")
#     username = username.strip()
#     password = getpass.getpass("Enter password: ")
#     password = password.strip()
#     with open('record.txt', 'r') as f:
#         login_success = False
#         for student in f.readlines():
#             uname = student.split(',')[0].split(':')[1].strip()
#             pword = student.split(',')[1].split(':')[1].strip()
#             if username == uname and password == pword:
#                 login_success = True
#         if login_success == True:
#             print(f'Welcome {username}')
#         else:
#             print("Invalid username or password")


# question = input("Do you have an account? (y / n) : ")
# if question == 'y':
#     login()
# elif question == 'n':
#     register()
# else:
#     print('Invalid input')
#     exit()


# class SPI:
   
#     def take_value(self):
#        p = int(input("enter principal: "))
#        r = int(input("enter rate: "))
#        t = int(input("enter time: "))
#        return[p, t, r]  
    

#     def calculate(self):
#         p, t, r = self.take_value()
#         si = (p * t * r)/100
#         return si


#     def display(self):
#         return f"The simple interest is : {self.calculate()}"


# obj = SPI()
# print(obj.display())

