# AlanSearchCursor.py
# Author: Alan Venneman
# Date: December 19, 2018
# Purpose: Uses ArcPy Search Cursor to Read a table.
# Inputs: a table
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

# Build search cursor
with arcpy.da.SearchCursor(table, field_list, where_clause) as s_cursor:
    for s_row in s_cursor:
        # Print total record count
        record_count += 1
        # Use cursor to print out ADDRESS, SOLDPRICE, SQFT, and PRICESQFT rows
        print("Record #{}: The {} square foot building at {} sold at ${}, which is ${} per square foot.".format(record_count, s_row[2], s_row[1], s_row[4], s_row[3]))
        
# Delete Variables
del table, field_list, where_clause, record_count, s_cursor, s_row
