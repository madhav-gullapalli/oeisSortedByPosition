file2 = open("textDB.txt","r+")
lines = file2.readlines()
k = 0
for line in lines:
    k += 1
    b = line.split()
    if(len(b) > 1 and b[0][0] != ','):
        if(k%1000 == 0):
            print(k)
        fileDB = open(f"C:\\Users\\madha\\PycharmProjects\\oeisVisualizer\\textDBData\\textDB{b[0]}.txt","w+")
        fileDB.write(line)
        fileDB.close()