a = int(input(" Enter your age : "))

# multiple if statement

# if statement no: 1

if(a%2 == 0):
    print("a is even")

else:
    print("a is odd")

# if statement no: 2

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering the invalid negative age")
    print("Chutiya h kya")

elif(a==0):
    print("You are enter the invalid age")
    print("Dudh pita bchcha h kya")

else:
    print("You are below the age of consent")

print("End of program")