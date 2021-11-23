
import json
import urllib.request
from html.parser import HTMLParser

metacount = 0; #global variable to count meta tags in start tags. ie class/id/value/input etc...

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data): #overridding default function of handle_comment method
        print("Encountered comment: ", data)
        pos=self.getpos() #get position
        print("\tAt line: ", pos[0], "position ", pos[1])
        # FOR THE ABOVE FUNCTION, When Parser comes across HTML comment through the ".read" function, will call on the "handle_comment" method
        #will pass the text as data print out a string (line 9) then get the position in the file where the comment was found (line 10/11)

    def handle_starttag(self, tag, attrs): #is the same as others but as you know with HTML, has many tag characteristics ie "class/id/onclick/value etc" which are the attrs!!
        print("Encountered comment: ", tag)
        global metacount
        if tag == 'meta':
            metacount +=1
        pos=self.getpos() #get position
        print("\tAt line: ", pos[0], "position ", pos[1])
        if attrs.__len__() > 0: 
            print("\Attributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])


    def handle_endtag(self, tag): #dont have any attrs in ending tags or inside html text! 
        print("Encountered comment: ", tag)
        pos=self.getpos() #get position
        print("\tAt line: ", pos[0], "position ", pos[1])

    def handle_data(self, data):
        if data.isspace(): #you want to print out just the HTML text data, this omits white space/blank lines
            return
        print("Encountered comment: ", data)
        pos=self.getpos() #get position
        print("\tAt line: ", pos[0], "position ", pos[1])

def printResults(data):
    #use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    #now we can access the contents of the JSON like any other Python object 
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
#output the number of events, plus the magntude and each event name
    count = theJSON["metadata"]["count"]
    print (str(count) + "events recorded")

#for each event, print the place where it occured 
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("------------\n")
#print the events that have a magnitude of 4 or greater 
    for i in theJSON["features"]:
        if (i["properties"]["mag"] > 4.0):
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("-----!-!-!------\n")

#print out events that were felt or reported feeling something
    print("Events that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported "  +str(feltReports) + " times")
    print("--#---#----#\n")

def main():
    #define a variable to hold the source URL
    #in this case we'll use the free data feed from the USGS
    #this feed lists all earthquakes for the last day larger than Mag 2.5
    urlData="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    #open the URL and read the data
    webURL = urllib.request.urlopen(urlData)
    print("result code:" + str(webURL.getcode()))

    if(webURL.getcode() ==200):
        data=webURL.read()
        printResults(data)
    else:
        print("received error code")

#main()
##########PARSING AND PROCESSING HTML

#example for parsing and processing HTML
def text():
    #create a variable which is an instance of the MYHTMLPARSER class. 
    parser=MyHTMLParser()
    #will open our HML file
    f = open("samplehtml.html")
    #if file exists (what r means) then:
    if f.mode =='r':
        print("found")
        contents = f.read() #reads the entire file
        parser.feed(contents) #pass in the contents to be parsed 
    print("meta tags found:" + str(metacount))

text()





