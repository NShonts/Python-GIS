import arcpy

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


arcpy.CreateFeatureclass_management(outFolder, fc, "POLYLINE")
arcpy.AddField_management(fc, "Name", "TEXT")
print ("Added Name field to feature class ...")
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
            polyline = arcpy.Polyline(pointList)
            cursor.insertRow((name, polyline))
            print("Added " + name)
            print("ADDED COORDINATES")
        print(nameList)
        print(pointList)
        pointList = arcpy.Array()
           

    #If name is in list, add values only    
    else:
        coordinate = line.split(", ")
        point = arcpy.Point(coordinate[1], coordinate[2])
        pointList.add(point)
        polyline = arcpy.Polyline(pointList)
        cursor.insertRow((name, polyline))

#Add last record
polyline = arcpy.Polyline(pointList)
cursor.insertRow((name, polyline))
print("Added " + name)

del cursor
        
        
            
            
        
