from math import sqrt

print ("Giai phuong trinh bac 2: ax^2 + bx + c = 0")
print ("Moi ban nhap:")
while True:
	try:
		a=float(input("Nhap a: "))
		break
	except ValueError:
		print("Vui long nhap so.")
print("a = " + str(a))

while True:
	try:	
		b=float(input("Nhap b: "))
		break
	except ValueError:
		print ("Vui long nhap so.")
print ("b = " + str(b))

while True:
	try:
		c=float(input("Nhap c: "))
		break
	except ValueError:
		print ("Vui long nhap so")
print ("c = " + str(c))

print ("---Ket qua: ----")

if a==0:
	if b==0:
		if c==0:
				print ("Phuong trinh vo so nghiem")
		else:
				print ("Phuong trinh vo nghiem")
	else:
			print ("Phuong trinh co 1 nghiem:",-c/b)
else:
	delta= b**2-4*a*c
	if delta <0:
		print ("Phuong trinh vo nghiem.")
	elif delta ==0:
		print ("Phuong trinh co 1 nghiem voi x= ",-b/(2*a))
	else:
		print ("Phuong trinh co 2 nghiem rieng biet x1 va x2:")
		print ("x1= ", float((-b - sqrt(delta))/ (2*a)))
		print ("x1= ", float((-b + sqrt(delta))/ (2*a)))
