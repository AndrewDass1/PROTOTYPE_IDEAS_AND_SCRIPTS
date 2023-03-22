import subprocess

string = "WMIC PATH Win32_Battery Get EstimatedChargeRemaining"

battery_percent_bytes = subprocess.check_output(string, shell=True)

decode_battery_percent = battery_percent_bytes.decode()

# Index 29-31 give battery percentage
# increment = 0
# for i in decode_battery_percent:
	# print("Index " + str(increment) + ": " + decode_battery_percent[increment])
	# increment += 1

index29 = decode_battery_percent[29]

if decode_battery_percent[30] == "0" or decode_battery_percent[30] == "1" or decode_battery_percent[30] == "2" or decode_battery_percent[30] == "3" or decode_battery_percent[30] == "4" or decode_battery_percent[30] == "5" or decode_battery_percent[30] == "6" or decode_battery_percent[30] == "7" or decode_battery_percent[30] == "8" or decode_battery_percent[30] == "9":
	current_battery_percentage = index29 + decode_battery_percent[30]
else:
	current_battery_percentage = index29

if decode_battery_percent[31] == "0":
	current_battery_percentage = index29 + decode_battery_percent[30] + decode_battery_percent[31]
else:
	current_battery_percentage = index29 + decode_battery_percent[30]

print(current_battery_percentage)
