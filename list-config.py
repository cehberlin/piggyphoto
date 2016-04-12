from __future__ import print_function
import piggyphoto

C = piggyphoto.Camera()
print(C.abilities)
C.list_config()

C.close()
