import arcpy

def createFeatureClass(outFolder, fc):
    arcpy.CreateFeatureclass_management(outFolder, fc, "POLYLINE")
    arcpy.AddField_management(fc, "Name", "TEXT")
    print ("Added Name field to feature class ...")
    
def addLine(name, pointList, cursor):
    polyline = arcpy.Polyline(pointList)
    cursor.insertRow((name, polyline))
    print("Added " + name)
    
