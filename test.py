import ctypes
import time
import psutil, os

p = psutil.Process( os.getpid() )
for dll in p.memory_maps():
  print(dll.path)



hwnd = ctypes.windll.user32.GetForegroundWindow()
lpdw_process_id = ctypes.c_ulong()
result = ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdw_process_id))
process_id = lpdw_process_id.value
print(process_id)