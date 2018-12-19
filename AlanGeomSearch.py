# AlanGeomSearch.py
# Author: Alan Venneman
# Date: December 19, 2018
# Purpose: Uses ArcPy Search Cursor to access the Shape field and to get the geometry of the feature class table.
# Inputs: ProposedWells.shp
# Outputs: None
##################################################
print("-" * 30)

# import arcpy, license
import arcinfo
import arcpy

# Set workspace
arcpy.env.workspace = r"C:\Student\ICTPythonGIS\Data\Texas"

# Build search cursor
table = "Proposed_Wells.shp"
field_list = ["SHAPE@XY"]
well_count = 0
with arcpy.da.SearchCursor(table, field_list) as s_cursor:
    for s_row in s_cursor:
        well_count += 1
        print("Well number {}: {}, {}".format(well_count, s_row[0][0], s_row[0][1]))
    print("Totat rows: {}").format(well_count)

# Step through cursor and print the x,y coordinate

# Print total count of proposed wells

# Delete Variables
del s_row, s_cursor, table, field_list, well_count
