import psutil 
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory= psutil.virtual_memory()
    
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




