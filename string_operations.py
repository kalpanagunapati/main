#strings = collection of words
print("kalpana")

#string concatination
a="kalpana "
b="Gunapati"
print(a+b) #o/p kalpana Gunapati 

#string Repetation 
a="* " *10 
print(a)

#first n characters in a string 
a=input() #kalpana
n=input()
n=int(n) # 3
part=a[:n]
print(part) #o/p kal 

# last n characters in a string 
a=input() #kalpana
n=input() 
n=int(n) #4 
length=len(a) #7
start_index=length-n #3
part=a[start_index:] 
print(part) #o/p pana 

