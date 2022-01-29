leaseFile = open("C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data")
outputFIle = open("C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data\\Output.txt", "w")

for line in leaseFile.readlines():
    print(line)
leaseFile.close()


outputFile.write("This is a new file")

for line in leaseFile.readlines():
    outputFile.write()
outputFile.close()
