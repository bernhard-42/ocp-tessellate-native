from time import time
from ocp_tessellate.ocp_utils import deserialize

import sys
sys.path.append("build")

import ocp_tessellate_native as tess


def decompose(array, indexes, flatten=False):
    result =[]
    s = 0
    for e in indexes:
        e2 = s + e
        sub = array[s:e2]
        if flatten:
            sub = sub.reshape(-1)
        result.append(sub)
        s = e2
    return result

def tessellate(obj, deflection, angular_tolerance, parallel):
    m =  tess.tessellate(obj, deflection, angular_tolerance, parallel, False, True)
    
    t = time()
    tr = decompose(m.triangles.reshape(-1, 3), m.triangles_per_face, True)
    print("Reshape tessellation", int(1000*(time() - t)), "ms")

    t = time()
    sg = decompose(m.segments.reshape(-1, 2, 3), m.segments_per_edge)
    print("Reshape edges", int(1000*(time() - t)), "ms")

    return {
        "vertices": m.vertices,
        "normals": m.normals,
        "triangles": tr,   
        "face_types": m.face_types, 
        "edges": sg,
        "edge_types": m.edge_types,
        "obj_vertices": m.obj_vertices
    }

file, acc, show = "examples/b123.brep", 0.002, True
# file, acc, show = "examples/rc.brep", 0.19, False

with open(file, "rb") as f:
    obj = deserialize(f.read())

tt = time()


mesh = tessellate(obj, acc, 0.3, parallel=True)

import json
if show:
    print("vertices:", mesh["vertices"])
    print("normals:", mesh["normals"])
    print("triangles:")
    for t in mesh["triangles"]:
        print("  ", json.dumps(t.tolist()))
    print("face_types:", mesh["face_types"])
    print("edge_types:", mesh["edge_types"])
    print("edges")
    for e in mesh["edges"]:
        print("  ", json.dumps(e.tolist()))
    print("obj_vertices:", mesh["obj_vertices"])

# print("overall:", int(1000*(time() - tt)), "ms")
