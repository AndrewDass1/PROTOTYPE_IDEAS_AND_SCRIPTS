#!/bin/bash

echo "$Enter 'true' or 'false' respectively to either activate or deactivate the Night Light feature"
read true_false_option

if [ $true_false_option == "true" ]; 
then
	echo "Night Light is activated."
	activate_night_light=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true)

	echo "Next, enter a number from 10000 to 1000 to change the night light temperature (Lowest Value: 10000, Highest Value: 1000. Going below or above the threshold disables night light.):"
	read color_temp_number

	color_temperature=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-temperature $color_temp_number)

	echo "Enter a time to begin the night light:"
	read first_time
	start_time=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-schedule-from $first_time)

	echo "Enter a time to end the night light:"
	read second_time
	end_time=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-schedule-to $second_time)


elif [ $true_false_option == "false" ];
then
	echo "Night Light is deactivated."
	deactivate_night_light=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false)
	echo $deactivate_night_light
else
	echo "Invalid response. Run the script again."
fi
