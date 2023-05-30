#!/bin/bash

echo "$Enter 'true' or 'false' respectively to either activate or deactivate the Night Light feature"
read true_false_option



if [ $true_false_option == "true" ]; 
then
	echo "Night Light is activated"
	activate_night_light=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true)

	if [  ]
elif [ $true_false_option == "false" ];
then
	echo "Night Light is deactivated."
	deactivate_night_light=$(gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false)
	echo $deactivate_night_light
else
	echo "Invalid response. Run the script again."
fi
