##Drawing a pattern using nested loops

size = in(input("Enter the size of the pattern::"))

i = 0 
while i < size:
    for j in range(size):
        print("*", end="")
    print()
    i += 1
