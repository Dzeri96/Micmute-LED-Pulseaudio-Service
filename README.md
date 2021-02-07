# Micmute LED service for pulseaudio (WORK IN PROGRESS)
## Tested on a Huawei matebook 14 AMD 2020 on Kubuntu 20.10

## Prerequisites
1. python3
2. gcc
3. pulsectl library (install via pip for root: `sudo -H pip install pulsectl`)
4. systemd (optional)

## Installation
1. Make sure `BRIGHTNESS_FILE_PATH` in set_micmute_led.c corresponds to the LED file path on your system.
2. Run `./install.sh`

## Running
If you have systemd and want to enable the script as soon as you log in, run `systemctl --user enable micmute_listener_pa.service`.

To start the service immediately, run `systemctl --user start micmute_listener_pa.service`.

## Contributions
I'm very intrested in your opinions in terms of the architecture of this service. If you have suggestions on how to avoid SETUID or make the whole thing cleaner or more secure, please start a discussion!