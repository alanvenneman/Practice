class Mixin(object):
    pass

    def binarySearch(self, list1, key):
        low = 0
        high = len(list1) - 1

        while high >= low:
            mid = (low + high) // 2
            if key < list1[mid]:
                high = mid - 1
            elif key == list1[mid]:
                return mid
            else:
                low = mid + 1

        return -low - 1

    def insertion_sort(self, sort):
        for i in range(1, len(sort)):
            current_element = sort[i]
            k = i - 1
            while k >= 0 and sort[k] > current_element:
                sort[k + 1] = sort[k]
                k -= 1

            sort[k + 1] = current_element
        return sort

    def listGeneration(self, list_length, upper_bound):
        import random

        p = 0
        li = []
        while p <= list_length:
            li.append(random.randint(1, upper_bound))
            p += 1
        return li

    def build_where_clause(self, table, field, value):
        import arcpy

        field_delimited = arcpy.AddFieldDelimiters(table, field)
        field_type = arcpy.ListFields(table, field)[0].type
        if str(field_type) == 'String':
            value = "'%s'" % value
        where_clause = "%s = %s" % (field_delimited, value)
        return where_clause

    def point_in_polygon_spatial_join(self, utility, polygon, output):
        import arcpy

        # take care of the field mapping first
        field_mappings = arcpy.FieldMappings()
        field_mappings.addTable(utility)
        field_mappings.addTable(polygon)

        arcpy.SpatialJoin_analysis(utility,
                                   polygon,
                                   output,
                                   "JOIN_ONE_TO_MANY",
                                   "KEEP_ALL",
                                   field_mappings,
                                   "HAVE_THEIR_CENTER_IN")
        return output

    def compare_fields(self, join_table, utility):
        import arcpy
        import time

        localtime = time.asctime( time.localtime(time.time()) )

        s_cursor = arcpy.SearchCursor(join_table)
        s_row = s_cursor.next()
        while s_row:
            if s_row.getValue("PROJECT_SERIAL_NUMBER_1") != s_row.getValue("PROJECT_SERIAL_NUMBER") and s_row.getValue(
                    "Join_Count") == 1:
                target_id = s_row.getValue("TARGET_FID")
                suggested_psn = s_row.getValue("PROJECT_SERIAL_NUMBER_1")

                u_cursor = arcpy.UpdateCursor(utility)
                row = u_cursor.next()
                while row:
                    if row.getValue("OBJECTID") == target_id:
                        row.setValue("SUGGESTED_PROJECT_SERIAL_NUMBER", suggested_psn)
                        u_cursor.updateRow(row)
                        print(f"row updated for {target_id} at {localtime}")
                    row = u_cursor.next()
                    # print(f"Current row: {row}")
                del row
            s_row = s_cursor.next()
        del s_row

    def create_gdb_in_new_folder(self, path, gdb_name):
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

    def copy_feature_class(self, path, gdb_name, scratch_gdb, feature_type):
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
            arcpy.SpatialJoin_analysis(os.path.join(f"{path}\\{gdb_name}", "ArcSDE_SDE_sGravityMain"),
                                       poop,
                                       "spatial_joined",
                                       "JOIN_ONE_TO_MANY",
                                       "KEEP_ALL",
                                       "",
                                       "HAVE_THEIR_CENTER_IN")
            spatial_output = os.path.join(f"{path}\\{gdb_name}", "spatial_joined")
            return spatial_output
