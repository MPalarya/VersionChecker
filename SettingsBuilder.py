import json
from collections import OrderedDict  # just to keep the json sorted and readable


def build_json():
    """
    'path'      -- directory to check for a new version
    'latest'    -- filename of latest (most recent) file in that directory
    'output'    -- where to copy the setup file to
    'to'        -- list of email addresses to notify on new version detection
    'cc'        -- ..
    'bcc        -- ..
    """

    manpack = OrderedDict()
    manpack['path'] = r'I:\ManPack-SDR Tester'
    manpack['latest'] = r'Manpack-SDR Tester 1.0.43.6 Setup.exe'
    manpack['output'] = r'\\jellyfish02\Projects\Manpack SDR\GUI Tester'
    manpack['to'] = ['michael.palarya@elbitsystems.com']
    manpack['cc'] = []
    manpack['bcc'] = []

    uwb = OrderedDict()
    uwb['path'] = r'I:\UWB Tester'
    uwb['latest'] = r'UWB Tester 1.0.0.2 Setup.exe'
    uwb['output'] = r'\\jellyfish02\Projects\Manpack SDR\UWB Tester'
    uwb['to'] = ['michael.palarya@elbitsystems.com']
    uwb['cc'] = []
    uwb['bcc'] = []

    settings = OrderedDict()
    settings['manpack'] = manpack
    settings['uwb'] = uwb

    print json.dumps(settings, indent=4)

    with open('Settings.json', 'w') as outfile:
        json.dump(settings, outfile, indent=4)


build_json()
