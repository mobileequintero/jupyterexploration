# Sentinel Value Loop
# create a variable coming from user

data = int(input("Enter a Integrer, the input exits with 0: "))
sum = 0
# variable for adding
while data != 0:
    # add the numbers
    sum += data 
    # example data 1, then sum is going to be sum = 0 + 1
    # keeo asking for data until data is 0
    
    data = int(input("Enter a Integrer, the input exits with 0: "))

print ("you got out of the loop")
print (" The sum is", sum)