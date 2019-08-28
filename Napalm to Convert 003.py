##### SET VARIABLES THAT MIGHT NOT BE SET FROM INPUT #####################################
#    This is where you add additional zones, tunnels, etc. if new prod stuff is added    #
##########################################################################################
import os
import sys
import napalm
import json
configFileNapalm = "TEST.txt"
newHostNameNapalm = [0, 0, 0, 0]
hostNameNapalm = "BLANKHOSTNAPALM"
userNameNapalm = "BLANKUSERNAPALM"
passWordNapalm = "BLANKPASSNAPALM"
#auto_rollback_on_error=False


###############################################################################
#####    Napalm Function(s)                                               #####
###############################################################################
def convert(hostNameNapalm, userNameNapalm, passWordNapalm):
    """Load a config for the device."""
    if not (os.path.exists(hostNameNapalm+".txt") and os.path.isfile(hostNameNapalm+".txt")):
        msg = 'Missing or invalid config file {0}'.format(hostNameNapalm)
        raise ValueError(msg)
    driver = napalm.get_network_driver('ios')
    errors={'auto_rollback_on_error':False}
    device = driver(hostname=(hostNameNapalm), username=(userNameNapalm), password=(passWordNapalm),optional_args=(errors))
    print ('Opening...')
    device.open()
    print ('Loading replacement Candidate...')
    device.load_merge_candidate(filename=(hostNameNapalm+".txt"))
    print ('/nDiff:')
    print (device.compare_config())
    choice = input("\nCommit? [y-n]: ")
    if choice == 'y':
      print ('Committing ...')
      device.commit_config()
    else:
      print ('Discarding ...')
      device.discard_config()
    device.close()
    print ('Done.')
    

#########################################################
#####  GATHER INPUT FOR ACTUAL NAPALM CONFIGURATION #####
#########################################################
#sys.stdout.write
while True:
        try:
            hostNameNapalm = str(input ("Please enter the host IP that you want to convert: "))
        except ValueError:
            print("That is not a valid entry.  Please try again.")
            continue
#        newHostNameNapalm = (hostNameNapalm.split("."))
#        if int(newHostNameNapalm[0]) != 10:
#            print ("This is not a correct IP for a Hostname, your 1st octet is invalid. ")
#            continue
        else:
            break

while True:
        try:
            userNameNapalm = str(input ("Please enter your username for HPNA: "))
        except ValueError:
            print ("That is not a valid entry.  Please try again.")
            continue
        else:
            break

while True:
        try:
            passWordNapalm = str(input ("Please enter your RSA token Password: "))
        except ValueError:
            print("That is not a valid entry.  Please try again.")
            continue
        else:
            break

########################################################
#####   Run Using the Captured Variables           #####
########################################################
convert(hostNameNapalm, userNameNapalm, passWordNapalm)
