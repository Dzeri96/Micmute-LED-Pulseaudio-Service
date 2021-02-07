#!/bin/python3

import pulsectl
import os
pulse = pulsectl.Pulse('my-client-name')

active_index = 1 # This is the index of the source
pulse_event = None

with pulsectl.Pulse('event-printer') as pulse:
    #print('Event types:', pulsectl.PulseEventTypeEnum)
    #print('Event facilities:', pulsectl.PulseEventFacilityEnum)
    #print('Event masks:', pulsectl.PulseEventMaskEnum)
    #print('Source list:', pulse.source_list())

    def print_events(ev):
        #print('Pulse event:', ev)
        global pulse_event
        pulse_event = ev
        ### Raise PulseLoopStop for event_listen() to return before timeout (if any)
        raise pulsectl.PulseLoopStop

    pulse.event_mask_set('all')
    pulse.event_callback_set(print_events)

    while True:
        pulse.event_listen()

        if pulse_event.index == active_index:
                led_value = 0 if pulse.source_info(active_index).mute == 1 else 1
                os.system("/usr/local/bin/set_micmute_led " + str(led_value))