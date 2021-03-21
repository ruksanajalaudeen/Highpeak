f = open("sample_input.txt")                                   #reading from file
f.readline()
a=[]
for x in f:
    a.append(x[:len(x)].split(":"))                            #separating Goodie name and its price
c=[]
b=[]
for i in a:
    c.append(int(i[1]))
    b.append(i[0])

n = len(c)                    
for i in range(n-1):                                            #sorting goodie price and name
    for j in range(0, n-i-1):  
        if c[j] > c[j+1] : 
            c[j], c[j+1] = c[j+1], c[j]
            b[j], b[j+1] = b[j+1], b[j]
output=[]
n=int(input("Number of employees: "))                           #reading number of employees
print("")
for i in range(len(c)-(n-1)):
    output.append(c[i+(n-1)]-c[i])
ind=output.index(min(output))
print("Here the goodies that are selected for distribution are:")
for i in range(ind,ind+n):
    print(b[i],":",c[i])
print("")
print("And the difference between the chosen goodie with highest price and the lowest price is",output[ind])
op=open("sample_output.txt","w")
op.write("Here the goodies that are selected for distribution are:\n")
for i in range(ind,ind+n):
    op.write(b[i]+": "+str(c[i])+"\n")
op.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(output[ind]))
op.close()




