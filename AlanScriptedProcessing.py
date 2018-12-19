# AlanScriptedProcessing.py
# Author: Alan Venneman
# Date: December 18, 2018
# Purpose: Buffers roads in a zip code in Fort Bend County by one tenth the squared speed limit.
# Inputs: strZip = zip code
# Outputs: roadsInZipXXXX = feature class
##################################################
print("-" * 40)

# import modules and correct license
import arcview
import arcpy
import os

# Set the environments and variables
workspace_path = r"C:\Student\ICTPythonGIS\Data"
arcpy.env.workspace = (os.path.join(workspace_path, "Texas.gdb"))
arcpy.env.overwriteOutput = 1

# Check if Scratch.gdb exists - create if necessary
scratch_ws = os.path.join(workspace_path, "Scratch.gdb")
if arcpy.Exists(scratch_ws):
    print("Scratch geodatabase detected.")
else:
    arcpy.CreateFileGDB_management(scratch_ws)
    print("New Scratch Geodatabase created.")
arcpy.env.scratchWorkspace = scratch_ws

# Select the ZIP Code
print("Selecting")
zip = raw_input("Enter zip: ")
zip_shape = "FB_Zip_Codes"
select_zip = "Zip" + zip
zip_query = "\"ZIP\" = '" + zip + "'"
arcpy.Select_analysis(zip_shape, select_zip, where_clause=zip_query)
print("Selected")

# Clip the roads
print("Clipping")
fbc_roads = "FortBend_Roads"
arcpy.Clip_analysis(fbc_roads, "Zip77471", "RoadsInZip77471")
print("Clipped")

# Add the Buffer field
print("Adding")
arcpy.AddField_management("RoadsInZip77471", "BuffDist", "FLOAT")
print("Added, calculating")
arcpy.CalculateField_management(in_table="RoadsInZip77471", field="BuffDist", expression="math.pow( !SpeedLimit!, 2 ) * 0.1", expression_type="PYTHON_9.3", code_block="")
print("Calculated")

# Create the buffer
print("Buffering")
arcpy.Buffer_analysis("RoadsInZip77471", "RoadsInZip77471_Buffer", "BuffDist")
print("Buffered")
# Delete the variables
del workspace_path, zip_shape, fbc_roads, scratch_ws, select_zip, zip, zip_query
