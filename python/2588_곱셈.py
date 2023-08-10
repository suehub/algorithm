num1 = int(input())
num2 = int(input())

x1 = num1 * (num2 % 100 % 10)  
x2 = num1 * (num2 // 10 % 10)
x3 = num1 * (num2 // 100)

print(x1)
print(x2)
print(x3)

result = x1 + x2*10 + x3*100

print(result)