number = input("Enter the Binary Number = ")
numbers = ['1', '0']

while True:

    if len(number) != 8:
        print("Number should be equal to 8.")
        number = input("Enter the Binary Number = ")
        continue

    i = 0
    valid = True

    while i < len(number):
        if number[i] not in numbers:
            print(f"Wrong input at position {i+1}")
            valid = False
            break

        i += 1

    if valid:
        break

    number = input("Enter the Binary Number = ")


value = [1, 2, 4, 8, 16, 32, 64, 128]
value = value[::-1]

total = 0

for i in range(len(value)):
    n = number[i]
    val = value[i]

    if n == '1':
        total += val

print(total)