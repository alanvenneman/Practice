# AlanUpdateCursor.py
# Author: Alan Venneman
# Date: December 19, 2018
# Purpose: Uses ArcPy Update Cursor to update the NWHouston table to include price per square foot.
# Inputs: NWHouston.dbf
# Outputs: None
##################################################
print("-" * 30)

# import arcpy, license
import arcinfo
import arcpy

# Set workspace
arcpy.env.workspace = r"C:\Student\ICTPythonGIS\Data\Texas"

# Set variables
table = "NWHouston.dbf"
field_list = ["ZIP_CODE", "ADDRESS", "SQFT", "PRICESQFT", "SOLDPRICE"]
where_clause = "\"ZIP_CODE\" = 77423"
record_count = 0

# Build update cursor
with arcpy.da.UpdateCursor(table, field_list, where_clause) as u_cursor:
    for u_row in u_cursor:
        # Print total record count
        record_count += 1
        # Do calculation to determine PPSQFT
        u_row[3] = u_row[4] / u_row[2]
        u_cursor.updateRow(u_row)
        # Use cursor to print out ADDRESS, SOLDPRICE, SQFT, and PRICESQFT rows
        print("Record #{}: The {} square foot building at {} sold at ${}, which is ${} per square foot.".format(record_count, u_row[2], u_row[1], u_row[4], round(u_row[3], 2)))
        
# Delete Variables
del table, field_list, where_clause, record_count, u_cursor, u_row
