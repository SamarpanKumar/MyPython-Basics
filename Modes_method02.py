#f = open('myfile02.txt', 'r')
#while True:
#    line = f.readline()
#    if not line:
#        break
#    print(line)

#f = open("myfile03.txt",'r')
#i = 0
#while True:
#    i = i+1
#    line = f.readline()
#    if not line:
#        break
   
#    m1 = int(line.split(",")[0])
#    m2 = int(line.split(",")[1])
#    m3 = int(line.split(",")[2])

#    print(f"Marks of Student{i} in Math is {m1*2}")
#    print(f"Marks of Student{i} in English is {m2*2}")
#    print(f"Marks of Student{i} in SST is {m3*2}")
#    print(line)



f = open('myfile04.txt','w')
lines = ['lines 1\n','line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
