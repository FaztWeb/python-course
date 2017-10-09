def createFile():
    file = open('data.txt', 'w')
    file.close()

def writeFile():
    #a is to append data to the file
    file = open('data.txt', 'a')
    file.write('Isaac Asimov\n')
    file.write('546445')
    file.close()

def readFile():
    file = open('data.txt', 'r')
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()
    file.close()
    
readFile()
