#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
proto.insert(0,"Hi")
print(proto)
proto.remove(22)
print(proto)
proto3=proto
print(proto3)
proto3.clear()
print(proto3)
protoa.reverse()
print(list(reversed(protoa)))
#print(protoa)
#print(protoa.count("ssh"))
