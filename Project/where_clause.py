import arcpy


arcpy.env.workspace = r'C:\Users\avenneman\Documents\Programming\SelectWork\Features.gdb'

def build_where_clause(table, field, value):
    field_delimited = arcpy.AddFieldDelimiters(table, field)
    fieldType = arcpy.ListFields(table, field)[0].type
    if str(fieldType) == 'String':
        value = "'%s'" % value
    whereClause = "%s = %s" % (field_delimited, value)
    return whereClause

if __name__ == "__main__":
    subdiv = r'Subdivisions_Res'
    output = r'Subdivisions_Res_Copy4'
    fieldname = "NAME_SEC"
    fieldvalue = "ELDRIDGE LAKE SECTION 2"
    if not arcpy.Exists(output):
        print("Creating new file")
        whereclause = build_where_clause(subdiv, fieldname, fieldvalue)
        arcpy.Select_analysis(subdiv, output, whereclause)
    else:
        print("Already exists")
