

manufacturers = [
  {'id': 0x00a1,
   'name': u'Creative Lighting',
   'pids': [
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'mode', 'type': 'uint8', 'enums': [
                            (0, 'DMX512'), (1, 'DALI'), (2, 'DSI')]
                          }
                        ]},
       'get_sub_device_range': 2,
       'name': u'DEVICE_MODE',
       'set_request': {'items': [{'name': u'mode', 'type': 'uint8',
                                  'enums': [(0, 'DMX512'), (1, 'DALI'), (2, 'DSI')]
                      }]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.creativelighting.com.au/datasheets/RDM%20Supplement.pdf',
       'notes': 'Controls the operating mode of the device',
       'value': 32768}]
  },
  {'id': 0x4845,
   'name': u'Howard Eaton Lighting',
   'pids': [
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'enabled', 'type': 'bool'},
                          {'name': u'max_allowed', 'type': 'uint8'}
                        ]},
       'get_sub_device_range': 0,
       'name': 'PWRUP_TEST',
       'set_request': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': 'http://www.goddarddesign.com/pdf_doc/rdmlabpack%20srn%20v2p9.pdf',
       'notes': 'Enable/disable the Power On Self Test (POST).',
       'value': 0xc857},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'dmx_nsc_packet_count', 'type': 'uint16'},
                          {'name': u'dmx_asc_packet_count', 'type': 'uint16'},
                          {'name': u'rdm_asc_packet_count', 'type': 'uint16'},
                          {'name': u'uart_errors', 'type': 'uint8'},
                          {'name': u'device_minutes', 'type': 'uint8'},
                          {'name': u'brownout_count', 'type': 'uint8'},
                          {'name': u'watchdog_resets', 'type': 'uint8'},
                          {'name': u'software_resets', 'type': 'uint8'},
                          {'name': u'dither_adjust', 'type': 'uint16'},
                          {'name': u'record_sensor_counts', 'type': 'uint8'},
                        ]},
       'get_sub_device_range': 0,
       'name': 'INTERNAL_STATS',
       'set_request': {'items': []},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': 'http://www.goddarddesign.com/pdf_doc/rdmlabpack%20srn%20v2p9.pdf',
       'notes': 'Fetch the internal stats.',
       'value': 0xc862},
    ],
  },
  {'id': 0x4a61,
   'name': u'Jands',
   'pids': [
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'enabled', 'type': 'bool'}
                        ]},
       'get_sub_device_range': 0,
       'name': u'NE_FAULT_DETECT_MODE',
       'set_request': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': 'http://www.jands.com.au/__data/assets/pdf_file/0004/36364/HPD_User_Manual_V2.0a.pdf',
       'notes': 'Turns the Neutral-Earth (N-E) fault detector on and off.',
       'value': 0x8080},
      {'get_request': {'items': []},
       'get_response': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'get_sub_device_range': 0,
       'name': u'DMX_PROTECT_MODE',
       'set_request': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': 'http://www.jands.com.au/__data/assets/pdf_file/0004/36364/HPD_User_Manual_V2.0a.pdf',
       'notes': 'Unknown.',
       'value': 0x8082},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'mode', 'type': 'uint8',
                           'enums': [(0, 'Hold'), (1, 'Fade to scene #1')]
                          }
                        ]},
       'get_sub_device_range': 0,
       'name': u'DMX_LOSS_MODE',
       'set_request': {'items': [{'name': u'mode', 'type': 'uint8',
                                  'enums': [
                                      # TODO: check if we can use scene 2 as well
                                      (0, 'Hold'), (1, 'Fade to scene #1')]
                          }]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': 'http://www.jands.com.au/__data/assets/pdf_file/0004/36364/HPD_User_Manual_V2.0a.pdf',
       'notes': 'Controls the behaviour when the DMX signal is lost.',
       'value': 0x8084},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'level', 'type': 'uint8', 'enums': [
                            (0, 'Off')]
                          }
                        ]},
       'get_sub_device_range': 2,
       'name': u'PREHEAT_LEVEL',
       'set_request': {'items': [{'name': u'level', 'type': 'uint8',
                                  'enums': [(0, 'Off')],
                                  'range': [(0, 0x32)],
                          }]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.jands.com.au/__data/assets/pdf_file/0004/36364/HPD_User_Manual_V2.0a.pdf',
       'notes': 'The Preheat function is used to  inject a small amount of power into the lamps when the control is set to zero.',
       'value': 0x8086},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'cap', 'type': 'uint8',
                           'enums': [(0, 'Off'),
                                     (1, '95%'),
                                     (2, '90%'),
                                     (3, '85%'),
                                     (4, '80%'),
                                     (5, '75%'),
                                     (6, '70%'),
                                     (7, '65%'),
                                     (8, '60%'),
                                     (9, '55%'),
                                     (10, '50%'),
                                     (11, '45%'),
                                     (12, '40%')],
                          }
                        ]},
       'get_sub_device_range': 2,
       'name': u'OUTPUT_CAP_VALUE',
       'set_request': {'items': [{'name': u'cap', 'type': 'uint8',
                                   'enums': [(0, 'Off'),
                                             (1, '95%'),
                                             (2, '90%'),
                                             (3, '85%'),
                                             (4, '80%'),
                                             (5, '75%'),
                                             (6, '70%'),
                                             (7, '65%'),
                                             (8, '60%'),
                                             (9, '55%'),
                                             (10, '50%'),
                                             (11, '45%'),
                                             (12, '40%'),
                                            ],
                          }]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.jands.com.au/__data/assets/pdf_file/0004/36364/HPD_User_Manual_V2.0a.pdf',
       'notes': 'Scale the output power of by a preset percentage. Each increment reduces output power by 5%, down to a minimum value of 40%. See the manual for more details on output voltage.',
       'value': 0x8088},
      {'get_request': {'items': []},
       'get_response': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'get_sub_device_range': 0,
       'name': u'DMX_TERM_MODE',
       'set_request': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': 'http://www.jands.com.au/__data/assets/pdf_file/0004/36364/HPD_User_Manual_V2.0a.pdf',
       'notes': 'Enable DMX termination.',
       'value': 0x808A},
    ]
  },
  {'id': 21324,
   'name': u'Soundlight',
   'pids': [
      {'get_request': {'items': []},
       'get_response': {'items': [{'name': u'mode', 'type': 'uint8'}]},
       'get_sub_device_range': 2,
       'name': u'DMX_HOLD_MODE',
       'set_request': {'items': [{'name': u'mode', 'type': 'uint8', 'enums': [
                          (0, 'Outputs to 0%'), (1, 'Output to 100%'),
                          (2, 'Hold'), (3, 'Go to predefined scene')],
                        }]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'Controls the behavior of the device when the signal fails.',
       'value': 0x80f1},
      {'get_request': {'items': [{'name': u'sensor_number', 'type': 'uint8'}]},
       'get_response': {'items': [{'name': u'sensor_number', 'type': 'uint8'},
                                  {'name': u'type', 'type': 'uint8'},
                                  {'name': u'unit', 'type': 'uint8'},
                                  {'name': u'prefix', 'type': 'uint8'},
                                  {'name': u'range_min', 'type': 'uint16'},
                                  {'name': u'range_max', 'type': 'uint16'},
                                  {'name': u'normal_min', 'type': 'uint16'},
                                  {'name': u'normal_max', 'type': 'uint16'},
                                  {'name': u'supports_recording',
                                   'type': 'uint8'},
                                  {'name': u'name',
                                   'max_size': 20,
                                   'type': 'string'}]},
       'get_sub_device_range': 2,
       'set_request': {'items': [{'name': u'sensor_number', 'type': 'uint8'},
                                 {'name': u'type', 'type': 'uint8'},
                                 {'name': u'unit', 'type': 'uint8'},
                                 {'name': u'prefix', 'type': 'uint8'},
                                 {'name': u'range_min', 'type': 'uint16'},
                                 {'name': u'range_max', 'type': 'uint16'},
                                 {'name': u'normal_min', 'type': 'uint16'},
                                 {'name': u'normal_max', 'type': 'uint16'},
                                 {'name': u'supports_recording',
                                  'type': 'uint8'},
                                 {'name': u'name',
                                  'max_size': 20,
                                  'type': 'string'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 2,
       'name': u'MODIFY_SENSOR_DEFINITION',
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'Used for setting a sensor definition for devices with variable sensor input. The SENSOR_DEFINITION PID in the E1.20 standard can read a sensor standard definition only, but not set.',
       'value': 0x8200},
      {'get_request': {'items': []},
       'get_response': {'items': [{'name': u'scale_value', 'type': 'uint8'}]},
       'get_sub_device_range': 2,
       'name': u'DC_CALIBRATION',
       'set_request': {'items': [{'name': u'scale_value', 'type': 'uint8'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'With the parameters, the outputs can be scaled to the desired maximum value',
       'value': 0xdcca},
      {'get_request': {'items': []},
       'get_response': {'items': [{'type': 'group',
                                   'name': 'dc_offsets',
                                   'items': [{'name': u'offset_value', 'type': 'uint8'}]
                        }]},
       'get_sub_device_range': 2,
       'name': u'DC_OFFSET',
       'set_request': {'items': [{'type': 'group',
                                  'name': 'dc_offsets',
                                  'items': [{'name': u'offset_value', 'type': 'uint8'}]
                        }]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'With the parameters, the offset adjustment of the outputs are set to the desired value. It is transmitted as many values as outputs must be set. The number is determined by the parameters length (PDL).  The offset input is especially useful when driving LEDs with a different starting point',
       'value': 0xdc0e},
      {'name': u'DC_FADER_OFFSET',
        'set_request': {'items': [{'type': 'group',
                                   'name': 'offsets',
                                   'items': [{'name': u'offset_value', 'type': 'uint8'}]
                                  }]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'With the parameters, the offset adjustment of the outputs are set to the desired value. The values are collected directly from the DMX input (the last valid zero weather package). There are are as many values as outputs must be set. The acquisition is initiated by the command. A reading is possible with the function DC_OFFSET. ',
       'value': 0xdc0f},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'curve_number', 'type': 'uint8'},
                          {'name': u'total_curves', 'type': 'uint8'},
                          {'name': u'segment_count', 'type': 'uint8'},
                          {'name': u'interpolation_method', 'type': 'uint8',
                           'enums': [(0, 'Step'), (1, 'Linear'), (2, 'Square'), (3, 'Cubic')],
                          },
                          {'name': u'start_value', 'type': 'uint8'},
                          {'name': u'curve_values',
                           'type': 'group',
                           'items': [
                             {'name': u'value', 'type': 'uint8'},
                           ],
                          },
                        ]},
       'get_sub_device_range': 2,
       'name': u'CURVE_DEFINITION',
       'set_request': {'items': [
                         {'name': u'curve_number', 'type': 'uint8'},
                         {'name': u'total_curves', 'type': 'uint8'},
                         {'name': u'segment_count', 'type': 'uint8'},
                         {'name': u'interpolation_method', 'type': 'uint8',
                          'enums': [(0, 'Step'), (1, 'Linear'), (2, 'Square'), (3, 'Cubic')],
                         },
                         {'name': u'start_value', 'type': 'uint8'},
                         {'name': u'curve_values',
                          'type': 'group',
                          'items': [
                            {'name': u'value', 'type': 'uint8'},
                          ],
                         },
                       ]},
       'set_response': {'items': []},
       'set_sub_device_range': 1,
       'link': 'http://www.soundlight.de/techtips/dmx512/slh_rdm_commands.htm',
       'notes': 'The number of values supplied needs to match what\' specified in the segment_count field',
       'value': 0xdccd},
   ]
  },
  {'id': 0x4c55,
   'name': u'Lumen Radio',
   'pids': [
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'enabled', 'type': 'bool'}
                        ]},
       'get_sub_device_range': 0,
       'name': u'FULL_DISCOVERY',
       'set_request': {'items': [{'name': u'enabled', 'type': 'bool'}]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': '',
       'notes': 'Starts full RDM discovery.',
       'value': 0x8000},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'interval', 'type': 'uint16',
                           'multiplier': -1},
                        ]},
       'get_sub_device_range': 0,
       'name': u'INCREMENTAL_DISCOVERY_INTERVAL',
       'set_request': {'items': [{'name': u'interval', 'type': 'uint16',
                                  'range': [(0x101, 0xffff)],
                                  'multiplier': -1,
                                 }]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': '',
       'notes': 'Controls the frequency at which incremental discovery runs.',
       'value': 0x8101},
      {'get_request': {'items': []},
       'get_response': {'items': [
                          {'name': u'timer_factor', 'type': 'uint16'}
                        ]},
       'get_sub_device_range': 0,
       'name': u'ACK_TIMER_FACTOR',
       'set_request': {'items': [{'name': u'timer_factor', 'type': 'uint16',
                                  'range': [(0x101, 0xffff)],
                                 }]},
       'set_response': {'items': []},
       'set_sub_device_range': 0,
       'link': '',
       'notes': 'Unknown.',
       'value': 0x8102},
    ],
  },
]


