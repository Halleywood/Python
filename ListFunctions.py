list=[1,2,3,11]
list.append(10)
print(list) #will add 10 to the end

list.extend(list)
print(list) #will now print the list twice 

list.remove(10)
print(list) #removes the first 10 value it finds. 

list.pop(8)
print(list) #removes value at index 8 which is 10. 

print(list.index(2)) #prints the INDEX# of the given value. 
print(list.index(3)) #prints the INDEX# of the given value. 

print(list.count(11))#shoes how many times value appears in list. 

list.reverse() #will reverse list order. 
print(list)
list.reverse()#will reverse it back to original order. 
print(list)

print(sorted(list, reverse=True)) #will sort list by given parameters

