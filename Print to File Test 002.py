
##### SET VARIABLES THAT MIGHT NOT BE SET FROM INPUT #####################################
#    This is where you add additional zones, tunnels, etc. if new prod stuff is added    #
##########################################################################################
import os
import sys
routerVPN = 0
routerMPLS = 0
username = "BLANKUSER"
password = "BLANKPASS"
hostNameNapalm = "BLANKHOSTNAMENAPALM"
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

existingIPlist = [0, 0, 0, 0]
newIPlist = [0, 0, 0, 0]
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




#####  DEFINE FUNCTIONS   #####################################################
#                Define Functions to create configs                           #
###############################################################################

# Building of the actual new VPN tunnels -
def tunnelBuild(tunnel, zone, site, count, interfaceIP, interface, publicIP):
    if site == 161:
        x = "OMA"
    elif site == 163:
        x = "CHD"
    else:
        x = "XXX"
    if tunnel >= 100 and tunnel < 200:
        y = " !"
        z = " rate-limit output 512000 96000 192000 conform-action transmit exceed-action drop"
        b = "512"
    elif tunnel >= 200:
        y = " delay 500000"
        z = " !"
        b = "56"
    else:
        y = "INVALID"
        z = "INVALID"
        b = "INVALID"
    if backup == 1:
        p = "shutdown"
    elif backup == 2:
        p = "no shutdown"
    else:
        p = "!"
    return print("no interface tunnel "+str(count)+str(tunnel)+"\n\
!\n\
interface Tunnel "+str(count)+str(tunnel)+"\n\
 "+str(p)+"\n\
 description DBU tunnel to US"+str(x)+"1RTRCN"+(zone)+"24A-T"+str(tunnel)+"\n\
 bandwidth "+str(b)+"\n\
 ip address 10."+str(site)+"."+newIPlist[2]+"."+newIPlist[3]+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp "+str(aS)+" 4\n\
 ip hold-time eigrp "+str(aS)+" 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10."+str(site)+"."+str(interfaceIP)+".1 "+str(publicIP)+"\n\
 ip nhrp map multicast "+str(publicIP)+"\n\
 ip nhrp network-id "+str(tunnel)+"\n\
 ip nhrp nhs 10."+str(site)+"."+str(interfaceIP)+".1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
"+str(z)+"\n\
 load-interval 30\n\
"+str(y)+"\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source "+str(interface)+"\n\
 tunnel destination "+str(publicIP)+"\n\
 tunnel key "+str(tunnel)+"\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
!")


# Building of the new routes needed for the Tunnel end points and removal of private routes (if necessary) -
def routeBuild(l, backup):
    print ("no ip route 10."+str(l)+".255.0 255.255.255.0 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
!")
    if (backup) == 2:
        return print("ip route "+str(publicIP)+" 255.255.255.255 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
!")


# Determination of the interfaces that will be used in configs based on router type
#(Ethernet for Internet, and Async for DBU) -
def internetInterface(router, routerMPLS, routerVPN):
    if backup == 1:
        if router == 1 and (routerMPLS == 1 or routerMPLS == 2 or routerMPLS == 3):
            return ["GigabitEthernet0/1", "A0/1/0"]
        elif router == 2 and routerVPN == 1: 
            return ["VLAN100", "A1"] 
        elif router == 2 and routerVPN == 2:
            return ["VLAN100", "A3"]
        elif router == 2 and routerVPN == 3:
            return ["FastEthernet0/1", "A1"]
        elif router == 2 and routerVPN == 4:
            return ["GigabitEthernet0/1", "A0/1/0"]
        elif router == 2 and routerVPN == 5:
            return ["FastEthernet0/1", "A0/1/0"]    
        else:
            return ["Dialer1", "NULL"]
    else:
        if router == 1 and (routerMPLS == 1 or routerMPLS == 2 or routerMPLS == 3):
            return ["dialer1", "A0/1/0"]
        elif router == 2 and routerVPN == 1: 
            return ["dialer1", "A1"] 
        elif router == 2 and routerVPN == 2:
            return ["dialer1", "A3"]
        elif router == 2 and routerVPN == 3:
            return ["dialer1", "A1"]
        elif router == 2 and routerVPN == 4:
            return ["dialer1", "A0/1/0"]
        elif router == 2 and routerVPN == 5:
            return ["dialer1", "A0/1/0"]
        else:
            return ["NULL", "NULL"]

# Search function to validate the IP entered is valid for an existing tunnel -
def findInList(x, y):
    z = 0
    for i in x:
        for t in i:
            if str(y) not in str(t):
                z = z
            else:
                z += 1
    if z > 0:
        return 1
    else:
        return 0


# Function to determine the zone that the tunnel resides in for comparison and AS determination -
def zoneFunction(x):
    z = 0
    w = 0
    if (x >= 18 and x < 24) or (x >= 94 and x < 99) or (x >= 106 and x < 108):
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


# Using the IP address 3rd octet to determine the actual tunnel number, regardless of zone -
def tunnelNumber(x):
    if x in cnA100 or x in cnB100:
        return 100
    elif x in cnA101 or x in cnB101:
        return 101
    elif x in cnA102:
        return 102
    elif x in cnA103:
        return 103
    elif x in cnA200 or x in cnB200:
        return 200
    elif x in cnA201 or x in cnB201:
        return 201
    elif x in cnA202:
        return 202
    elif x in cnA203:
        return 203
    elif x in cnA1 or x in cnB1:
        return 1
    elif x in cnA2 or x in cnB2:
        return 2
    else:
        return "NO TUNNEL"
    

# Determines the 3rd octet needed to add the tunnel NHRP value and network value I.E. 118 and 119 would = 118 -    
def tunnelIPvalue(s):
    if s % 2 == 0:
        return s
    else:
        return (s - 1)
    

# Determines the new Tunnel End Point value based on the new Tunnel IP -    
def tepValue(zone, site, tunnel):
    if site == 161:
        tep = "216.66.221."
    elif site == 163:
        tep = "208.72.255."
    else:
        tep = "X.X.X."
    if zone == "A":
        if tunnel == 200:
            return str(tep)+"38"
        elif tunnel == 201:
            return str(tep)+"39"
        elif tunnel == 202:
            return str(tep)+"20"
        elif tunnel == 203:
            return str(tep)+"41"
        elif tunnel == 100:
            return str(tep)+"6"
        elif tunnel == 101:
           return str(tep)+"7"
        elif tunnel == 102:
            return str(tep)+"14"
        elif tunnel == 103:
            return str(tep)+"15"
    elif zone == "B":
        if tunnel == 200:
            return str(tep)+"42"
        elif tunnel == 201:
            return str(tep)+"43"
        elif tunnel == 100:
            return str(tep)+"10"
        elif tunnel == 101:
            return str(tep)+"11"


# Determines the AS value which will be used for EIGRP based on the zone of the tunnels -
def asValue(zone):
    if (zone) == "A":
        return "65329"
    elif (zone) == "B":
        return "65342"
    else:
        return "INVALID"


# If needed, this will be added to the paste config calculated from user input -
def internetACL (router, backup):
    if router == 1:
        if backup == 1:
            return print ("ip access-list extended Internet-In\n\
 permit udp 208.72.255.0 0.0.0.15 any eq non500-isakmp\n\
 permit udp 208.72.255.0 0.0.0.15 any eq isakmp\n\
 permit udp 216.66.221.0 0.0.0.15 any eq non500-isakmp\n\
 permit udp 216.66.221.0 0.0.0.15 any eq isakmp\n\
 permit tcp 208.72.255.0 0.0.0.15 any eq 22\n\
 permit tcp 216.66.221.0 0.0.0.15 any eq 22\n\
 deny tcp any any log\n\
!\n\
ip access-list extended Internet-Out\n\
 permit udp any 208.72.255.0 0.0.0.15 eq isakmp\n\
 permit udp any 208.72.255.0 0.0.0.15 eq non500-isakmp\n\
 permit udp any 216.66.221.0 0.0.0.15 eq isakmp\n\
 permit udp any 216.66.221.0 0.0.0.15 eq non500-isakmp\n\
 permit tcp any eq 22 208.72.255.0 0.0.0.15\n\
 permit tcp any eq 22 216.66.221.0 0.0.0.15\n\
!\n\
!\n")
    else:
        return print ("!\n")


# This builds the 4G internet connected interface config based on router type -
def internetInterfaceBuild(routerMPLS, routerVPN):
    if backup == 1:
        if routerMPLS == 1 or routerVPN == 4:
            return print ("interface GigabitEthernet0/1\n\
 ip address 100.64.0.2 255.255.255.252\n\
 ip access-group Internet-In in\n\
 ip access-group Internet-Out out\n\
 duplex auto\n\
 speed auto\n\
 no shutdown\n\
!\n")
        elif routerMPLS == 2 or routerMPLS == 3 or routerVPN == 3 or routerVPN == 5:
            return print("interface FastEthernet0/1\n\
 ip address 100.64.0.2 255.255.255.252\n\
 ip access-group Internet-In in\n\
 ip access-group Internet-Out out\n\
 no shutdown\n\
!\n")
        elif routerVPN == 1:
            return print ("vlan 100\n\
 name AT&T4G\n\
exit\n\
!\n\
int vlan 100\n\
 desc Internet4G\n\
 ip address 100.64.0.2 255.255.255.252\n\
 ip access-group Internet-In in\n\
 ip access-group Internet-Out out\n\
 no shutdown\n\
!\n\
int fa7\n\
switchport access vlan 100\n\
no shut\n\
!\n")
        elif routerVPN == 2:
            return print ("vlan 100\n\
 name AT&T4G\n\
exit\n\
!\n\
int vlan 100\n\
 desc Internet4G\n\
 ip address 100.64.0.2 255.255.255.252\n\
 ip access-group Internet-In in\n\
 ip access-group Internet-Out out\n\
 no shutdown\n\
!\n\
int gi7\n\
switchport access vlan 100\n\
no shut\n\
!\n")
             

        else:
            return print ("Not a Valid Interface")
    else:
        return print ("!")


# This adds the crypto config, if necessary, which is determined via user input -
def routerCryptoBuild (router):
    if(router) == 1:
        return print("\n\
\n\
\n\
\n\
!\n\
!\n\
crypto isakmp key Ph3e5anT5 address 216.66.221.0 255.255.255.192\n\
crypto isakmp key Ph3e5anT5 address 208.72.255.0 255.255.255.192\n\
!\n\
crypto isakmp policy 10\n\
 encr aes 256\n\
 group 2\n\
!\n\
crypto isakmp policy 20\n\
 encr aes 256\n\
 authentication pre\n\
 group 2\n\
!\n\
crypto ipsec transform-set FDCAES esp-aes 256 esp-sha-hmac\n\
 mode transport\n\
!\n\
crypto ipsec profile B2B-DMVPN\n\
 set transform-set FDCAES\n\
!\n\
crypto isakmp keepalive 120 periodic\n\
crypto ipsec nat-transparency udp-encaps\n\
crypto isakmp aggressive-mode disable\n\
!\n\
!\n")

    
# This builds and adds the EEM config based on the user input and values calculated in the calculation section -
def addEEM (backup, count, TEP):
    tepList = ((tepValue(zone, site, tunnel)).split("."))
    tepRoute = str(tepList[3])
    if router == 1:
        if tvE == 2:
            tunnel1Number = int(tvE) - 1 
            tunnel2Number = int(tvE)
        else:
            tunnel1Number = int(tvE)
            tunnel2Number = int(tvE) + 1
    elif router == 2:
            tunnel1Number = int(tvE) + 1000
            tunnel2Number = int(tvE) + 2000
    if backup == 1:
        return print ('no ip route 10.175.183.1 255.255.255.255 Dialer2 250 name DBU-Testing-Route\n\
no ip route 167.16.0.0 255.255.255.0 Dialer1 250 name Dial-Route\n\
no ip route 204.194.120.0 255.255.248.0 Dialer1 250 name Dial-Route\n\
no ip route 204.194.128.0 255.255.240.0 Dialer1 250 name Dial-Route\n\
no ip route 206.201.48.0 255.255.240.0 Dialer1 250 name Dial-Route\n\
!\n\
int dialer 1\n\
shutdown\n\
int dialer 2\n\
shutdown\n\
no int dialer 1\n\
no int dialer 2\n\
default interface '+str(DialInt)+'\n\
no dialer watch-list 10\n\
no dialer-list 1\n\
no ip access-list standard Dbu-In\n\
no ip access-list standard Dbu-Out\n\
no ip access-list standard Dbutest-In\n\
no ip access-list standard Dbutest-Out\n\
no access-list 101\n\
!\n\
track 102 stub-object\n\
track 202 stub-object\n\
!\n\
Track 300 list Boolean and\n\
object 102\n\
object 202\n\
!\n\
event manager applet TRACKTUNNELADOWN\n\
event syslog pattern "Neighbor 10.161.'+str(existingTunnelIP)+'.1 [(]Tunnel'+str(tunnel1Number)+'[)] is down"\n\
action 1.0 syslog msg "Tunnel '+str(tunnel1Number)+' Neighbor DOWN"\n\
action 2.0 track set 102 state up\n\
!\n\
event manager applet TRACKTUNNELBDOWN\n\
 event syslog pattern "Neighbor 10.163.'+str(existingTunnelIP)+'.1 [(]Tunnel'+str(tunnel2Number)+'[)] is down"\n\
 action 1.0 syslog msg "Tunnel '+str(tunnel2Number)+' Neighbor DOWN"\n\
 action 2.0 track set 202 state up\n\
!\n\
event manager applet TRACKTUNNELAUP \n\
 event syslog pattern "Neighbor 10.161.'+str(existingTunnelIP)+'.1 [(]Tunne'+str(tunnel1Number)+'[)] is up"\n\
 action 1.0 syslog msg "Tunnel '+str(tunnel1Number)+' UP"\n\
 action 2.0 track set 102 state down\n\
!\n\
event manager applet TRACKTUNNELBUP\n\
event syslog pattern "Neighbor 10.163.'+str(existingTunnelIP)+'.1 [(]Tunnel'+str(tunnel2Number)+'[)] is up"\n\
 action 1.0 syslog msg "Tunnel '+str(tunnel2Number)+' UP"\n\
 action 2.0 track set 202 state down\n\
!\n\
no event manager applet 4GBackupUP\n\
event manager applet 4GBackupUP\n\
 event track 300 state up\n\
 action 1.0 syslog msg "On 4G Backup"\n\
 action 2.0 cli command "enable"\n\
 action 2.1 cli command "config t"\n\
 action 3.0 cli command "int tunnel '+str(count-1)+str(tunnel)+'"\n\
 action 3.1 cli command "no shut"\n\
 action 4.0 cli command "int tunnel '+str(count)+str(tunnel)+'"\n\
 action 4.1 cli command "no shut"\n\
 action 5.0 cli command "router eigrp '+str(aS)+'"\n\
 action 5.1 cli command "no passive-interface t'+str(count-1)+str(tunnel)+'"\n\
 action 5.2 cli command "no passive-interface t'+str(count)+str(tunnel)+'"\n\
 action 6.0 wait 10\n\
 action 6.1 syslog msg "%TRACKING-5-STATE: 300 list boolean and Down->Up"\n\
!\n\
no event manager applet 4GBackupDOWN\n\
event manager applet 4GBackupDOWN\n\
 event track 300 state down\n\
 action 1.0 syslog msg "4G Backup DOWN"\n\
 action 2.0 cli command "enable"\n\
 action 2.1 cli command "config t"\n\
 action 3.0 cli command "router eigrp '+str(aS)+'"\n\
 action 3.1 cli command "passive-interface t'+str(count-1)+str(tunnel)+'"\n\
 action 3.2 cli command "passive-interface t'+str(count)+str(tunnel)+'"\n\
 action 4.0 wait 10\n\
 action 5.0 cli command "enable"\n\
 action 5.1 cli command "config t"\n\
 action 6.0 cli command "int tunnel '+str(count-1)+str(tunnel)+'"\n\
 action 6.1 cli command "shut"\n\
 action 7.0 cli command "int tunnel '+str(count)+str(tunnel)+'"\n\
 action 7.1 cli command "shut"\n\
!\n\
ip route 216.66.221.'+str(tepRoute)+' 255.255.255.255 100.64.0.1\n\
ip route 208.72.255.'+str(tepRoute)+' 255.255.255.255 100.64.0.1\n\
!\n')
    

# This adds the EIGRP config for the new tunnels -
def routerEIGRP(aS, interfaceIP, tunnel):
    if router == 1:
        return print("!\n\
!\n\
!\n\
router eigrp "+str(aS)+"\n\
network 10.161."+str(interfaceIP)+".0 0.0.1.255\n\
network 10.163."+str(interfaceIP)+".0 0.0.1.255\n\
no distribute-list Dbu-Out out Dialer1\n\
no distribute-list Dbu-In in Dialer1\n\
no distribute-list Dbutest-Out out Dialer2\n\
no distribute-list Dbutest-In in Dialer2\n\
distribute-list Eigrp-To-Tunnels out Tunnel"+str(count-1)+str(tunnel)+"\n\
distribute-list Eigrp-To-Tunnels out Tunnel"+str(count)+str(tunnel)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel"+str(count-1)+str(tunnel)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel"+str(count)+str(tunnel)+"\n\
passive-interface Tunnel"+str(count-1)+str(tunnel)+"\n\
passive-interface Tunnel"+str(count)+str(tunnel)+"\n")
    elif router == 2:
        return print ("!\n\
!\n\
!\n\
router eigrp "+str(aS)+"\n\
network 10.161."+str(interfaceIP)+".0 0.0.1.255\n\
network 10.163."+str(interfaceIP)+".0 0.0.1.255\n\
distribute-list Eigrp-To-Tunnels out Tunnel"+str(count-1)+str(tunnel)+"\n\
distribute-list Eigrp-To-Tunnels out Tunnel"+str(count)+str(tunnel)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel"+str(count-1)+str(tunnel)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel"+str(count)+str(tunnel)+"\n\
no passive-interface Tunnel"+str(count-1)+str(tunnel)+"\n\
no passive-interface Tunnel"+str(count)+str(tunnel)+"\n")


# This adds the dialer config for new Internet Dialup conversion -
def dialBuild(aS, username, password):
    if backup == 2:
        if (routerVPN) == 1:
            print ("no chat-script DIALV34")
            print ('chat-script DIALV34 ABORT ERROR ABORT BUSY "" "ATZ" OK "AT+MS=V34" OK "ATDT \T"  TIMEOUT 90 CONNECT \c')
        elif (routerVPN) == 2:
            print ("no chat-script DIALV34")
            print ('chat-script DIALV34 ABORT ERROR ABORT BUSY "" "ATZ" OK "AT\\\\n4%c0" OK "ATDT \T" TIMEOUT 90 CONNECT \c\n\
modemcap entry silabs:MSC=&f&g13%c0+ds=0;ms=v34,1,2400,24000,2400,24000\n\
modemcap entry v42:MSC=f&\\n4%c0+ms=v32')
        print ("dialer watch-list 10 ip 204.194.120.0 255.255.255.0\n\
dialer watch-list 10 ip 204.194.121.0 255.255.255.0\n\
!\n\
!\n\
interface "+str(DialInt)+"\n\
 bandwidth 28\n\
 no ip address\n\
 encapsulation ppp\n\
 dialer in-band\n\
 dialer pool-member 1\n\
 async mode interactive\n\
 no keepalive\n\
 ppp authentication chap callin\n\
 fair-queue\n\
 no shutdown\n\
\n\
\n\
interface Dialer1\n\
 description Dialer1 for Production Traffic\n\
 bandwidth 6\n\
 ip address negotiated\n\
 encapsulation ppp\n\
 dialer pool 1\n\
 dialer idle-timeout 300")
        if ((routerVPN) == 1 or (routerVPN) == 2):
                print (" dialer string 18445214686 modem-script DIALV34")
        else:
                print (" dialer string 18445214686")
        print (" dialer watch-group 10\n\
 dialer-group 1\n\
 ppp authentication chap callin\n\
 ppp pap sent-username "+str(username)+"@firstdata.com password "+str(password)+"\n\
 service-policy output Client_Traffic_Out\n\
 no shutdown")

# Removes the unused Old Tunnel interfaces for VPN routers with 4G backup -
def removeOldTunnel(router, backup, tvE):
    if router == 2:
        if backup == 1:
            oldTunnel = (tvE) + 100
            print('no interface tunnel 1'+str(oldTunnel)+'\n\
no interface tunnel 2'+str(oldTunnel)+'\n\
!\n\
!\n\
!')
            return (tvE) + 100 

# Resets Dialer and Async line interfaces to default values so they can be configured fresh -
def defaultInterfaces(DialInt, backup):
    if backup == 2:
        return print("interface dialer 1\n\
shutdown\n\
exit\n\
default interface dialer 1\n\
interface "+str(DialInt)+"\n\
shutdown\n\
exit\n\
default interface "+str(DialInt)+"\n\
interface "+str(DialInt)+"\n\
no shutdown\n\
track 200 interface "+str(DialInt)+" line-protocol\n\
!\n\
!\n\
!")


#####  GATHER INPUT ###########################################################
#                     Router Type, MPLS or VPN                                #
###############################################################################
os.system('cls')


while True:
    try:
        hostNameNapalm = str(input ("Please enter the host IP address that you plan to convert: "))
    except ValueError:
        print ("That is not a valid entry.  Please try again.")
        continue
    if hostNameNapalm == "":
        print ("That is not a valid entry.  Please try again.")
        continue
    hostNameNapalmList = (hostNameNapalm.split("."))
    if len(hostNameNapalmList) != 4:
        print("This IP is too short, please try again: ")
        continue
#    if int(hostNameNapalmList[0]) != 10:
#        print ("This is not a correct IP for a host, your 1st octet is invalid. ")
#        continue
#    if int(hostNameNapalmList[1]) != 189 and int (hostNameNapalmList[1]) != 173:
#        print ("This is not a Loopback 2 IP address, please enter a Loopback 2 IP: ")
#        continue
    if (hostNameNapalmList[2]) == "" or int(hostNameNapalmList[2]) == 0 or int(hostNameNapalmList[2]) > 254:
        print ("This is not a Loopback 2 IP address, please enter a Loopback 2 IP: ")
        continue
    if (hostNameNapalmList[3]) == "" or int(hostNameNapalmList[3]) == 0 or int(hostNameNapalmList[3]) > 254:
        print ("This is not a Loopback 2 IP address, please enter a Loopback 2 IP: ")
        continue    
    else:
        break



while True:
    try:
        router = int(input ("Please enter the router type: \n\
'1' for MPLS \n\
'2' for VPN\n\
: "))
    except ValueError:
            print ("That is not a valid Selection.  Please try again.")
            continue
    if (router) != 1 and (router) != 2:
        print ("Please select '1' or '2' :")        
    else:
        break

##### Backup Type, 4G or Internet Dialup -
while True:
    try:
        backup = int(input ("Please enter the backup type you are installing: \n\
'1' for 4G Wireless \n\
'2' for Internet Dialup \n\
: "))
    except ValueError:
            print ("That is not a valid Selection.  Please try again.")
            continue
    if (backup) != 1 and (backup) != 2:
        print ("Please select '1' or '2' :")        
    else:
        break


##### MPLS and VPN Router Model Selections -
if router == 1:
    while True:
        try:
            routerMPLS = int(input ("Please enter the MPLS router model: \n\
'1' for 1900 Series \n\
'2' for 2900 Series \n\
'3' for 3900 Series \n\
: "))
        except ValueError:
                print ("That is not a valid Selection.  Please try again.")
                continue
        if (routerMPLS) != 1 and (routerMPLS) != 2 and (routerMPLS) != 3:
            print ("Please select '1', '2' or '3' :")        
        else:
            break
elif router == 2:
    while True:
        try:
            routerVPN = int(input ("Please enter the VPN router model: \n\
'1' for 891 \n\
'2' for 891F \n\
'3' for 1800 Series \n\
'4' for 1900 Series \n\
'5' for 2800 Series \n\
: "))
        except ValueError:
                print ("That is not a valid Selection.  Please try again.")
                continue
        if (routerVPN) != 1 and (routerVPN) != 2 and (routerVPN) != 3 and (routerVPN) != 4 and (routerVPN) != 5:
            print ("Please select '1', '2' or '3' :")        
        else:
            break
else:
    print ("Invalid Router Selection!")

        

##### Additional info needed for DBU #####

if backup == 2:
    while True:
        try:
            username = str(input ("Please enter the router name which will be used for GlobalPops authentication: "))
        except ValueError:
                print ("That is not a valid entry.  Please try again.")
                continue
        else:
            break
    while True:
        try:
            password = str(input ("Please enter the password which will be used for GlobalPops authentication: "))
        except ValueError:
                print ("That is not a valid entry.  Please try again.")
                continue
        else:
            break

##### Additional info for Existing Tunnels #####

if router == 1:
    while True:
        try:
            existingTunnel = str(input ("Please enter one of the existing MPLS VPN tunnel IP addresses: "))
        except ValueError:
            print ("That is not a valid entry.  Please try again.")
            continue
        if existingTunnel == "":
            print ("That is not a valid entry.  Please try again.")
            continue
        existingIPlist = (existingTunnel.split("."))
        if len(existingIPlist) != 4:
            print("That IP is too short! Please try again: ")
            continue
        if int(existingIPlist[0]) != 10:
            print ("This is not a correct IP for these tunnels your 1st octet is invalid. ")
            continue
        if int(existingIPlist[1]) != 161 and int(existingIPlist[1]) != 163:
            print ("This is not a correct IP for these tunnels your second octet is invalid. ")
            continue
        if int(existingIPlist[2]) < 1 or int(existingIPlist[2]) > 23:
            print ("This is not one of the MPLS VPN tunnel IPs, 3rd octet is invalid. ")
            continue
        if (existingIPlist[3]) == "" or int(existingIPlist[3]) == 0 or int(existingIPlist[3]) > 254:
            print("This is not a valid IP.  Please try again: ")
            continue
        else:
            break


if router == 2:
    while True:
        try:
            existingTunnel = str(input ("Please enter one of the existing VPN tunnel IP addresses: "))
        except ValueError:
            print ("That is not a valid entry.  Please try again.")
            continue
        existingIPlist = (existingTunnel.split("."))
        if int(existingIPlist[0]) != 10:
            print ("This is not a correct IP for these tunnels your 1st octet is invalid. ")
            continue
        if int(existingIPlist[1]) != 161 and int(existingIPlist[1]) != 163:
            print ("This is not a correct IP for these tunnels your second octet is invalid. ")
            continue
        if int(findInList(vpn, (existingIPlist[2]))) < 1:
            print (findInList((existingIPlist[2]), vpn))
            print ("This is not one of the VPN tunnel IPs, 3rd octet is invalid. ")
            continue
        if backup == 1 and (tunnelNumber(int(existingIPlist[2])) > 199 or tunnelNumber(int(existingIPlist[2])) < 3):
            print ("This tunnel IP is for Dialup (56Kb/S) or MPLS, you need to enter a Tunnel 100 - 103 IP. ")
            continue
        if int(existingIPlist[3]) < 0 or int(existingIPlist[3]) > 255:
            print ("Please enter a valid IP, your 4th octet is invalid. ")
            continue
        else:
            break



##### Enter IP address for the new Tunnel for VPN (Either 4G Wireless OR Internet Dialup).

while True:
    try:
        newTunnel = str(input ("Please enter one of the the IP addresses of one of the\n\
new VPN tunnels you will be building: "))
    except ValueError:
        print ("That is not a valid entry.  Please try again.")
        continue
    newIPlist = (newTunnel.split("."))
    if len(newIPlist) != 4:
        print("This IP is too short!  Please try again: ")
        continue
    if int(newIPlist[0]) != 10:
        print ("This is not a correct IP for these tunnels your 1st octet is invalid. ")
        continue
    if int(newIPlist[1]) != 161 and int(newIPlist[1]) != 163:
        print ("This is not a correct IP for these tunnels your second octet is invalid. ")
        continue
    if findInList(cnAandB, str(newIPlist[2])) < 1:
        print ("This is not one of the VPN tunnel IPs, 3rd octet is invalid. ")
        continue
    if backup == 1 and tunnelNumber(int(newIPlist[2])) > 199:
        print ("This tunnel is for Dialup (56Kb/S), you need a High-bandwidth tunnel (100-103)\n\
OTHER than any currently being used on this router. ")
        continue
    if backup == 2 and (tunnelNumber(int(newIPlist[2])) < 199 and tunnelNumber(int(newIPlist[2]) > 2)):
        print ("This tunnel is for a High Bandwidth connection (4G, Broadband Internet)\n\
Please enter a low bandwidth tunnel IP (200 - 203). ")
        continue
    if int(newIPlist[2]) == int(existingIPlist[2]):
        print ("The existing VPN tunnel and new VPN tunnel cannot be the same. ")
        continue
    if (findInList(mpls, str(newIPlist[2]))) == 1:
        print ("The new VPN tunnel cannot be MPLS with this script. ")
        continue
    if (newIPlist[3])== "" or int(newIPlist[3]) <= 0 or int(newIPlist[3]) > 255:
        print ("Please enter a valid IP, your 4th octet is invalid. ")
        continue
    if (router == 1 or router == 2) and ((zoneFunction(int(newIPlist[2]))) != (zoneFunction(int(existingIPlist[2])))):
        print ("These tunnels are in different Zones.")
        continue
    else:
        break

##############################################################
#####      Run Functions to get Tunnel #s, AS, etc.      #####
##############################################################
if backup == 1:
    count = 7
else:
    count = 0
tvN = tunnelNumber(int(newIPlist[2]))
tvE = tunnelNumber(int(existingIPlist[2]))
zone = zoneFunction(int(newIPlist[2]))
interfaceIP = tunnelIPvalue(int(newIPlist[2]))
existingTunnelIP = tunnelIPvalue(int(existingIPlist[2]))
tunnel = tunnelNumber(int(newIPlist[2]))
publicIP = tepValue(zone, (int(newIPlist[1])), tvN)
aS = asValue(zone)
TEP = tepValue(zone, site, tunnel)
interface = internetInterface(router, routerMPLS, routerVPN)
DialInt = (interface[1])

##### RUN PROGRAM TO GENERATE OUTPUT FILE
#os.system('cls')
sys.stdout=open((hostNameNapalm)+".txt", "w")
routerCryptoBuild (router)
internetACL (router, backup)
oldTunnel = removeOldTunnel(router, backup, tvE)
defaultInterfaces(DialInt, backup)
internetInterfaceBuild(routerMPLS, routerVPN)
for l in site:
    count += 1
    publicIP = tepValue(zone, l, tunnel)
    tunnelBuild(tunnel, zone, l, count, interfaceIP, (interface[0]), publicIP)
    routeBuild(l, backup)
addEEM (backup, count, TEP)
routerEIGRP(aS, interfaceIP, tunnel)
dialBuild(aS, username, password)
sys.stdout.close()


        

