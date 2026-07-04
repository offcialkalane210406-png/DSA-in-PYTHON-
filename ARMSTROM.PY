num = 153
temp = num
result = 0

while temp > 0:
    ld = temp % 10
    result += ld**3
    temp = temp // 10

if result == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")