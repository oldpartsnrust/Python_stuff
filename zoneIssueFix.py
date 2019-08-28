import os
routerVPN = 0
routerMPLS = 0
username = "BLANKUSER"
password = "BLANKPASS"
existingVPNtunnel = 0
oldTunnel = 0
# Lists containing 3rd octet of tunnel IPs -
cnA1 = [4, 5, 8, 9, 12, 13]
cnA2 = [6, 7, 10, 11, 14, 15]
cnA100 = [80, 81]
cnA101 = [82, 83]
cnA102 = [118, 119]
cnA103 = [122, 123]
cnA200 = [84, 85]
cnA201 = [86, 87]
cnA202 = [120, 121]
cnA203 = [124, 125]

cnB1 = [18, 20, 22]
cnB2 = [19, 21, 23]
cnB100 = [94, 95]
cnB101 = [96, 97]
cnB200 = [98, 99]
cnB201 = [106, 107]


cnA4g = [cnA100, cnA101, cnA102, cnA103]
cnAdbu = [cnA200, cnA201, cnA202, cnA203]
cnAmpls = [cnA1, cnA2]

cnB4g = [cnB100, cnB101]
cnBdbu = [cnB200, cnB201]
cnBmpls = [cnB1, cnB2]

mpls = [cnAmpls, cnBmpls]
vpn = [cnA4g, cnB4g]
dbu = [cnAdbu, cnBdbu]

cnA = [cnA4g, cnAdbu, cnAmpls]
cnB = [cnB4g, cnBdbu, cnBmpls]
cnAandB = [cnA, cnB]

existingIPlist = [10, 161, 94, 12]
newIPlist = [10, 161, 122, 12]
site = [161, 163]
zone = "Z"
count = 0
zvAnew = 0
zvBnew = 0
zvAexisting = 0
zvBexisting = 0
routerMPLS = 0
routerVPN = 0
tvN = 0
tvE = 0


def zoneFunction(x):
    z = 0
    w = 0
    if (x >= 18 and x < 24) or (x >= 94 and x < 100) or (x >= 106 and x < 108):
        return "B"
    
    for i in cnA:
        for t in i:
            for b in t:
                if str(x) not in str(b):
                    z = z
                else:
                    z += 1
    if z >= 1:
        return "A"
    else:
        return "NONE"


Zone1 = (zoneFunction(int(newIPlist[2])))
Zone2 = (zoneFunction(int(existingIPlist[2])))
print (Zone1)
print (Zone2)
