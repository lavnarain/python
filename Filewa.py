fd=open("C:\\Users\\iot\\Desktop\\Python Codes\\Files.txt","w+")
for i in range(4):
    LikhneWala=input('Give line number %d: '%(i))
    fd.write(LikhneWala+'\n')
# fd.write("vdjbvjdbjdb\nhdwjgbjfwbdjf\nhndlkjblkfjwd\nnhfjklvbfklj")
fd.seek(0)
l1=fd.readlines()
cnt =1
for x in l1:
    print(cnt,x)
    cnt +=1

print("Total number of lines: ",len(l1))