pids = [{'get_request': {'items': []},
  'get_response': {'items': [{'name': u'description',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_MODEL_DESCRIPTION',
  'value': 128},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'label',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'MANUFACTURER_LABEL',
  'value': 129},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'label',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_LABEL',
  'set_request': {'items': [{'name': u'label',
                             'max_size': 32,
                             'type': 'string'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 130},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'state', 'type': 'uint8', 'enums': [
                      (0, 'Off'), (1, 'On'), (2, 'Strike'), (3, 'Standby'),
                      (4, 'Not Present'), (0x7f, 'Error')]
                  }]},
  'get_sub_device_range': 2,
  'name': u'LAMP_STATE',
  'set_request': {'items': [{'name': u'state', 'type': 'uint8',
                  'enums': [(0, 'Off'), (1, 'On'), (2, 'Strike'), (3, 'Standby')],
                  'range': [(0, 3), (0x80, 0xDF)],
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1027},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'mode', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_ON_MODE',
  'set_request': {'items': [{'name': u'mode', 'type': 'uint8',
                  'enums': [(0, 'Off'), (1, 'DMX'), (2, 'On'), (3, 'On After Calibration')],
                  'range': [(0, 3), (0x80, 0xDF)],
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1028},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'power_cycles', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_POWER_CYCLES',
  'set_request': {'items': [{'name': u'power_cycles', 'type': 'uint32'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1029},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'identify_state', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'IDENTIFY_DEVICE',
  'set_request': {'items': [{'name': u'identify_state', 'type': 'bool'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 4096},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'version', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'BOOT_SOFTWARE_VERSION',
  'value': 193},
 {'name': u'RECORD_SENSORS',
  'set_request': {'items': [{'name': u'sensor_number', 'type': 'uint8',
                             'range': [(0, 0xff)],
                             'enums': [(0xff, 'All Sensors')],
                 }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 514},
 {'get_request': {'items': []},
  'get_response': {'items': [{'type': 'group',
                              'name': 'uids',
                              'items': [{'name': u'manufacturer_id', 'type': 'uint16'},
                                        {'name': u'device_id', 'type': 'uint32'}],
                   }]},
  'get_sub_device_range': 0,
  'name': u'PROXIED_DEVICES',
  'value': 16},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'device_count', 'type': 'uint16'},
                             {'name': u'list_changed', 'type': 'bool'}]},
  'get_sub_device_range': 0,
  'name': u'PROXIED_DEVICE_COUNT',
  'value': 17},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'year', 'type': 'uint16'},
                             {'name': u'month', 'type': 'uint8'},
                             {'name': u'day', 'type': 'uint8'},
                             {'name': u'hour', 'type': 'uint8'},
                             {'name': u'minute', 'type': 'uint8'},
                             {'name': u'second', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'REAL_TIME_CLOCK',
  'set_request': {'items': [{'name': u'year', 'type': 'uint16', 'range': [(2003, 65535)]},
                    {'name': u'month', 'type': 'uint8', 'range': [(1, 12)]},
                    {'name': u'day', 'type': 'uint8', 'range': [(1, 31)]},
                    {'name': u'hour', 'type': 'uint8', 'range': [(0, 23)]},
                    {'name': u'minute', 'type': 'uint8', 'range': [(0, 59)]},
                    {'name': u'second', 'type': 'uint8', 'range': [(0, 60)]}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1539},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'short_message', 'type': 'uint16'},
                             {'name': u'length_mismatch', 'type': 'uint16'},
                             {'name': u'checksum_fail', 'type': 'uint16'}]},
  'get_sub_device_range': 0,
  'name': u'COMMS_STATUS',
  'set_request': {'items': []},
  'set_response': {'items': []},
  'set_sub_device_range': 0,
  'value': 21},
 {'get_request': {'items': [{'name': u'sensor_number', 'type': 'uint8',
                             'range': [(0, 0xfe)],
                 }]},
  'get_response': {'items': [{'name': u'sensor_number', 'type': 'uint8'},
                             {'name': u'type', 'type': 'uint8'},
                             {'name': u'unit', 'type': 'uint8'},
                             {'name': u'prefix', 'type': 'uint8'},
                             {'name': u'range_min', 'type': 'uint16'},
                             {'name': u'range_max', 'type': 'uint16'},
                             {'name': u'normal_min', 'type': 'uint16'},
                             {'name': u'normal_max', 'type': 'uint16'},
                             {'name': u'supports_recording',
                              'type': 'uint8'},
                             {'name': u'name',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SENSOR_DEFINITION',
  'value': 512},
 {'get_request': {'items': [{'name': u'status_type', 'type': 'uint8', 'enums': [
                    (1, 'Last Message'), (2, 'Advisory'),
                    (3, 'Warning'), (4, 'Error')]
                   }]},
  'get_response': {'items': []},
  'get_sub_device_range': 0,
  'name': u'QUEUED_MESSAGE',
  'value': 32},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'language',
                              'max_size': 2,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'LANGUAGE',
  'set_request': {'items': [{'name': u'language',
                             'max_size': 2,
                             'type': 'string'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 176},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': 'slot_values',
                              'type': 'group',
                              'items': [{'name': u'slot_offset', 'type': 'uint16'},
                                        {'name': u'default_slot_value', 'type': 'uint8'}]
                  }]},
  'get_sub_device_range': 2,
  'name': u'DEFAULT_SLOT_VALUE',
  'value': 290},
 {'name': u'RESET_DEVICE',
  'set_request': {'items': [{'name': u'reset_mode', 'type': 'uint8', 'enums': [
                    (1, 'Warm'), (0xff, 'Cold')]
                 }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 4097},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'hours', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_HOURS',
  'set_request': {'items': [{'name': u'hours', 'type': 'uint32'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1024},
 {'name': u'CAPTURE_PRESET',
  'set_request': {'items': [{'name': u'scene', 'type': 'uint16'},
                            {'name': u'fade_up_time', 'type': 'uint16'},
                            {'name': u'fade_down_time', 'type': 'uint16'},
                            {'name': u'wait_time', 'type': 'uint16'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 4144},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'dmx_address', 'type': 'uint16'}]},
  'get_sub_device_range': 2,
  'name': u'DMX_START_ADDRESS',
  'set_request': {'items': [{'name': u'dmx_address', 'type': 'uint16', 'range': [
                    (1, 512)],
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 240},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'invert_status', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DISPLAY_INVERT',
  'set_request': {'items': [{'name': u'invert_status', 'type': 'uint8', 'enums': [
                      (0, 'Off'), (1, 'On'), (2, 'Auto')]
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1280},
 {'get_request': {'items': [{'name': u'status_type', 'type': 'uint8', 'enums': [
                    (0, 'None'), (1, 'Last Message'), (2, 'Advisory'),
                    (3, 'Warning'), (4, 'Error')]
                   }]},
  'get_response': {'items': [{'type': 'group',
                              'name': 'messages',
                              'items': [{'name': u'sub_device', 'type': 'uint16'},
                                        {'name': u'status_type', 'type': 'uint8'},
                                        {'name': u'message_id', 'type': 'uint16'},
                                        {'name': u'value1', 'type': 'uint16'},
                                        {'name': u'value2', 'type': 'uint16'}],
                  }]},
  'get_sub_device_range': 0,
  'name': u'STATUS_MESSAGE',
  'value': 48},
 {'get_request': {'items': [{'name': u'status_id', 'type': 'uint16'}]},
  'get_response': {'items': [{'name': u'label',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 0,
  'name': u'STATUS_ID_DESCRIPTION',
  'value': 49},
 {'name': u'CLEAR_STATUS_ID',
  'set_request': {'items': []},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 50},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'status_type', 'type': 'uint8'}]},
  'get_sub_device_range': 3,
  'name': u'SUB_DEVICE_STATUS_REPORT_THRESHOLD',
  'set_request': {'items': [{'name': u'status_type', 'type': 'uint8', 'enums': [
                    (0, 'None'), (2, 'Advisory'), (3, 'Warning'), (4, 'Error')]
                   }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 51},
 {'get_request': {'items': [{'name': u'sensor_number', 'type': 'uint8',
                             'range': [(0, 0xfe)],
                  }]},
  'get_response': {'items': [{'name': u'sensor_number', 'type': 'uint8'},
                             {'name': u'present_value', 'type': 'uint16'},
                             {'name': u'lowest', 'type': 'uint16'},
                             {'name': u'highest', 'type': 'uint16'},
                             {'name': u'recorded', 'type': 'uint16'}]},
  'get_sub_device_range': 2,
  'name': u'SENSOR_VALUE',
  'set_request': {'items': [{'name': u'sensor_number',
                             'type': 'uint8',
                             'range': [(0, 0xff)],
                             'enums': [(0xff, 'All Sensors')],
                 }]},
  'set_response': {'items': [{'name': u'sensor_number', 'type': 'uint8'},
                             {'name': u'present_value', 'type': 'uint16'},
                             {'name': u'lowest', 'type': 'uint16'},
                             {'name': u'highest', 'type': 'uint16'},
                             {'name': u'recorded', 'type': 'uint16'}]},
  'set_sub_device_range': 1,
  'value': 513},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'invert', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'PAN_INVERT',
  'set_request': {'items': [{'name': u'invert', 'type': 'bool'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1536},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'label',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SOFTWARE_VERSION_LABEL',
  'value': 192},
 {'get_request': {'items': []},
  'get_response': {'items': [{'type': 'group',
                              'name': 'languages',
                              'items': [{'name': u'language',
                                         'max_size': 2,
                                         'min_size': 2,
                                         'type': 'string'}],
                  }]},
  'get_sub_device_range': 2,
  'name': u'LANGUAGE_CAPABILITIES',
  'value': 160},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'label',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'BOOT_SOFTWARE_LABEL',
  'value': 194},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'hours', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_HOURS',
  'set_request': {'items': [{'name': u'hours', 'type': 'uint32'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1025},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'mode', 'type': 'uint16'},
                             {'name': u'level', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'PRESET_PLAYBACK',
  'set_request': {'items': [{'name': u'mode', 'type': 'uint16',
                             'enums': [(0, 'Off'), (0xffff, 'All')],
                             'range': [(0, 0xffff)]},
                            {'name': u'level', 'type': 'uint8'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 4145},
 {'get_request': {'items': [{'name': u'personality', 'type': 'uint8', 'range': [
                    (0, 0xff)]
                  }]},
  'get_response': {'items': [{'name': u'personality', 'type': 'uint8'},
                             {'name': u'slots_required', 'type': 'uint16'},
                             {'name': u'name',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'DMX_PERSONALITY_DESCRIPTION',
  'value': 225},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'level', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DISPLAY_LEVEL',
  'set_request': {'items': [{'name': u'level', 'type': 'uint8'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1281},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'current_personality',
                              'type': 'uint8'},
                             {'name': u'personality_count',
                              'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DMX_PERSONALITY',
  'set_request': {'items': [{'name': u'personality', 'type': 'uint8', 'range': [
                    (0, 0xff)]
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 224},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': 'slots',
                              'type': 'group',
                              'items': [{'name': u'slot_offset', 'type': 'uint16'},
                                        {'name': u'slot_type', 'type': 'uint8'},
                                        {'name': u'slot_label_id', 'type': 'uint16'}],
                   }]},
  'get_sub_device_range': 2,
  'name': u'SLOT_INFO',
  'value': 288},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': 'params',
                              'type': 'group',
                              'items': [{'name': 'param_id', 'type': 'uint16'}],
                             }]
                  },
  'get_sub_device_range': 2,
  'name': u'SUPPORTED_PARAMETERS',
  'value': 80},
 {'get_request': {'items': [{'name': u'pid', 'type': 'uint16'}]},
  'get_response': {'items': [{'name': u'pid', 'type': 'uint16'},
                             {'name': u'pdl_size', 'type': 'uint8'},
                             {'name': u'data_type', 'type': 'uint8'},
                             {'name': u'command_class', 'type': 'uint8'},
                             {'name': u'type', 'type': 'uint8'},
                             {'name': u'unit', 'type': 'uint8'},
                             {'name': u'prefix', 'type': 'uint8'},
                             {'name': u'min_value', 'type': 'uint32'},
                             {'name': u'max_value', 'type': 'uint32'},
                             {'name': u'default_value', 'type': 'uint32'},
                             {'name': u'description',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 0,
  'name': u'PARAMETER_DESCRIPTION',
  'value': 81},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'invert', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'TILT_INVERT',
  'set_request': {'items': [{'name': u'invert', 'type': 'bool'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1537},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'protocol_major', 'type': 'uint8'},
                             {'name': u'protocol_minor', 'type': 'uint8'},
                             {'name': u'device_model', 'type': 'uint16'},
                             {'name': u'product_category',
                              'type': 'uint16'},
                             {'name': u'software_version',
                              'type': 'uint32'},
                             {'name': u'dmx_footprint', 'type': 'uint16'},
                             {'name': u'current_personality',
                              'type': 'uint8'},
                             {'name': u'personality_count',
                              'type': 'uint8'},
                             {'name': u'dmx_start_address', 'type': 'uint16'},
                             {'name': u'sub_device_count',
                              'type': 'uint16'},
                             {'name': u'sensor_count', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'DEVICE_INFO',
  'value': 96},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'using_defaults', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'FACTORY_DEFAULTS',
  'set_request': {'items': []},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 144},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'strikes', 'type': 'uint32'}]},
  'get_sub_device_range': 2,
  'name': u'LAMP_STRIKES',
  'set_request': {'items': [{'name': u'strikes', 'type': 'uint32'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1026},
 {'get_request': {'items': [{'name': u'test_number', 'type': 'uint8'}]},
  'get_response': {'items': [{'name': u'test_number', 'type': 'uint8'},
                             {'name': u'description',
                              'max_size': 32,
                              'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SELF_TEST_DESCRIPTION',
  'value': 4129},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'power_state', 'type': 'uint8'}]},
  'get_sub_device_range': 2,
  'name': u'POWER_STATE',
  'set_request': {'items': [{'name': u'power_state', 'type': 'uint8', 'enums': [
                    (0, 'Full Off'), (1, 'Shutdown'), (2, 'Standby'),
                    (0xff, 'Normal')]
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 4112},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'tests_active', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'PERFORM_SELF_TEST',
  'set_request': {'items': [{'name': u'test_number', 'type': 'uint8',
                  'range': [(0, 0xff)],
                  'enums': [(0, 'Off'), (0xff, 'All')],
                  }]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 4128},
 {'get_request': {'items': [{'name': u'slot_number', 'type': 'uint16'}]},
  'get_response': {'items': [{'name': u'slot_number', 'type': 'uint16'},
                             {'name': u'name', 'max_size': 32, 'type': 'string'}]},
  'get_sub_device_range': 2,
  'name': u'SLOT_DESCRIPTION',
  'value': 289},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': 'detail_ids',
                              'type': 'group',
                              'max_size': 6,
                              'items': [{'name': 'detail_id', 'type': 'uint16'}],
                   }]},
  'get_sub_device_range': 2,
  'name': u'PRODUCT_DETAIL_ID_LIST',
  'value': 112},
 {'get_request': {'items': []},
  'get_response': {'items': [{'name': u'swap', 'type': 'bool'}]},
  'get_sub_device_range': 2,
  'name': u'PAN_TILT_SWAP',
  'set_request': {
                  'items': [{'name': u'swap', 'type': 'bool'}]},
  'set_response': {'items': []},
  'set_sub_device_range': 1,
  'value': 1538}]
