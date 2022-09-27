# Micmute LED service for pulseaudio (WORK IN PROGRESS)
## Tested on a Huawei matebook 14 AMD 2020 on Kubuntu 20.10, 21.04 and 22.04

## Prerequisites
1. python3
2. gcc
3. pulsectl library (install via pip for root: `sudo -H pip install pulsectl`)
4. systemd (optional)

## Installation
1. Make sure `BRIGHTNESS_FILE_PATH` in set_micmute_led.c corresponds to the LED file path on your system.
2. Make sure `mic_name` in micmute_listener_pa.py corresponds to your mic device name. This name can be found within the sources printed out when the client is started. (This will be made more user-friendly with upcoming releases)
3. Run `./install.sh`

## Running

### With systemd
If you want to enable the script as soon as you log in, run `systemctl --user enable micmute_listener_pa.service`.
To start the service immediately, run `systemctl --user start micmute_listener_pa.service`.

### Without systemd
Simply run `~/.local/bin/micmute_listener_pa.py &` after installation. For starting the client at boot, look up your distro's individual way to achieve this.

## Contributions
I'm very intrested in your opinions in terms of the architecture of this service. If you have suggestions on how to avoid SETUID or make the whole thing cleaner or more secure, please start a discussion!
