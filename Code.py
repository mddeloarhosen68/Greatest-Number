x = int(input("Enter 1st Value:"))
y = int(input("Enter 2nd Value:"))
z = int(input("Enter 3rd Value:"))

if x > y and x > z:
    greatest = x

elif y > x and y > z:
    greatest = y

else:
    greatest = z

print(("The Greatest number is:",greatest))