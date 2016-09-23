# import os
# import glob

# all_list = list()
# #for f in glob.glob(os.path.dirname(__file__)+"/*.py"):
# print str(__file__)
# print str(os.path.abspath(__file__))
# print str(os.path.abspath(__file__)+"\\*.py")
# print str(os.path.abspath(__file__)+"/*.py")
# for f in glob.glob(os.path.abspath(__file__)+"\\*.py"):
    # print str(f)
    # if os.path.isfile(f) and not os.path.basename(f).startswith('_'):
        # all_list.append(os.path.basename(f)[:-3])

# __all__ = all_list 


#for m in __all__:
#	print str(m)
#	module_obj = __import__(m)

# import pkgutil 

# __path__ = pkgutil.extend_path(__path__, __name__)
# for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
      # __import__(modname)
#print str( os.path.abspath(__file__) )

import pymod_example
import tripping_bite

import psi

import bard
import cleric
import druid
import paladin
import ranger
import rogue
import sorcerer
import wizard


import arcane_archer
import arcane_trickster
import archmage
import assassin
import blackguard
import duelist
import dwarven_defender
import eldritch_knight
import mystic_theurge
import bladesinger

import fighting_defensively
import opportunist

import prayer_beads
