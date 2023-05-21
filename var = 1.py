#userInput = input("enter 1 or 2: ")

#if userInput == 1:
  #   print ("Hello, World! ")
 #    print ("How are you ? ")

#elif userInput == 2:
  #  print ("Python rocks! ")
 #   print ("I love python ")

#else:
  #  print ("You didn't not enter an invalid number ")


#pets = ["cats", "dogs", "goats", "buffaloe", "chickens"]

#for myPets in pets:
    #print (myPets)

    #for index, myPets in enumerate(pets):
        #print(index, myPets)

#for i in range(5):
 #   print (i)

#for i in range(4, 20, 2):
 #       print(i)

#counter = 5

#while counter > 0:
 #   print("Counter = ", counter)
  #  counter = counter - 5 
  

#j = 0 

#for i in range(5):
  #  j = j + 2
   # print("i = ", i , "j = ", j)

    #if j == 6:
     #   break



#j = 0 

#for i in range(5):

 # j = j + 2

  #print("i = ", i, "j = ", j)

  #if j == 6:

   # continue
  #print("I will be skipped over if j = 6 ")





#try:

  #answer = 12/2

 # print(answer)

#except:

#  print("An error occured. ")




#try:

 # userInput1 = int(input("Please enter first number: "))
  
  #userInput2 = int(input("Please enter second number: "))

  #answer = userInput1/userInput2

  #print("The answer is ", answer)

 # myFile =open("Missing.txt", "r")

#except ValueError:

 # print("Error: You did not enter a number")

#except ZeroDivisionError:

 # print("Error: Cannot divide by zero")

#except Exception as e:

 # print("Unkown error: " , e)
  



#def checkIfPrime(numberToCheck):

 #for x in range(2, numberToCheck):
   
   #if (numberToCheck%x == 0 ):
     
    # return False

   #return True
      
     # answer = check_if_prime(13)



#from sys import argv

#script, myfile = argv

#txt = open ("myfile.txt", "r")

#firstline = txt.readline()
#secondline = txt.readline()
#print (firstline)
#print (secondline)

#txt.close()


'''
operation_1 = 
operation_2 =
operation_3 = 
operation_4 = 
answer = operation_1 , operation_2




def add(x , y):

  return x + y

def sub(x , y):

  return x - y 

def div(x , y):

  return x / y

def mult(x , y):

  return x * y




'''

'''
# Prompt for user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
# Perform operations
print("Sum: {} + {} = {}".format(a,b,a+b))
print("Difference: {} - {} = {}".format(a,b,a-b))
print("Product: {} * {} = {}".format(a,b,a*b))
print("Quotient: {} / {} = {}".format(a,b,a/b))
print("Power: {}^{} = {}".format(a,b,a**b))
print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))

'''

'''
# First part: Prompt for user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
""")
op = int(input("Enter the choice number: "))
# Second part: Perform operations based on input
if op == 1:
        print("Sum: {} + {} = {}".format(a,b,a+b))
elif op == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))
elif op == 3:
        print("Product: {} * {} = {}".format(a,b,a*b))
elif op == 4:
        print("Power: {}^{} = {}".format(a,b,a**b))
elif op == 5:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Division by 0 not possible!")
elif op == 6:
        try:
            print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
        except:
            print("Divsion by 0 not possible!")
else:
        print("No such choice!")

        '''





def prompt_menu():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    choice = "Y", "N"
    print("""
Choose an operation from the list:
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
    """)
    op = int(input("Enter the choice number: "))
    return a, b, op
def calculate():
    a, b, op = prompt_menu()
    if op == 1:
        print("Sum: {} + {} = {}".format(a,b,a+b))
    elif op == 2:
        print("Difference: {} - {} = {}".format(a,b,a-b))
    elif op == 3:
        print("Product: {} * {} = {}".format(a,b,a*b))
    elif op == 4:
        print("Power: {}^{} = {}".format(a,b,a**b))
    elif op == 5:
        try:
            print("Quotient: {} / {} = {}".format(a,b,a/b))
        except:
            print("Division by 0 not possible!")
    elif op == 6:
        try:
            print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b,a//b,a%b))
        except:
            print("Divsion by 0 not possible!")
    else:
        print("No such choice!")
    loop()
def loop():
    choice = input("Do you want to continue? (Y,N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input!")
        loop()
calculate()