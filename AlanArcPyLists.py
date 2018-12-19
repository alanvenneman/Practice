# AlanArcPyLists.py
# Author: Alan Venneman
# Date: December 18, 2018
# Purpose: Uses ArcPy list methods to list data frames and layers in a map document.
# Inputs: mxd = map document
# Outputs: None
##################################################
print("-" * 30)

# import modules and correct license
import arcinfo
import arcpy
import os

# Get the map document
path = r"C:\Student\ICTPythonGIS\MapDocuments"
mxd = "FireDistricts.mxd"
## mxd = raw_input("Enter an mxd: ")
#while 
## if arcpy.Exists(mxd):
##  print("MXD found")
## else:
##  arcpy.AddError("MXD not found.")
##  mxd = raw_input("Enter an mxd: ")
arcpy.env.workspace = path
full_mxd_path = os.path.join(path, mxd)

# Print the map document properties
mxd_object = arcpy.mapping.MapDocument(full_mxd_path)
print("Title: {}".format(mxd_object.title))
print("Author: {}".format(mxd_object.author))
print("Summary: {}".format(mxd_object.summary))
print("Date Saved: {}".format(mxd_object.dateSaved))

# Loop through the data frames and properties
list_df = arcpy.mapping.ListDataFrames(mxd_object)
for d in list_df:
    print("Data frame: {}".format(d.name))
    print("\tExtent: {}".format(d.extent))
    print("\tMap Units: {}".format(d.mapUnits))
    print("\tScale: {}".format(d.scale))
    print("\tSpatial Reference: {}".format(d.spatialReference))

# Loop through layers and properties
layers = arcpy.mapping.ListLayers(mxd_object)
for l in layers:
    print("Layer: {}".format(l.name))
    if l.isFeatureLayer == True:
        print("\tDefinition Query: {}".format(l.definitionQuery))
        print("\tShow Labels: {}".format(l.showLabels))
    print("\tTransparency: {}".format(l.transparency))
    print("\tVisible: {}".format(l.visible))

# Delete the variables
del layers, list_df, mxd_object, path, mxd, d, l, e
