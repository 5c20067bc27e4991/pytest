import struct

values = (12, 'abc'.encode(), 2.5)
# s = struct.Struct('i3sf')
# pack_data = s.pack(*values)
# unpack_data = s.unpack(pack_data)

pack_data = struct.pack('i3sf', *values)
unpack_data = struct.unpack('i3sf',pack_data)

print(pack_data)
print(unpack_data)
print(struct.calcsize('128s'))