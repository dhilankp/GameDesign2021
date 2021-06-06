#Dhilan Patel 
#6/4/2021
#We are going to print a multiplication table 
# Asking the user what table 
# Input --> user input using the input funtion 
print ('What is the base?')
base=int(input())
print(type(base))
print('Math Tables',base)
print() 
for var3 in range (1,11): 
    resolved=base*var3
    print(base, 'x', var3, "=", (base*var3))
print()
for var3 in range (1,11): 
    resolved=base+var3
    print(base, '+', var3, "=", (base+var3))
print()
for var3 in range (1,11): 
    resolved=base-var3
    print(base, '-', var3, "=", (base-var3))
print()
for var3 in range (1,11): 
    resolved=base/var3
    print(base, '/', var3, "=", (base/var3))
print()

