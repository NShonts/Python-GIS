import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 7\\Lesson_7_Data"

arcpy.CheckOutExtension("Spatial")

landuseRaster = "landusep"

#River Raster
riverRaster = "reclassriv"

remapRiver = []
remapRiver.append([1, 0])
remapRiver.append(["NODATA", 1])

riverValues = arcpy.sa.RemapValue(remapRiver)

riverReclass = arcpy.sa.Reclassify(riverRaster, "VALUE", riverValues, "NODATA")
riverReclass.save("C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 7\\Lesson_7_Data\\ReclassRiver")

#Lake Raster
lakeRaster = "lakebuff"

remapLake = []
remapLake.append([1, 0])
remapLake.append(["NODATA", 1])

lakeValues = arcpy.sa.RemapValue(remapLake)

lakeReclass = arcpy.sa.Reclassify(lakeRaster, "VALUE", lakeValues, "NODATA")
lakeReclass.save("C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 7\\Lesson_7_Data\\ReclassLake")

#Rock Porosity Raster
rockRaster = "rockpor"

remapRock = []
remapRock.append([1, 3, 1])
remapRock.append([3, 6, 2])
remapRock.append([6, 9, 3])
remapRock.append([9, 12, 4])
remapRock.append([12, 15, 5])

rockValues = arcpy.sa.RemapRange(remapRock)

rockReclass = arcpy.sa.Reclassify(rockRaster, "VALUE", rockValues, "NODATA")
rockReclass.save("C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 7\\Lesson_7_Data\\ReclassRock")

#Map Algebra
finalRaster = riverReclass * lakeReclass * landuseRaster * rockReclass
finalRaster.save("C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 7\\Lesson_7_Data\\finalRaster")


arcpy.CheckInExtension("Spatial")
