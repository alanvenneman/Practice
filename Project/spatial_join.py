import arcpy
import os


workspace = r"C:\Users\avenneman\Documents\Programming\SelectWork\Features.gdb"
output = r"C:\Users\avenneman\Documents\Programming\SelectWork\output.gdb"

joinFeatures = os.path.join(workspace, "Subdivisions_Res")
drainageFeatures = os.path.join(workspace, "dGravityMain")
waterFeatures = os.path.join(workspace, "ArcSDE_SDE_wPressurizedMain_2018")
sanitaryFeatures = os.path.join(workspace, "ArcSDE_SDE_sGravityMain")

drain_outfc = os.path.join(output, "JoinedDrainFC")
water_outfc = os.path.join(output, "JoinedWaterFC")
sanitary_outfc = os.path.join(output, "JoinedSanitaryFC")

arcpy.SpatialJoin_analysis(drainageFeatures, joinFeatures, drain_outfc, "#", "#", "#", "HAVE_THEIR_CENTER_IN")
arcpy.SpatialJoin_analysis(waterFeatures, joinFeatures, water_outfc, "#", "#", "#", "HAVE_THEIR_CENTER_IN")
arcpy.SpatialJoin_analysis(sanitaryFeatures, joinFeatures, sanitary_outfc, "#", "#", "#", "HAVE_THEIR_CENTER_IN")
select_statement = "SUBDIV IS NOT NULL AND Project_Serial_Number <> ''"
