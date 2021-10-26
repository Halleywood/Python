dict1 = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
list=['hello','there','man']
dict2 = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
dict3={'catname':'Kirby', 'catname2':'Fran', 'catname3':'Elwood'}
#*cmp(dict1,dict2)
#!NOT WORKING???
#*len() 
#!will tell you length of dictionary. in below example will print out TWO!!!
print(len(dict1))
#*str() 
#! produces string representation of dictionary. just prints out whole dictionary...
print(str(dict3))
print(str(dict1))

#*type(): returns type of passed variable. If passed variable is a dictionary will return 
#*"dict"? prints "<class 'dict'>" last one prints <class 'list'>
print(type(dict1))
print(type(dict3))
print(type(list))

#* prints [catname, catname2, catname3]??
print(sorted(dict3))

#dict10.update(dict20) would merge dict1 and 2 together. 
print(dict1)

#* prints out all key names
print(dict3.keys())
#! to have all values. 
print(dict3.values())
#!to have all the items
print(dict3.items())

for key in dict3.keys():
    print("Key: ", key)
for value in dict3.values():
    print("Value: ", value)
for k, v in dict3.items():
    print("Key: ", k)
    print("Value: ", v)
#RESULTS: key:catname key:catname2 key:catname3 Value: Kirby value: Fran Value:Elwood
#results: key:catname value:Kirby etc...

print(dict3.get('catname'))
#results in Kirby 
pet=dict3.get('catname')
print(pet)
pets=dict3.get('kirby')
print(pets)
