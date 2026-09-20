import psutil 
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory= psutil.virtual_memory()
    print("Inside function: memory checked")
    return memory.percent

def get_disk_usage():
    disk=psutil.disk_usage("C:\\")
    return disk.percent

def get_system_status():
    cpu_usage=get_cpu_usage()
    memory_usage= get_memory_usage()
    disk_usage= get_disk_usage()


    return {
        "cpu_usage": cpu_usage,
        "memory_usage" : memory_usage,
        "disk_usage" :disk_usage
    }



system_status = get_system_status()
print("Disk usage is :", system_status["disk_usage"],"%")

if(system_status["disk_usage"]>90):
    print("CRITICAL: Disk usage is too high!")
else:
    print("Disk usage is normal.")
