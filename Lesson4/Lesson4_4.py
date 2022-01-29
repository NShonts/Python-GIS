import arcpy

out_folder_path = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 4\\Lesson4_Data"
gdb_name = "Lesson4.gdb"
gdb_fullPath = out_folder_path + "/" + gdb_name


if not arcpy.Exists(gdb_fullPath):
    print ("Geodatabase does not exist. Creating...")
    arcpy.CreateFileGDB_management(out_folder_path, gdb_name)
else:
    print ("Geodatabase already exists")

arcpy.env.workspace = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 4\\Lesson4_Data"

#Find all Polygon features
FCList = arcpy.ListFeatureClasses("", "polygon")
number_of_polygons = len(FCList)
all_features = arcpy.ListFeatureClasses()
total_features = len(all_features)

#Loading polygons into geodatabase
arcpy.FeatureClassToGeodatabase_conversion(FCList, gdb_fullPath)
print(number_of_polygons, "were added to the geodatabase.")
print(total_features - number_of_polygons, "were skipped.")
