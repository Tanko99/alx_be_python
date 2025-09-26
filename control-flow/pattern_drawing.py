##Drawing a pattern using nested loops

size = int(input("Enter the size of the pattern::"))

row = 0 
while row < size:
    for columns in range(size):
        print("*" end="")
    print()
    row += 1
    
