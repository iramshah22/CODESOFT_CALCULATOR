#SYEDA IRRAM HASSAN
#SIMPLE CALCULATOR USING PYTHON
#CODESOFT INTERNSHIP TASK 2
 
def add(x,y):    
   # This function is used for adding two numbers   
   return x+y  
def subtract(x,y): 
   # This function is used for subtracting two numbers   
   return x-y 
def multiply(x,y):   
   # This function is used for multiplying two numbers   
   return x*y 
def divide(x,y):   
   # This function is used for dividing two numbers    
   return x/y   
def exponent(x,y):
   return x**y
# Now we will take inputs from the user   
print("\n\n\n") 
print("***********This is your simple Calculator**********")
print()
print ("Select from below the operation you want to perform")    
print()
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide") 
print ("e. Exponent")   
    
choice = input("Please enter your choice (a/ b/ c/ d/ e): ")  
print()  
    
num1 = int (input ("Please enter the first number: "))    
num2 = int (input ("Please enter the second number: ")) 
print("\n")   
if choice == 'a':    
   print (num1, " + ", num2, " = ", add(num1, num2))    
    
elif choice == 'b':    
   print (num1, " - ", num2, " = ", subtract(num1, num2))    
    
elif choice == 'c':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == 'd':    
   print (num1, " / ", num2, " = ", divide(num1, num2))    
elif choice == 'e':
   print (num1, " ** ", num2, " = ", exponent(num1,num2))
else:    
   print ("This is an invalid input")   