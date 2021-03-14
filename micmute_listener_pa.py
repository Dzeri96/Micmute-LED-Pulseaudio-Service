#!/bin/python3

import pulsectl
import os
import sys
import signal
pulse = pulsectl.Pulse('micmute-listener')

# TODO: Read this from an external config file
mic_name = 'alsa_input.pci-0000_04_00.6.analog-stereo'

active_index = 1 # This is the index of the source
pulse_event = None

def shutdown(signum, frame):
    print('Shutting down client...')
    pulse.disconnect()
    quit(0)

def find_mic_index():
    global active_index

    for source in pulse.source_list():
        if(source.name == mic_name):
            active_index = int(source.index)
            print('Mic index set: %d' % (active_index))
            return
    
    raise RuntimeError('Could not find a device corresponding to %s!' % (mic_name))

def catch_events(ev):
    print('Pulse event:', ev)
    global pulse_event
    pulse_event = ev
    ### Raise PulseLoopStop for event_listen() to return before timeout (if any)
    raise pulsectl.PulseLoopStop

def set_led_value(value):
    os.system("/usr/local/bin/set_micmute_led " + str(value))

def init():
    pulse.connect(wait= True)

    #print('Event types:', pulsectl.PulseEventTypeEnum)
    #print('Event facilities:', pulsectl.PulseEventFacilityEnum)
    #print('Event masks:', pulsectl.PulseEventMaskEnum)
    print('Source list:', pulse.source_list())
    
    find_mic_index()
    init_led_value = 0 if pulse.source_info(active_index).mute == 1 else 1
    set_led_value(init_led_value)

    pulse.event_mask_set('all')
    pulse.event_callback_set(catch_events)


if __name__ == '__main__':
    print('Starting the micmute listener...')
    signal.signal(signal.SIGINT, shutdown)
    init()

    while True:
        try:
            pulse.event_listen()
        except pulsectl.pulsectl.PulseDisconnected:
            # TODO: check the docu, maybe this isn't the best way to restart the connection
            print('PulseAudio disconnected! Attempting to reconnect...', file=sys.stderr)
            init()
            continue

        if pulse_event.index == active_index:
                led_value = 0 if pulse.source_info(active_index).mute == 1 else 1
                set_led_value(led_value)