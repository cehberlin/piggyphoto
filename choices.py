from __future__ import print_function
import piggyphoto as pp

cam = pp.Camera()

print(cam.config.main.capturesettings.shutterspeed.choices)

cam.close()
