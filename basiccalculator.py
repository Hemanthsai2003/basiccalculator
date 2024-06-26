def addition(firstnum, secondnum):
    return float(firstnum)+float(secondnum)
def subtraction(firstnum, secondnum):
    return float(firstnum)-float(secondnum)
def multiplication(firstnum, secondnum):
    return float(firstnum)*float(secondnum)
def division(firstnum, secondnum):
    return float(firstnum)/float(secondnum)
def modulodivision(firstnum, secondnum):
    return float(firstnum)%float(secondnum)

while True:
    firstnum = input("Enter a number (or 'exit' to quit) : ")
    if firstnum == "exit":
            print("Exiting the program.")
            break

    print("Select operator : \n1. + \n2. -\n3. *\n4. /\n5. %")
    operator =int(input("Enter your operator choice: "))
    secondnum = input("Enter another number : ")
    if operator == 1:
        result = addition(firstnum, secondnum)
    elif operator == 2:
        result = subtraction(firstnum, secondnum)
    elif operator == 3:
        result = multiplication(firstnum, secondnum)
    elif operator == 4:
        result = division(firstnum, secondnum)
    elif operator == 5:
        result = modulodivision(firstnum, secondnum)
    else:
        result = None
        print("Invalid operator choice.")

    if result is not None:
        print(f"The result is: {result}")