import arcpy
# import os
# from module.Mixin import Mixin
# import importlib
# importlib.reload(Mixin)


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "QAQC"
        self.alias = "QAQC"
        # List of tool classes associated with this toolbox
        self.tools = [ProjectIDTool]


class ProjectIDTool(object): #, Mixin):
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
            displayName="Project Serial Number Field",
            name="psn_field",
            datatype="Field",
            parameterType="Required",
            direction="Input")
        param2.parameterDependencies = [param1.name]

        param3 = arcpy.Parameter(
            displayName="Workspace",
            name="database",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        param4 = arcpy.Parameter(
            displayName="Output Joined Feature",
            name="output_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Output")

        params = [param0, param1, param2, param3, param4]
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

    def copy_feature_class(self, path, gdb_name, scratch_gdb, feature_type):
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

    # def compare_fields(self, utility, field):
    #     if field not in utility:
    #         arcpy.AddField_management(utility, field_name="SUGGESTED_PROJECT_SERIAL_NUMBER", field_type="TEXT")
    #         arcpy.AddMessage("SUGGESTED_PROJECT_SERIAL_NUMBER added to feature class.")
    #     cursor = arcpy.da.SearchCursor()

    def execute(self, parameters, messages):
        """The source code of the tool."""
        utility_features = parameters[0].valueAsText
        subdivision_feature = parameters[1].valueAsText
        project_serial_number_field = parameters[2].valueAsText
        database = parameters[3].valueAsText
        output_feature = parameters[4].valueAsText

        if int(arcpy.GetCount_management(utility_features)[0]) == 0:
            messages.addErrorMessage(f"{utility_features} has no features")
        joined_feature = ProjectIDTool.copy_feature_class(self,
                                                          "C:\\Users\\avenneman\\Documents\\Programming\\SelectWork\\",
                                                          "Features.gdb",
                                                          "scratch.gdb",
                                                          "polygon")

        fields = arcpy.ListFields(joined_feature)
        for field in fields:
            if field.name == project_serial_number_field:
                arcpy.AddMessage("true")

        return
