# AlanUpdateMapDoc.py
# Author: Alan Venneman
# Date: December 18, 2018
# Purpose: Uses ArcPy to fix the data frames and layers in a map document.
# Inputs: mxd = map document
# Outputs: None
##################################################
print("-" * 30)

# import arcpy and license
import arcinfo
import arcpy
import os

# Get the Map document
path = r"C:\Student\ICTPythonGIS\MapDocuments"
mxd = "Fields.mxd"
full_mxd_path = os.path.join(path, mxd)
arcpy.env.workspace = path
mxd_object = arcpy.mapping.MapDocument(full_mxd_path)
mxd_summary = "Southern LA petroleum"
mxd_description = "Oil and gas fields in southern LA."
mxd_tags = "oil, gas, petroleum, Louisiana, wells"

# Update the map document by setting variables, summary, description and tags.
try:
    print("Setting summary, description and tags.")
    mxd_object.summary = mxd_summary
    mxd_object.description = mxd_description
    mxd_object.tags = mxd_tags
    print("Summary: {}".format(mxd_summary))
    print("Description: {}".format(mxd_description))
    print("Tags: {}".format(mxd_tags))
except:
    print(arcpy.GetMessages(2))

# Get Map Layers
well_layer_object = arcpy.mapping.ListLayers(mxd_object, "*Wells*")[0]
well_layer_name = "Wells"
well_layer_path = r"C:\Student\ICTPythonGIS\Data\Louisiana.gdb"
## well_layer_source = os.path.join(well_layer_path, well_layer_name)
well_layer_scale = 2000000
## print(well_layer_object.name)

# Find the MMSWells layer
try:
    print("Setting name, source and minimum scale for Wells Layer.")
    # Set source using replaceDataSource
    well_layer_object.replaceDataSource(well_layer_path, "FILEGDB_WORKSPACE", "Wells")
    ## well_layer_object.dataSource = well_layer_source - This doesn't seem to work
    print(well_layer_object.dataSource)

    # Change the layer name to Wells using name.
    well_layer_object.name = well_layer_name

    # Set minimum scale dependency to 2,000,000 using minScale
    well_layer_object.minScale = well_layer_scale
    

    # Print attributes
    print("Layer Name: {}".format(well_layer_name))
    print("Layer Source: {}".format(well_layer_object.dataSource))
    print("Layer Scale: {}".format(well_layer_scale))
except:
    print(arcpy.GetMessages(2))

# Save the changes
mxd_object.save()

# Delete variables
del path, mxd, full_mxd_path, mxd_object, mxd_summary, mxd_description, mxd_tags
del well_layer_object, well_layer_name, well_layer_scale, well_layer_path
