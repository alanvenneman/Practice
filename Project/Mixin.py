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

    def listGeneration(self, listlength, upperbound):
        import random

        p = 0
        li = []
        while p <= listlength:
            li.append(random.randint(1, upperbound))
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
        arcpy.SpatialJoin_analysis(utility, polygon, output, "#", "#", "#", "HAVE_THEIR_CENTER_IN")
        return output

    def compare_fields(self, utility, field):
        import arcpy
        if field not in utility:
            arcpy.AddField_management(utility, field_name="SUGGESTED_PROJECT_SERIAL_NUMBER", field_type="TEXT")
