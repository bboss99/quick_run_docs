import bpy

def makeSpline(cu, typ, points):
    spline = cu.splines.new(typ)
    npoints = len(points)
    
    if typ == 'BEZIER' or typ == 'BSPLINE':
        spline.bezier_points.add(npoints-1)
        for (n,pt) in enumerate(points):
            bez = spline.bezier_points[n]
            (bez.co, bez.handle1, bez.handle1_type, bez.handle2, bez.handle2_type) = pt
    else:
        spline.points.add(npoints-1)    # One point already exists?
        for (n,pt) in enumerate(points):
            spline.points[n].co = pt
        
    return
    
cu = bpy.data.curves.new("MyCurve", "CURVE")
ob = bpy.data.objects.new("MyCurveObject", cu)
scn = bpy.context.scene
scn.objects.link(ob)
scn.objects.active = ob

cu.dimensions = "3D"

makeSpline(cu, "NURBS", [(0,0,0,1), (0,0,1,1), (0,1,1,1), (1,4,1,1)] )
makeSpline(cu, "NURBS", [(1,0,0,1), (1,0,1,1), (1,2,1,1), (1,4,1,1)] )
makeSpline(cu, "NURBS", [(2,1,0,1), (2,1,1,1), (2,3,1,1), (1,4,1,1)] )