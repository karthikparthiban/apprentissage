#list Comprehension
#ex_1
vehicle=['bike','car','bus','flight','ship']
newvehicle=[]
for x in vehicle:
    if 'b' in x:
        newvehicle.append(x)
print(newvehicle)                           #for using for loop method_
#ex_2
name=['sanjay','vijay','sangeeth','vishnu','dinesh','diveshkumar']
new_name=[]
for y in name:
    if 'd'in y:
        new_name.append(y)
print(new_name)

#ex_3                                   #list Comprehension methods
name=['sanjay','vijay','sangeeth','vishnu','dinesh','diveshkumar','premkumar']
new_name=[x for x in name if 'kumar' in x]
print(new_name)
#ex_4
name=['sanjay','vijay','sangeeth','vishnu','dinesh','diveshkumar','premkumar']
new_name=[x for x in name if x!='vishnu']
print(new_name)
#ex_5
name=['sanjay','vijay','sangeeth','vishnu','dinesh','diveshkumar','premkumar']
new_name=[x.upper() for x in name if x!='vishnu']
print(new_name)
#ex_6
name=['sanjay','vijay','sangeeth','vishnu','dinesh','diveshkumar','premkumar']
new_name=[x if x!='vishnu' else 'hariharan' for x in name]
print(new_name)

#filehandling
file=open("C:\Users\TEST\Desktop\csv","r")
print(file.read())

myfile = open('C:/Users/TEST/Desktop/csv.csv','r')
mytxt = myfile.read()
 myfile.close()