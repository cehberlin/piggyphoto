from __future__ import print_function
import piggyphoto as pp

cam = pp.Camera()

cc = cam.config
ap = cc.get_child_by_name("aperture")
print(ap.choices)
print(ap.value)

cam.close()
