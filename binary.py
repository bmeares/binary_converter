input = int(input("Enter a decimal number: "))
remainders = []
while input != 0:
    remainders.append(input % 2)
    input //= 2
for i in remainders[::-1]:
    print(i,end="")
print()
