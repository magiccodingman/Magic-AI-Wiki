import subprocess
import time
import re
import os

# Set the IPMI command interface credentials and IP
IPMI_IP = "10.26.26.176"
IPMI_USER = "username"
IPMI_PASS = "password"

# Function to set fan speed via IPMI
def set_fan_speed(speed):
    hex_speed = format(min(max(int(speed), 10), 100), 'x')
    command = f"ipmitool -I lanplus -H {IPMI_IP} -U {IPMI_USER} -P {IPMI_PASS} raw 0x30 0x30 0x02 0xff 0x{hex_speed}"
    subprocess.run(command, shell=True)

# Function to get GPU temperatures using nvidia-smi
def get_gpu_temps():
    nvidia_smi_cmd = 'nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader'
    try:
        output = subprocess.check_output(nvidia_smi_cmd, shell=True)
        temps = [int(temp) for temp in output.decode().strip().split('\n')]
        return temps
    except subprocess.CalledProcessError as e:
        print("Failed to get GPU temperatures", e.output)
        return []

# Function to get CPU temperatures using the updated ipmitool command
def get_cpu_temps():
    command = f"ipmitool -I lanplus -H {IPMI_IP} -U {IPMI_USER} -P {IPMI_PASS} sdr type temperature"
    try:
        output = subprocess.check_output(command, shell=True)
        # Extracting only the highest temperature value
        temp_line = subprocess.check_output("awk -F'|' '{print $1, $5}' | sed 's/ degrees C//g' | sort -nk2 | tail -1", input=output, shell=True)
        temp_value = int(re.search(r'\d+', temp_line.decode().strip()).group())
        return [temp_value]  # Return a list with a single value for consistency with the GPU temps function
    except subprocess.CalledProcessError as e:
        print("Failed to get CPU temperatures", e.output)
        return []

# Function to get fan speed via IPMI
def get_fan_speed():
    # Adjust these names based on your system after checking with 'ipmitool sensor'
    fan_sensors = ['Fan1', 'Fan2', 'Fan3']  # Example sensor names
    fan_speeds = []
    for sensor in fan_sensors:
        command = f"ipmitool -I lanplus -H {IPMI_IP} -U {IPMI_USER} -P {IPMI_PASS} sensor get '{sensor}'"
        try:
            output = subprocess.check_output(command, shell=True)
            fan_speed = re.search(r'Sensor Reading\s+:\s+(\d+(\.\d+)?)(\s+RPM)?', output.decode())
            if fan_speed:
                fan_speeds.append(fan_speed.group(1) + " RPM")
        except subprocess.CalledProcessError as e:
            print(f"Failed to get {sensor} speed", e.output)
            fan_speeds.append("Unknown")
    return fan_speeds

# Function to determine fan speed based on temperatures
def determine_fan_speed(gpu_temps, cpu_temps):
    temps = gpu_temps + cpu_temps
    fan_speed = 30  # Default fan speed
    if any(temp > 75 for temp in temps):
        fan_speed = 100
    elif any(temp > 70 for temp in temps):
        fan_speed = 80
    elif any(temp > 65 for temp in temps):
        fan_speed = 70
    elif any(temp > 60 for temp in temps):
        fan_speed = 60
    elif any(temp > 50 for temp in temps):
        fan_speed = 40
    return fan_speed

# Main control function
def control_fan():
    gpu_temps = get_gpu_temps()
    cpu_temps = get_cpu_temps()
    fan_speed = determine_fan_speed(gpu_temps, cpu_temps)
    set_fan_speed(fan_speed)
    current_fan_speeds = get_fan_speed()
    print(f"GPU Temps: {gpu_temps}, Highest CPU Temps: {cpu_temps}, Fan Speed Set To: {fan_speed}%, Current Fan Speeds: {current_fan_speeds}")

# Call the control function every 3 seconds
while True:
    control_fan()
    time.sleep(3)