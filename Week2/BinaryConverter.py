# This program converts integers and fractions into binary numbers.

x = float(input("Think of a number for binary conversion : "))

numint = int(str(x).split(".")[0])
numffloat = float("."+str(x).split(".")[1])

p = 0

while (numffloat*(2**p))%1 != 0:
    #print("remainder : " + str(numf*(2**p)- int(numf*(2**p))))
    p +=1
    
afterd = ""
num = int(numffloat*(2**p))
while num>0:
    afterd = str(num%2) + afterd
    num= num//2

befored = ""


while numint > 0:
    befored = str(numint%2) + befored
    numint = numint//2

for i in range(p-len(afterd)):
    afterd= "0" + afterd
    
final = befored + "." + afterd
    

print("Binary representation is : " +final)