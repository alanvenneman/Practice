import arcpy


subdiv = r'C:\Users\avenneman\Documents\Programming\SelectWork\Features.gdb\Subdivisions_Res'
mxd = arcpy.mapping.MapDocument(r"C:\Users\avenneman\Documents\Programming\SelectWork\ProjectSerialNumber.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "u*")[0]
def create_list():
    file = open("try_it.txt", "w")
    file.write("ELDRIDGE LAKE SECTION 2")
    file.close()

def data_frame():
    read = open("try_it.txt", "r")
    wc = read.readline()
    read.close()
    arcpy.SelectLayerByAttribute_management(subdiv, "NEW_SELECTION", wc)
    df.zoomToSelectedFeatures()
    arcpy.RefreshActiveView()

del mxd, df
