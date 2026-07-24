import platform
import socket

print("Hostname:", socket.gethostname())
print("Operating System:", platform.system())
print("Release:", platform.release())
print("Machine:", platform.machine())
print("Processor:", platform.processor())