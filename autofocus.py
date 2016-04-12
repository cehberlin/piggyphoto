from __future__ import print_function
import piggyphoto

C = piggyphoto.Camera()
print(C.abilities)


# example: setting date manually
cc = C.config
af = cc.get_child_by_name("autofocusdrive")
af.value = 1
C.config = cc

C.close()
