import arcpy
import Homework9_2_Functions

# Set up the Environment
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data"

#Set paths
outFolder = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data"
fc = "WellPaths.shp"


inputPath = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 6\\Lesson6_Data\\WellPaths.txt"

#Open txt
inputFile = open(inputPath)

name = ""
nameList = []

Homework9_2_Functions.createFeatureClass(outFolder, fc)

cursor = arcpy.da.InsertCursor(fc, ["Name","SHAPE@"])
print ("Opened feature class for editing...")

for line in inputFile:

    #Split file by delimeter
    lineSegment = line.split(", ")
    #print(lineSegment)

    name = lineSegment[0]
    
    #If Name is not in list, it is either the first line or a new well line
    if name not in nameList:
        length = len(nameList)
        print(length)
        nameList.append(name)
        #print(nameList)
        pointList = arcpy.Array([arcpy.Point(lineSegment[1], lineSegment[2])])
        print(pointList)
        if len(pointList) > 0:
            Homework9_2_Functions.addLine(name, pointList, cursor)
        print(nameList)
        print(pointList)
        pointList = arcpy.Array()
           

    #If name is in list, add values only    
    else:
        coordinate = line.split(", ")
        point = arcpy.Point(coordinate[1], coordinate[2])
        pointList.add(point)
        Homework9_2_Functions.addLine(name, pointList, cursor)

#Add last record
Homework9_2_Functions.addLine(name, pointList, cursor)

del cursor
        
            
            
        
