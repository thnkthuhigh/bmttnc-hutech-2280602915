def ktsnt(n):
    if n<= 1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i ==0:
            return False
        return True
   
number=int(input("nhap so can kt: "))
if ktsnt(number):
    print(number,"la so nto.")
else:
    print(number,"k la so nto.")