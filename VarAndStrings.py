#Dhilan Patel
# We are learning how to work with Srtings 
# While loop 
# Different type of var

num1=19
num2=3.5
num3=0x2342FABADCDACFACEEDFA
#How to know what type of data is a variable
print(type(num1))
print(type(num2))
print(type(num3))
phrase='Hello there!'
print(type(phrase))
#String functions 
num=len(phrase)
print(num)
print(phrase[3:7]) #print from 3 to 6
print(phrase[6:]) #from index to the end
print(phrase *2) #Print it twice 
#concadenation --> joining strings 
phrase = phrase + " "+ "Goodbye"
print(phrase[2:num-2])
while "there" in phrase:
    print("there" in phrase)
    phrase="changed"
    print(phrase)
# make 3 string variables print them individualy 
#"print s1+s2"
#print st2+st3
#print st1+st2 +st3
string= "Good Morning!"
string2="Good Afternoon!"
string3="Have a good day!"
print(string +" " + string2 )
print(string2 +" "+ string3)
print(string +" " + string2 +" " +string3)

