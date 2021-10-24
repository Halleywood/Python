string="a Big, brown, Fox jumped over the big, brown log"
string1="alphabravo"
string2="1,2,3"
string3="12345"
print(string.upper())
print(string.lower())

print(string.count("brown")) #will returin number of occurences, which is 2. 

print(string.split()) #if nothing specified will chop string at EVERY SPACE. 
print(string.split(",")) #chops up string AT EVERY ","

print(string.find(",")) #returns INDEX of the start of the first defined
#bunstring appearance...comma shows up at space 6 or index 5?
print(string.find("B")) #shows up at space 3 or index 2. 
print(string.isalnum()) #will print TRUE it it only letters and numbers. 
#because there are spaces and punctuation it will return false! 
print(string1.isalnum()) #will return true. 

print(string1.isalpha()) #returns true IF ONLY LETTERS, no spaces/numbers etc

print(string.isdigit()) #returns false
print(string2.isdigit()) #returns false
print(string3.isdigit()) #returns true. no spaces!

print(string.islower()) #returns false if any upper case
print(string1.islower()) #returned TRUE, no uppercase. 

print(string.isupper()) #returned false, not all upper 

print(string.upper())
print(string.isupper()) #WILL STILL RETURN FALSE. "string.upper" is
#only a print function...does not actually change string variable!!!

print(string.join(string1)) #literally joined string 1 to A, then L, then P etc. 
print(string1.join(string3)) #returns 1alphabravo2alphabravo3alphabravo
#4alphabravo5. NOTE it does not add to end of 5??? sandwiched between??
print(string3.join(string1)) #does not add 12345 to last O. sandwiched between. 

print(string.endswith("g")) #returns a true
print(string1.endswith("g")) #returns a false. 
