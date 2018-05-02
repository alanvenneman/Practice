import arcpy


subdiv = r'C:\Users\avenneman\Documents\Programming\SelectWork\Features.gdb\Subdivisions_Res'
mxd = arcpy.mp.ArcGISProject(r"C:\Users\avenneman\Documents\Programming\SelectWork\ProjectSerialNumber\ProjectSerialNumber.aprx")

layout = mxd.listLayouts()
for lm in mxd.listMaps():
    print("Map: " + lm.name)
    for lyr in lm.listLayers():
        print(" " + lyr.name)
# mapframe = layout.listElements("")[0]
#
# print(mapframe.name)
# print(mapframe.map.name)

def create_list():
    file = open("try_it.txt", "w")
    file.write("NAME_SEC = 'ELDRIDGE LAKE SECTION 2'")
    file.close()

def data_frame():
    read = open("try_it.txt", "r")
    sub = read.readline()
    print (sub)
    # wc = "{} = {}".format("NAME_SEC", sub)
    read.close()

    arcpy.SelectLayerByAttribute_management(subdiv, "NEW_SELECTION", sub)

create_list()
data_frame()

del mxd


"""
Idea for class structure

#################################################

class PointInPolygon():
    def __init__(self, s_path, s_main, d_main):
        self.subdivision_feature = s_path
        self.subdivision_copy = sub_copy
        self.sanitary_main = s_main
        self.water_main = w_main
        self.drainage_main = d_main
        # self.proj_serial_num = psn
        # self.field_name = f_name
        # self.suggested_proj_serial_num = sug_psn
        
    def delete():
        arcpy.Delete_management(self.subdivision_copy)
        
    def find_points(feature, path):
        
        
class Sanitary_Updater(Selector):
    def __init__(self, s_path, s_main):
        Selector.__init__(self, s_main):
        
    def update_sanitary(self, s_main):
        pass
        
#################################################

This may not be the most efficient way to do this, but it satisfies the inheritance requirement. I may not need a class
for each of the three features, but I will need the subdivision feature multiple places as will need the three line
features.

I also had ideas for some helper functions to go along with the where_clause maker.

Scratch file keeper/deleter

Add field
Search cursor - finds the PSN
Update cursor - updates the lines with the PSN


"""