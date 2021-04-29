
# Print a Alphabet tree diagram like this
# A
# A B
# A B C
# A B C D
# A B C D E

rows = int(input("Enter Number of Rows? "))

for i in range(rows):
    for j in range(i):
        print(chr(j+65), end=" ")
    print()