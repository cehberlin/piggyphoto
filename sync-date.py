from __future__ import print_function
import piggyphoto

C = piggyphoto.Camera()
print(C.abilities)


# example: setting date manually
cc = C.config
dt = cc.get_child_by_name("datetime")
print(dt.value)
dt.value = 1400000000
C.config = cc
print(dt.value)

# example: date autosync
cc = C.config
syncdate = cc.get_child_by_name("syncdatetime")
syncdate.value = 1
C.config = cc

C.close()
