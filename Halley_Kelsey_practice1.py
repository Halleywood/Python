#1
#def number_of_food_groups():
#    return 5
#print(number_of_food_groups())
#nothing. need to store return in a variable. 
#!ACTUALLY RETURNS 5. 

#2
#def number_of_military_branches():
#    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#nothing. need to store return as a variable??
#!Correct, Reports ERROR, first function not defined. 

#3
#def number_of_books_on_hold():
#    return 5
#    return 10
#print(number_of_books_on_hold())
#will return 10 or nothing because not stored in a variable. 
#! actually returns 5. hits first return statement and exits. 

#4
#def number_of_fingers():
#    return 5
#    print(10)
#print(number_of_fingers())
#print("answerto4")
#will return 5?
#! correct, returns 5. 

#5
#def number_of_great_lakes():
#    print(5)
#x = number_of_great_lakes()
#print(x)
#will return 5?
#! prints 5, none.


#6
#def add(b,c):
#    print(b+c)
#print(add(1,2) + add(2,3))
#print("answerto6")
#prints 3, prints 5, prints 8 #! actually prints out error "unsupported operand?"


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
print("answerto7")
#will print 25? #! correct

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
print("answerto8")
#will print 10 #! WILL PRINT OUT 100, then 10. 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print("answerto9")
#will print 7,14,7,14,7 #! PRINTS 7, PRINTS 14, PRINTS 21. 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
print("answerto10")
#will return 8?? #! correct

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
print("answerto11")
#will print 500. print 500. print 300.print 500? #! correct

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
print("answerto12")
#500. 500. 300. 500. #! correct

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
print("answerto13")
#500. 500. 300. 300? #! CORRECT
#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
print("answerto14")
#1. 3. 2. #! correct
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
print("answerto15")
#1. 3. 5. #! ALSO PRINTS 10. SO ANSWER= 1,3,5,10!