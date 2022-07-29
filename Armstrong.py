num = int(input("Enter a 3 digit number: "))
summ=0
temp=num
4
while (temp>0):
    digit = temp % 10
    summ += digit**3
    temp //= 10
if (num==summ):
    print(f"{num} is an Armstrong Number:")
else:
    print(f"{num} is not an Armstrong Number")
