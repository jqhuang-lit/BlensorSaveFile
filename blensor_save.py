import bpy
import math
from numpy import arange
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *
import blensor

"""clear the scanning in view windows and start newly scan"""
#bpy.ops.blensor.delete_scans(); 
#bpy.ops.blensor.scan();

def savePCDFile(filepath, meshname):
    f=open(filepath,"w") 
    i = 0; 
    for item in bpy.data.objects:
        if item.type == 'MESH' and item.name.startswith(meshname):
            print('write once')
            for sp in item.data.vertices:
                #print('X=%+#5.3f\tY=%+#5.3f\tZ=%+#5.3f' % (sp.co[0], sp.co[1],sp.co[2]));
                str='%#5.3f\t%#5.3f\t%#5.3f \n' % (sp.co[0], sp.co[1],sp.co[2]);
                i = i+1;
                f.write(str);  
    f.close() 
    f=open(filepath,"r+")
    header = ("# .PCD v0.7 - Point Cloud Data file format\nVERSION 0.7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH %d\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS %d\nDATA ascii\n" %(i,i))
    data = f.read()
    f.seek(0)
    f.write(header)
    f.write(data)
    
def savePLYFile(filepath, meshname):
    f=open(filepath,"w") 
    i = 0; 
    for item in bpy.data.objects:
        if item.type == 'MESH' and item.name.startswith(meshname):
            print('write once')
            for sp in item.data.vertices:
                #print('X=%+#5.3f\tY=%+#5.3f\tZ=%+#5.3f' % (sp.co[0], sp.co[1],sp.co[2]));
                str='%#5.3f\t%#5.3f\t%#5.3f \n' % (sp.co[0], sp.co[1],sp.co[2]);
                i = i+1;
                f.write(str);  
    f.close() 
    f=open(filepath,"r+")
    header = ("ply\nformat ascii 1.0\ncomment Created by Blensor\nelement vertex %d\nproperty float x\nproperty float y\nproperty float z\nend_header\n" %(i))
    data = f.read()
    f.seek(0)
    f.write(header)
    f.write(data)



isdelete = 0
isscan = 0
issave = 0
mode = "continues"

if(isdelete):   
    for num in range(0,154):
        bpy.ops.blensor.delete_scans();
  
if(isscan):
    for num in range(0,12):
        bpy.ops.blensor.scan();
  
if(issave):    
    for num in range(2,12):
        filepath = f"D:/dataset/CameraPose_x5y5z95_{num-1}.ply"
        meshname = f"Scan.{num:03d}"  
        savePLYFile(filepath, meshname)

if(mode == "continues"):
    bpy.ops.blensor.scan();
    bpy.ops.blensor.scan();
    euler_0 = 0.0
    euler_total = 90
    num_frames = 100
    for num in range(2,2+num_frames):  #2-153
        bpy.ops.blensor.scan();
    
        euler_0_angle = euler_0/pi*180
        filepath = f"D:/dataset/CameraPose_x5y5z95_ModelPose_x0y10z{-euler_0_angle:3f}_{num-1}.ply"
        meshname = f"Scan.{num:03d}"
        savePLYFile(filepath, meshname)
        
        euler_0 = euler_0 - (euler_total / num_frames)/180*pi
        for i in bpy.context.visible_objects:
            if i.name == "C919":           
                bpy.data.objects["C919"].rotation_euler[2] = euler_0   
      
    