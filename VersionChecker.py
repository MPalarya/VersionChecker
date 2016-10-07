import glob
import os
from shutil import copyfile
import json


def check_version(settings_file):

    with open(settings_file) as json_file:
        settings = json.load(json_file)

    for tester in settings:
        path = settings[tester]['path']
        latest_published = settings[tester]['latest']

        list_of_exes = [os.path.join(path, x)
                        for x in os.listdir(path) if x.lower().endswith('.exe')]
        print list_of_exes

        latest_version = os.path.basename(max(list_of_exes, key=os.path.getctime))
        print latest_version

        if latest_version == latest_published:
            print '%s \t - UP TO DATE!' % tester

        else:
            print '%s \t\t - there is a new version!' % tester
            print 'copying...\t %s' % latest_version
            print 'from:     \t %s' % path
            print 'to:       \t %s' % settings[tester]['output']
            src = os.path.join(path, latest_version)
            dst = os.path.join(settings[tester]['output'], latest_version)
            if not os.path.isfile(dst):
                copyfile(src, dst)
            print 'success!'

            settings[tester]['latest'] = latest_version
            with open(settings_file, 'w') as outfile:
                json.dump(settings, outfile, indent=4)

            print 'updated settings file'

        print ''

check_version(r'I:\VersionPublisher\Settings.json')

