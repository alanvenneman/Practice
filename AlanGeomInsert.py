# AlanGeomInsert.py
# Author: Alan Venneman
# Date: December 19, 2018
# Purpose: Uses ArcPy Insert Cursor to add a new well using the Shape field and to get the geometry of the feature class table.
# Inputs: ProposedWells.shp
# Outputs: None
##################################################
print("-" * 30)

# import arcpy, license
import arcinfo
import arcpy

# Set workspace
arcpy.env.workspace = r"C:\Student\ICTPythonGIS\Data\Texas"

user_answer = 'Y'

while user_answer == 'Y' or user_answer == 'y':
    # Create prompt for Long and Lat
    insert_lon = float(raw_input("Enter Longitude - probably will begin with a '-': "))
    insert_lat = float(raw_input("Enter Latitude - probably will be positive: "))

    # Build insert cursor
    table = "Proposed_Wells.shp"
    field_list = ["SHAPE@XY"]
    well_count = 0
    i_cursor = arcpy.da.InsertCursor(table, field_list)
    i_cursor.insertRow(((insert_lon, insert_lat), ))
    del i_cursor
    print("Row added at {}, {}".format(insert_lon, insert_lat))
    user_answer = raw_input("Add another well? Y/N: ")
with arcpy.da.SearchCursor(table, field_list) as s_cursor:
    for s_row in s_cursor:
        well_count += 1
        print("Well number {}: {}, {}".format(well_count, s_row[0][0], s_row[0][1]))
    print("Total rows: {}").format(well_count)

# Step through cursor and print the x,y coordinate

# Print total count of proposed wells

# Delete Variables
del table, field_list, well_count, insert_lon, insert_lat, s_cursor, s_row, user_answer
