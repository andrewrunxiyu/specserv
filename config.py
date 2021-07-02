#!/usr/bin/env python3
#
#  ____  _____    _    ____    _____ _   _ ___ ____    ____ ___ _____ _
# |  _ \| ____|  / \  |  _ \  |_   _| | | |_ _/ ___|  | __ )_ _|_   _| |
# | |_) |  _|   / _ \ | | | |   | | | |_| || |\___ \  |  _ \| |  | | | |
# |  _ <| |___ / ___ \| |_| |   | | |  _  || | ___) | | |_) | |  | | |_|
# |_| \_\_____/_/   \_\____/    |_| |_| |_|___|____/  |____/___| |_| (_)
#
# This is not a configuration file. This is a module that *reads* config.yaml, and *that* is your configuration file.
# You would only want to edit this file in case you want to really extend the way that the program reads the
# configuration, i.e., read everything from a totally different configuration format. However, of course, you need to
# output everything to the format that gets produced by the default version of this config.py. Otherwise, how could the
# other scripts in this program understand and parse the configuration?
#


import yaml
from yaml.loader import SafeLoader


with open('config.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
