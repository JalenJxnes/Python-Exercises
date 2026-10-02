import psutil
import time

# Define CPU, Memory, Disk Usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent


# Analyze saturation
def analyze_saturation(cpu_threshold = 80, memory_threshold = 80, disk_threshold = 80):
    # Create metric variables
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()

    print("CPU Usage:", cpu_usage)
    print("Memory Usage:", memory_usage)
    print("Disk Usage:", disk_usage)

    # Check if monitors are above stated limits
    if cpu_usage > cpu_threshold or memory_usage > memory_threshold or disk_usage > disk_threshold:
        print("System is saturated. Take action now.")
    else:
        print("System is optimal. No action needed.")

if __name__ == "__main__":
    while True:
        analyze_saturation()
        time.sleep(5)