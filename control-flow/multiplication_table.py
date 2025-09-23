# multiplication table

number = int(input("Enter the number you want to see its multiplication:"))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    result = number * i
    print(f"{number} * {i} = {result}")
    
    