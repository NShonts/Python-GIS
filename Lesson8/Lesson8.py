import arcpy

arcpy.env.overwriteOutput = True

#Define paths
workspace = r"C:\\Users\\Nate\\Documents\\Python GIS\\Lesson 8\\Lesson8_Data"
output = workspace + r"\Lesson8_Project"
CountyLayer = workspace + r"\Counties.shp"

tempPDF = output + r"\temp.pdf"
finalPDF = output + r"\final.pdf"

#Obtain pointers
aprx = arcpy.mp.ArcGISProject(output + r"\Lesson8_Project.aprx")
mapx = aprx.listMaps("Jefferson")[0]
lyr = mapx.listLayers("Counties")[0]
lyt = aprx.listLayouts("Colorado")[0]
mf = lyt.listElements('MAPFRAME_ELEMENT', "Map Frame")[0]


#Create empty PDF
pdfDoc = arcpy.mp.PDFDocumentCreate(finalPDF)

#Export original data frame to PDF
lyt.exportToPDF(tempPDF)
pdfDoc.appendPages(tempPDF)


with arcpy.da.SearchCursor(CountyLayer, "COUNTY") as cursor:
    for row in cursor:
        whereClause = """ "COUNTY" = '{0}' """.format(row[0])
        lyr.definitionQuery = whereClause
        mf.camera.setExtent(mf.getLayerExtent(lyr))
        mf.camera.scale *= 1.3

        title = lyt.listElements('TEXT_ELEMENT', "Text")[0]
        title.text = row[0] + ", CO"

        lyt.exportToPDF(tempPDF)
        pdfDoc.appendPages(tempPDF)

pdfDoc.saveAndClose()
del pdfDoc
del aprx
