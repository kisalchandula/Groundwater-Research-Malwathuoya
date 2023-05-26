import os
import arcpy
from arcpy import env

# get user inputs
in_ws = arcpy.GetParameterAsText(0)
out_p = arcpy.GetParameterAsText(1)
in_zvalue = arcpy.GetParameterAsText(2)
in_mask = arcpy.GetParameterAsText(3)
in_extent = arcpy.GetParameterAsText(4)
in_point = arcpy.GetParameterAsText(5)
out_table = arcpy.GetParameterAsText(6)

# set workspace and output path
arcpy.env.workspace = in_ws
out_folder = f"{out_p}/"

fcs = arcpy.ListFeatureClasses('*', 'Point')

# loop for iterative interpolation
for fc in fcs:
    with arcpy.EnvManager(extent=in_extent, mask=in_mask):
        out = arcpy.sa.Idw(fc, z_field=in_zvalue, cell_size="3.26773613823798E-03", power=1,
                           search_radius="VARIABLE 12",
                           in_barrier_polyline_features="")
        out.save(os.path.join(out_folder, fc + '.tif'))

arcpy.env.workspace = out_folder
rst_names = arcpy.ListRasters("*", "TIF")

paths = []
# loop for create Raster paths
for n in rst_names:
    path = f"{out_folder}{n}"
    paths.append(path)

# loop for create Raster objects
rst = []
for name in paths:
    r = arcpy.Raster(name)
    rst.append(r)

# Extract point location values from rasters as table
arcpy.ExtractValuesToTable_ga(in_point, rst, out_table)
