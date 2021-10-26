
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


#!1.) UPDATE VALUES IN DICTIONARIES 
#!Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
#!Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Bryant'
#!In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)
#!Change the value 20 in z to 30
z[0]['y']=30
print(z)


#Iterate Through a List of Dictionaries
def iterateDictionary(students):
    for i in range(len(students)):
        print(students[i]['first_name'])
        print(students[i]['last_name'])
iterateDictionary(students)

#!solution from video
def iteratedictionary(key_value, list):
    for i in range(len(list)):
        for key,value in list[i].items():
            if key==key_value:
                print(value)
iteratedictionary('first_name', students)
iteratedictionary('last_name', students)


#!bonus to get them to appear exactly as below!)
#!first_name - Michael, last_name - Jordan
#!first_name - John, last_name - Rosales
#!first_name - Mark, last_name - Guillen
#!first_name - KB, last_name - Tonel

def iterateDictionary(list):
    for i in range(len(students)):
        first='first_name'
        last= 'last_name'
        for first,last in list[i].items():
            print(f"{first}-{last}")    
iterateDictionary(students)  

#!solution from video!
def iteratedictionary(list):
    for i in range(len(students)):
        name=""
        for key,value in list[i].items():
            name+=(f"{key}-{value},")
        print(name)
iteratedictionary(students)


#*3)Get Values From a List of Dictionaries
#*Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
#*the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students)
#*should output: "michael,john,mark,kb" etc...

def iterateDictionary2(some_key, list):
    for i in range(len(students)):
        print(list[i][some_key])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)       

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# 4.)Iterate Through a Dictionary with List Values
#  Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values
# within each key's list. For example:
def printinfo(some_dictionary):
    for key,value in some_dictionary.items():
        print(len(value), key.upper())
        for i in range (len(value)):
            print(value[i])
printinfo(dojo)
