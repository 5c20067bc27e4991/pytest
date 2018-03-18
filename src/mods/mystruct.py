import struct

values = (12, 'abc'.encode(), 2.5)
s = struct.Struct('i3sf')
pack_data = s.pack(*values)
unpack_data = s.unpack(pack_data)

print(pack_data)
print(unpack_data)