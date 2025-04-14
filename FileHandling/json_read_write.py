import json ,os    #Module need to be imported



os.chdir("d:\\Python_LB\\FileHandling\\test\\")

#creating the json
data = [
    {
    "Name" : "Akash",
    "Age"  : 34,
    "City" : "Mumbai"
    },
    {
    "Name" : "Suraj",
    "Age"  : 30,
    "City" : "Pune"
    },
    {
    "Name" : "Aniket",
    "Age"  : 28,
    "City" : "BLR"
    },
    {
    "Name" : "Vikas",
    "Age"  : 38,
    "City" : "Hyd"
    }
]


with open("Data.json",'w') as file:
    json.dump(data , file ,indent=4 )

print('Data is written')

#Reading the data from the json file
with open("Data.json",'r') as file:
   result = json.load(file)

print("Data available in the json file as below\n====================================")
print(result)

#a = []
for data in result:
    print(f"The Employee Name : {data['Name']}\nThe Employee Age : {data['Age']}\nThe Employee City : {data['City']}\n====================================")
    #print(f"{data},")
    #a.append(data)

#print(a)