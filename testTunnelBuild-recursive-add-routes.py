def tunnelBuild(x, zone, site, count, tuSub, tep):
    return print("no interface tunnel "+str(count)+str(x)+"\n\
interface Tunnel "+str(count)+str(x)+"\n\
 description DBU tunnel to USOMA1RTRCN"+(zone)+"24A-T"+str(x)+"\n\
 bandwidth 56\n\
 ip address 10.16"+str(site)+"."+str(tuSub)+"."+list[3]+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp "+str(aS)+" 4\n\
 ip hold-time eigrp "+str(aS)+" 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.16"+str(site)+"."+str(tuSub)+".1 "+str(tep)+"\n\
 ip nhrp map multicast "+str(tep)+"\n\
 ip nhrp network-id "+str(x)+"\n\
 ip nhrp nhs 10.16"+str(site)+"."+str(tuSub)+".1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination "+str(tep)+"\n\
 tunnel key "+str(x)+"\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n")

def siteValue(s):
  if s == "161":
    return 1
  elif s == "163":
    return 3

def zoneValue(s):
    if s > 87 and s < 120:
        return "B"
    else:
        return "A"
    
def tunnelValue(s):
    if s >= 84 and s < 86:
        return 200
    elif s >= 86 and s < 88:
        return 201
    elif s >= 120 and s < 122:
        return 202
    elif s >= 124 and s < 126:
        return 203
    elif s >= 98 and s < 100:
        return 200
    elif s >= 106 and s < 108:
        return 201

def tuSubValue(s):
    if s >= 84 and s < 86:
        return 84
    elif s >= 86 and s < 88:
        return 86
    elif s >= 120 and s < 122:
        return 120
    elif s >= 124 and s < 126:
        return 124
    elif s >= 98 and s < 100:
        return 98
    elif s >= 106 and s < 108:
        return 106

def tepValue(z, s, t):
    if z == "A":
        if s == 1:
            if t == 200:
                return "216.66.221.38"
            elif t == 201:
                return "216.66.221.39"
            elif t == 202:
                return "216.66.221.20"
            else:
                return "216.66.221.41"
        else:
            if t == 200:
                return "208.72.255.38"
            elif t == 201:
                return "208.72.255.39"
            elif t == 202:
                return "208.72.255.20"
            else:
                return "208.72.255.41"
    elif z == "B":
        if s == 1:
            if t == 200:
                return "216.66.221.42"
            elif t == 201:
                return "216.66.221.43"
        else:
            if t == 200:
                return "208.72.255.42"
            elif t == 201:
                return "208.72.255.43"

def asValue(z):
     if(z) == "A":
        return "65329"
     else:
        return "65342"
             
def routeBuild(a):
    return print("no ip route 10.16"+str(a)+".255.0 255.255.255.0 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
ip route "+str(tep)+" 255.255.255.255 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
\n")
                 
    

ip = input ("Enter the DBU tunnel IP address you were assigned: ")
list = (ip.split("."))

zone = zoneValue(int(list[2]))
x = tunnelValue(int(list[2]))
tuSub = tuSubValue(int(list[2]))
aS = asValue(zone)
site = [1, 3]

count = 0
for l in site:
  count += 1
  tep = tepValue(zone, l, x)
  tunnelBuild(x, zone, l, count, tuSub, tep)
  routeBuild(l)

    


                 
