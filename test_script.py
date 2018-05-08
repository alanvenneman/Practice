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

def compare_fields(join_table, subdivision_psn, utility):
    import arcpy


    s_cursor = arcpy.SearchCursor(join_table)
    s_row = s_cursor.next()
    while s_row:
        if s_row.getValue(subdivision_psn) != s_row.getValue("PROJECT_SERIAL_NUMBER_1") and s_row.getValue("Join_Count") == 1:
            target_id = s_row.getValue("TARGET_FID")
            suggested_psn = s_row.getValue(subdivision_psn)


            u_cursor = arcpy.UpdateCursor(utility)
            row = u_cursor.next()
            while row:
                if row.getValue("OBJECTID") == target_id:
                    row.setValue("SUGGESTED_PROJECT_SERIAL_NUMBER", suggested_psn)
                    u_cursor.updateRow(row)
                    print("row updated")
                row = u_cursor.next()
                # print(f"Current row: {row}")
            del row
        s_row = s_cursor.next()
    del s_row


def clean_up(file):
    import arcpy

    arcpy.env.workspace = "C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb"
    arcpy.Delete_management(file)

feature = os.path.join("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb", "ArcSDE_SDE_sGravityMain")
subdivision_join = os.path.join("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb", "spatial_joined")

copy_feature_class("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\",
                   "Features.gdb",
                   "Scratch.gdb",
                   "polygon")
compare_fields(subdivision_join, "Project_Serial_Number", feature)

delete = input("Undo? Y/N\n")
if delete == 'Y' or delete == 'y':
    shutil.rmtree("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Scratch.gdb")
    clean_up("spatial_joined")
