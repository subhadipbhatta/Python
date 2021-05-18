file1 = open("test", 'w')

for i in range(10):
    file1.write("Hello - this is my first file \n")

file1.close()

file2 = open("test", 'r')
#print(file2.read())

for j in file2:
    print(j)







