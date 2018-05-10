import arcpy
import os
import time


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "QAQC"
        self.alias = "QAQC"
        # List of tool classes associated with this toolbox
        self.tools = [ProjectIDTool]


class ProjectIDTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Project Serial Number QA/QC Tool"
        self.description = "Creates a column in the feature class that suggests the Project Serial Number determined" \
                           "by the tool's algorithm."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input Feature",
            name="utility_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="Project Serial Number Source Feature",
            name="subdivision_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        param2 = arcpy.Parameter(
            displayName="Workspace",
            name="database",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        param3 = arcpy.Parameter(
            displayName="Output Joined Feature",
            name="output_feature",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")
        param3.parameterDependencies = [param0.name]

        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def copy_feature_class(self, path, gdb_name, subdivision, utility):
        import os

        arcpy.env.workspace = os.path.join(path, gdb_name)
        arcpy.SpatialJoin_analysis(utility,
                                   subdivision,
                                   "spatial_joined",
                                   "JOIN_ONE_TO_MANY",
                                   "KEEP_ALL",
                                   "",
                                   "HAVE_THEIR_CENTER_IN")
        spatial_output = os.path.join(f"{path}\\{gdb_name}", "spatial_joined")
        return spatial_output

    def compare_fields(self, join_table, utility):
        import arcpy
        import time

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
                        localtime = time.asctime(time.localtime(time.time()))
                        print(f"row updated for {target_id} at {localtime}")
                    row = u_cursor.next()
                del row
            s_row = s_cursor.next()
        del s_row

    def execute(self, parameters, messages):
        """The source code of the tool."""
        xutility_features = parameters[0].valueAsText
        xsubdivision_feature = parameters[1].valueAsText
        xdatabase = parameters[2].valueAsText
        xoutput_feature = parameters[3].valueAsText

        utility_features = os.path.join("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb",
                                        "dGravityMain")
        database = "C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb"
        output_feature = os.path.join("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb",
                                      "dGravityMain")
        subdivision_feature = os.path.join("C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\Features.gdb",
                                           "Subdivisions_Res")

        if int(arcpy.GetCount_management(utility_features)[0]) == 0:
            messages.addErrorMessage(f"{utility_features} has no features")
        path = os.path.dirname(database)
        gdb_name = os.path.basename(database)
        joined_feature = ProjectIDTool.copy_feature_class(self,
                                                          path,
                                                          gdb_name,
                                                          subdivision_feature,
                                                          utility_features)

        ProjectIDTool.compare_fields(self, joined_feature, utility_features)
        endtime = time.asctime(time.localtime(time.time()))
        print(endtime)

        return output_feature


def main():
    tbx = Toolbox()
    tool = ProjectIDTool()
    tool.execute(tool.getParameterInfo(), None)


if __name__ == "__main__":
    main()
