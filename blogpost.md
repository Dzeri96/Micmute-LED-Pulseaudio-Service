# Micmute listener service for pulseaudio

## Problems I faced:
1. Only root can write to the led brightness file.
2. Running the script as root prevents it from connecting to pulseaudio.
3. Running pulseaudio in system mode is bad for security and performance.
4. setfacl doesn't work for some reason.
5. Udev triggers also don't work.
6. SUID doesn't work with interpreted files.

## Links
https://github.com/torfsen/python-systemd-tutorial