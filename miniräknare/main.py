def addition (x, y):
   return x+y
def subtraction (x,y):
   return x-y
def multiplication (x, y):
   return x*y
def division (x, y):
   return x/y
print ("Vill du 1. addera, 2. subtrahera, 3. multiplicera eller 4. dividera?")
choice =int(input ())
print ("Skriv första numret")
nummer1 =int(input ())
print ("skriv andra numret")
nummer2 =int(input ())
if choice ==1:
    print (nummer1, "+", nummer2, "=", addition (nummer1, nummer2))
if choice ==2:
    print (subtraction(nummer1, nummer2))
if choice ==3:
    print (multiplication(nummer1, nummer2))
if choice ==4:
    print (division(nummer1, nummer2))
