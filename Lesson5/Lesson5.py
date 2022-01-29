import arcpy
import sys
import traceback

countiesPath = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 5\\Lesson5_Data\\COUNTIES.shp"
wellsPath = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 5\\Lesson5_Data\\Wells.shp"

##Create counties layer and wells layer
arcpy.MakeFeatureLayer_management(countiesPath, "counties_lyr")
arcpy.MakeFeatureLayer_management(wellsPath, "wells_lyr")


#Set Variables
fieldList = ["nowells", "density", "county", "SHAPE@AREA"]
wells = 0
density = 0


try: 
    with arcpy.da.UpdateCursor(countiesPath, fieldList) as cursor:
        for row in cursor:
            #Loop through each county
            whereClause = "COUNTY = '" + row[2] + "'"
            print(whereClause)
            #Create layer of selected county
            arcpy.MakeFeatureLayer_management(countiesPath, "county_lyr", whereClause)
            print("layer created")
            #Select wells within the created county layer
            arcpy.SelectLayerByLocation_management("wells_lyr", "WITHIN", "county_lyr", "", "NEW_SELECTION")
            #Find number of wells selected in county layer
            wells = int(arcpy.GetCount_management("wells_lyr").getOutput(0))
            print(wells)
            #Set NoWells field equal to number of wells
            row[0] = wells
            #Find density of wells in ShapeArea
            density = wells / row[3]
            print(density)
            #Set Density field equal to density of wells in ShapeArea
            row[1] = density
            #Update row in fields
            cursor.updateRow(row)
            #Delete county layer to allow loop to continue
            arcpy.Delete_management("county_lyr")
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)
    print(pymsg)
    print(msgs)


        
