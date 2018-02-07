import arcpy
import os


environment = r'C:\EsriTraining\RegressionPro\regression.gdb'
feature_class = 'CallPredictionsFY'
output = os.path.join(environment, 'area_stats')
# Not entirely sure that this creates a new feature class or not.
arcpy.CalculateAreas_stats(feature_class, output)
