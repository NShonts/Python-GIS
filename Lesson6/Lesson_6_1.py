import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data\\"
fClass = "Cities.shp"


#Setup Search cursor and create output file
cursor = arcpy.da.SearchCursor(fClass, ["NAME", "SHAPE@"])
CitiesFilePath = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data\\Cities.txt"
print("New file created")

#Open file for writing
CitiesFile = open(CitiesFilePath, "w")
print("File opened")

#Iterate through rows, print city name and x,y coordinates
for row in cursor:
    for point in row[1]:
        #Write name and coordinates to file
        CitiesFile.write(row[0] + "," + ("{}, {}".format(point.X,point.Y)) + "\n")
#Close file
CitiesFile.close()
