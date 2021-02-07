#!/bin/bash
cp micmute_listener_pa.py ~/.local/bin/. &&
mkdir -p ~/.config/systemd/user/ &&
cp micmute_listener_pa.service ~/.config/systemd/user/. &&
gcc set_micmute_led.c -o set_micmute_led &&
sudo chown root:root set_micmute_led &&
sudo chmod u+s set_micmute_led &&
sudo mv set_micmute_led /usr/local/bin/.