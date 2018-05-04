import shutil
import os


def create_gdb_in_new_folder(path, gdb_name):
    import arcpy
    import pathlib
    import sys

    new_path = pathlib.Path(path)

    if not pathlib.Path.exists(new_path):
        pathlib.Path(new_path).mkdir(parents=True, exist_ok=True)

    try:
        arcpy.env.workspace = str(new_path)
        arcpy.env.overwriteOutput = True
        arcpy.CreateFileGDB_management(str(new_path), gdb_name)
    except Exception:
        e = sys.exc_info()[1]
        print(e.args[0])
        arcpy.AddError(e.args[0])


def copy_feature_class(path, gdb_name, scratch_gdb, feature_type):
    import arcpy
    import os

    arcpy.env.workspace = os.path.join(path, gdb_name)
    arcpy.CreateFileGDB_management(path, scratch_gdb)
    fclist = arcpy.ListFeatureClasses("*", feature_type)

    for fc in fclist:
        fcdesc = arcpy.Describe(fc)
        copied_feature = f"{path}\\{scratch_gdb}\\{fcdesc.basename}"
        poop = arcpy.CopyFeatures_management(fc, copied_feature)
        arcpy.AddField_management(poop, "PSN_COPY", "TEXT")
        arcpy.CalculateField_management(poop, "PSN_COPY", "!PROJECT_SERIAL_NUMBER!", "PYTHON3")
        arcpy.SpatialJoin_analysis(os.path.join(path + gdb_name, "ArcSDE_SDE_sGravityMain"),
                                   poop,
                                   "spatial_joined",
                                   "JOIN_ONE_TO_MANY",
                                   "KEEP_ALL",
                                   "",
                                   "HAVE_THEIR_CENTER_IN")
        return poop

def compare_fields(utility, psn_field, suggested_field):
    import arcpy

    # if suggested_field not in utility:
    #     arcpy.AddField_management(utility, field_name=suggested_field, field_type="TEXT")
    #     arcpy.AddMessage("SUGGESTED_PROJECT_SERIAL_NUMBER added to feature class.")
    cursor = arcpy.da.UpdateCursor(utility, [psn_field, suggested_field])
    row = cursor.next()
    while row:
        if row.getValue(psn_field) != row.getValue("PSN_COPY"):
            row.setValue(suggested_field, row.getValue("PSN_COPY"))
            cursor.updateRow(row)
        row = cursor.next()
    del row


def clean_up(file):
    import arcpy

    arcpy.env.workspace = "C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb"
    arcpy.Delete_management(file)

feature = os.path.join("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb", "ArcSDE_SDE_sGravityMain")

copy_feature_class("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\",
                   "Features.gdb",
                   "Scratch.gdb",
                   "polygon")
compare_fields(feature, "Project_Serial_Number", "SUGGESTED_PROJECT_SERIAL_NUMBER")

delete = input("Undo? Y/N\n")
if delete == 'Y' or delete == 'y':
    shutil.rmtree("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Scratch.gdb")
    clean_up("spatial_joined")
