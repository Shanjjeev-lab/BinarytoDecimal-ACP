binary = "1110"
decimal = 0
count = len(binary) - 1
for i in range(0, len(binary) - 1):
    power = 2 ** count
    num = len(binary[i]) * power
    decimal += num
    count = count - 1

print(decimal)