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

#for num in range(2,11):
#    bpy.ops.blensor.delete_scans();
#    bpy.ops.blensor.scan();

for num in range(2,51):  # 假设循环范围为0到9
    filepath = f"/home/dev/Public/Experiments/ex4/B2/0deg/noisy/B2_5m_x0y0z0_cam_x0y0z2_noisy_{num-1}.ply"  # 拼接文件路径
    meshname = f"NoisyScan.{num:03d}"
    savePLYFile(filepath, meshname)

