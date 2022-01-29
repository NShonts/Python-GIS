import arcpy

arcpy.env.workspace = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 4\\Lesson4_Data"

FCList = arcpy.ListFeatureClasses()

for feature in FCList:
    print (feature + ", " + arcpy.Describe(feature).shapeType)
