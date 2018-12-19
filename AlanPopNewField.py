# AlanPopNewField.py
# Author: Alan Venneman
# Date: December 19, 2018
# Purpose: Demonstrate a custom tool in ArcToolbox that asks the user for
# specific values from a table, feeds the information into a new field,
# which can then be used to label the features.
# Inputs: inputTable = User input table
# strExp = SQL query
# newField = Name of field to create
# fieldOne = 1st field to pull data from
# fieldTwo = 2nd field to pull data from
# separator = Character to use as a separator
# Outputs: Updated table with new field populated with a specified value.
# ##################################################
print("-" * 30)

# import arcpy, license
import arcinfo
import arcpy
import sys

# Get user input

input_table = sys.argv[1]
sql_expression = sys.argv[2]
new_field = sys.argv[3]
field_one = sys.argv[4]
field_two =  sys.argv[5]
separator = sys.argv[6]

##input_table = r"C:\Student\ICTPythonGIS\Data\Texas\NWHouston.dbf"
##sql_expression = "PRICESQFT > 0"
##new_field = "PriceSize"
##field_one = "PRICESQFT"
##field_two = "SQFT"
##separator = " psf/Size: "

# Add a field to table
try:
    arcpy.AddField_management(input_table, new_field, "TEXT", "", "", 50, "PriceSize")

    # Create an update cursor to add data to new field
    field_list = [new_field, field_one, field_two]
    with arcpy.da.UpdateCursor(input_table, field_list, sql_expression) as u_cursor:
        for u_row in u_cursor:
            u_row[0] = "{}{}{}".format(u_row[1], separator, u_row[2])
            u_cursor.updateRow(u_row)
##            print(u_row[0])
except RuntimeError as e:
    arcpy.GetMessage(2)
    print(e)

# Print message confirming success
print("New field populated: {}".format(new_field))
# Delete variables
del input_table, sql_expression, new_field, field_one, field_two, separator, field_list, u_row, u_cursor
