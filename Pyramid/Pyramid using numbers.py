rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\n")