import arcpy
import os
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
            displayName="Output Joined Feature",
            name="output_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Output")

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

    def copy_subdivision_add_field(self, polygon):
        arcpy.env.overwriteOutput = True
        original = r"C:\Users\avenneman\Documents\Programming\SelectWork\output.gdb"
        polygon_copy = os.path.join(polygon, original)
        # layer = arcpy.MakeFeatureLayer_management(polygon, "polygon_layer")
        arcpy.Copy_management(polygon, polygon_copy)
        arcpy.AddField_management(polygon_copy, "PSN_COPY", "TEXT")
        arcpy.CalculateField_management(polygon_copy, "PSN_COPY", "!PROJECT_SERIAL_NUMBER!", "PYTHON3")
        return polygon_copy

    def point_in_polygon_spatial_join(self, utility, polygon_copy, output):
        # take care of the field mapping first
        field_mappings = arcpy.FieldMappings()
        field_mappings.addTable(utility)
        field_mappings.addTable(polygon_copy)

        arcpy.SpatialJoin_analysis(utility,
                                   polygon_copy,
                                   output,
                                   "JOIN_ONE_TO_MANY",
                                   "KEEP_ALL",
                                   field_mappings,
                                   "HAVE_THEIR_CENTER_IN")
        arcpy.Delete_management(polygon_copy)
        return output

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
        output_feature = parameters[3].valueAsText

        if int(arcpy.GetCount_management(utility_features)[0]) == 0:
            messages.addErrorMessage(f"{utility_features} has no features")
        polygon_copy = ProjectIDTool.copy_subdivision_add_field(self, subdivision_feature)
        joined_feature = ProjectIDTool.point_in_polygon_spatial_join(self,
                                                                     utility_features,
                                                                     polygon_copy,
                                                                     output_feature)
        fields = arcpy.ListFields(joined_feature)
        for field in fields:
            if field.name == project_serial_number_field:
                arcpy.AddMessage("true")

        return
