#!/usr/bin/env python

import sys
sys.path.append('/usr/share/inkscape/extensions') # or another path, as necessary

import inkex
from simplestyle import *

class PCheck(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-w', '--what', action = 'store',
          type = 'string', dest = 'what', default = 'World',
          help = 'What would you like to greet?')
