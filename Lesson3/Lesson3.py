#import system module
import arcpy
arcpy.CheckOutExtension("Spatial")
from arcpy.sa import *

arcpy.env.overwriteOutput = True

#Set environment
arcpy.env.workspace = "C:/Users/Nate/Documents/Python GIS/Lesson 3/Lesson3_Data"

#Define variables
in_point_features = "WellsSubset.shp"
z_field = "TD"
out_polyline_features = "output.shp"


#Run Natural Neighbor Tool, creates raster from data
raster = NaturalNeighbor(in_point_features, z_field)

#Run Contour tool with 1500 as interval, output shapefile to out_polyline_features variable
Contour(raster, out_polyline_features, 1500)

arcpy.CheckInExtension("Spatial")
