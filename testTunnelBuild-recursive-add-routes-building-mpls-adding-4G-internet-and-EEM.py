'''*********************************************************************************************
TUNNEL BUILD FUNCTION: Takes IP address and determines the correct configuration for the TUNNELS
*********************************************************************************************'''
def tunnelBuild(tunnel, zone, site, count, tuSub, tep, internet):
    if site == 1:
        x = "OMA"
    else:
        x = "CHD"
    if tunnel >= 100 and tunnel < 200:
        y = ""
        z = " rate-limit output 512000 96000 192000 conform-action transmit exceed-action drop"
    else:
        y = " delay = 50000"
        z = ""
    return print("no interface tunnel "+str(count)+str(tunnel)+"\n\
interface Tunnel "+str(count)+str(tunnel)+"\n\
 description DBU tunnel to US"+str(x)+"1RTRCN"+(zone)+"24A-T"+str(tunnel)+"\n\
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
 ip nhrp network-id "+str(tunnel)+"\n\
 ip nhrp nhs 10.16"+str(site)+"."+str(tuSub)+".1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
"+str(z)+"\n\
 load-interval 30\n\
"+str(y)+"\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source "+str(internet)+"\n\
 tunnel destination "+str(tep)+"\n\
 tunnel key "+str(tunnel)+"\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n")


'''*********************************************************************************************
Sub functions for TUNNEL Build: Uses input for Tunnel IP and builds variables for Tunnel build
*********************************************************************************************'''
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
    if s >= 80 and s < 82:
        return 100
    elif s >= 82 and s < 84:
        return 101
    elif s >= 118 and s < 120:
        return 102
    elif s >= 122 and s < 124:
        return 103
    elif s >= 94 and s < 96:
        return 100
    elif s >= 96 and s < 98:
        return 101
    elif s >= 84 and s < 86:
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
    else:
        return 1

def tuSubValue(s):
    if s >= 80 and s < 82:
        return 80
    elif s >= 82 and s < 84:
        return 82
    elif s >= 118 and s < 120:
        return 118
    elif s >= 122 and s < 124:
        return 122
    elif s >= 94 and s < 96:
        return 94
    elif s >= 96 and s < 98:
        return 96
    elif s >= 84 and s < 86:
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
    else:
        return 1

def tepValue(z, s, t):
    if z == "A":
        if s == 1:
            if t == 200:
                return "216.66.221.38"
            elif t == 201:
                return "216.66.221.39"
            elif t == 202:
                return "216.66.221.20"
            elif t == 203:
                return "216.66.221.41"
            elif t == 100:
                return "216.66.221.6"
            elif t == 101:
                return "216.66.221.7"
            elif t == 102:
                return "216.66.221.14"
            elif t == 103:
                return "216.66.221.15"
        else:
            if t == 200:
                return "208.72.255.38"
            elif t == 201:
                return "208.72.255.39"
            elif t == 202:
                return "208.72.255.20"
            elif t == 203:
                return "208.72.255.41"
            elif t == 100:
                return "208.72.255.6"
            elif t == 101:
                return "208.72.255.7"
            elif t == 102:
                return "208.72.255.14"
            elif t == 103:
                return "208.72.255.15"
    elif z == "B":
        if s == 1:
            if t == 200:
                return "216.66.221.42"
            elif t == 201:
                return "216.66.221.43"
            elif t == 100:
                return "216.66.221.10"
            elif t == 101:
                return "216.66.221.11"
        else:
            if t == 200:
                return "208.72.255.42"
            elif t == 201:
                return "208.72.255.43"
            elif t == 100:
                return "208.72.255.10"
            elif t == 101:
                return "208.72.255.11"

def asValue(z):
     if(z) == "A":
        return "65329"
     else:
        return "65342"


'''*********************************************************************************************
ROUTER INTERNET ACL:
*********************************************************************************************'''
def internetACL (router, dbu):
    if router == "1":
        if dbu == "1":
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
    

'''*********************************************************************************************
INTERFACE SELECTION FOR 4G INTERNET:
*********************************************************************************************'''
def internetInterface(model1, model2):
    if model1 == "1" or model2 == "4":
        return "GigabitEthernet0/1"
    elif model1 == "2" or model1 == "2" or model2 == "3" or model2 == "5":
        return "FastEthernet0/1"
    elif model2 == "1" or model2 == "2":
        return "VLAN100"
    else:
        return "Dialer1"

'''*********************************************************************************************
INTERFACE BUILD FOR 4G INTERNET:
*********************************************************************************************'''
def internetInterfaceBuild(x, y):
    if model1 == "1" or model2 == "4":
        return print ("interface GigabitEthernet0/1\n\
ip address 100.64.0.2 255.255.255.252\n\
ip access-group Internet-In in\n\
ip access-group Internet-Out out\n\
no shutdown\n\
!\n")
    elif model1 == "2" or model1 == "2" or model2 == "3" or model2 == "5":
        return print("interface FastEthernet0/1\n\
ip address 100.64.0.2 255.255.255.252\n\
ip access-group Internet-In in\n\
ip access-group Internet-Out out\n\
no shutdown\n\
!\n")
    elif model2 == "1" or model2 == "2":
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

    else:
        return print ("Not a Valid Interface")


'''*********************************************************************************************
ROUTER TYPE FUNCTION: Adds additional output as needed for current router type conversions
I.E. MPLS router requires additional crypto info, but VPN router does not require additional
*********************************************************************************************'''
def routerMPLS (z):
    if(z) == "1":
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
    elif(z)=="2":
        return print("!\n")
    else:
        return print("Invalid Entry")


'''*********************************************************************************************
BUILDING OUT THE EEM for VPN 4G ROUTERS
*********************************************************************************************'''
def addEEM (dbu, count, tep):
    list = (tep.split("."))
    tepRoute = str(list[3]) 
    count += 1
    if dbu == "1":
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
default interface BRI0/1/0\n\
default interface A0/1/0\n\
default interface A1\n\
default interface A3\n\
no dialer watch-list 10\n\
no dialer-list 1\n\
no ip access-list standard Dbu-In\n\
no ip access-list standard Dbu-Out\n\
no ip access-list standard Dbutest-In\n\
no ip access-list standard Dbutest-Out\n\
no access-list 101\n\
!\n\
track 101 stub-object\n\
track 102 stub-object\n\
!\n\
Track 300 list Boolean and\n\
object 101\n\
object 102\n\
!\n\
event manager applet TRACKTUNNELADOWN\n\
event syslog pattern "Neighbor 10.161.'+str(tuSub)+'.1 [(]Tunnel1[)] is down"\n\
action 1.0 syslog msg "Tunnel 1 Neighbor DOWN"\n\
action 2.0 track set 101 state up\n\
!\n\
event manager applet TRACKTUNNELBDOWN\n\
 event syslog pattern "Neighbor 10.163.'+str(tuSub)+'.1 [(]Tunnel2[)] is down"\n\
 action 1.0 syslog msg "Tunnel 2 Neighbor DOWN"\n\
 action 2.0 track set 102 state up\n\
!\n\
event manager applet TRACKTUNNELAUP \n\
 event syslog pattern "Neighbor 10.161.'+str(tuSub)+'.1 [(]Tunnel1[)] is up"\n\
 action 1.0 syslog msg "Tunnel 1 UP"\n\
 action 2.0 track set 101 state down\n\
!\n\
event manager applet TRACKTUNNELBUP\n\
event syslog pattern "Neighbor 10.163.'+str(tuSub)+'.1 [(]Tunnel2[)] is up"\n\
 action 1.0 syslog msg "Tunnel 2 UP"\n\
 action 2.0 track set 102 state down\n\
!\n\
no event manager applet 4GBackupUP\n\
event manager applet 4GBackupUP\n\
 event track 300 state up\n\
 action 1.0 syslog msg "On 4G Backup"\n\
 action 2.0 cli command "enable"\n\
 action 2.1 cli command "config t"\n\
 action 3.0 cli command "int tunnel '+str(count)+str(tunnel)+'"\n\
 action 3.1 cli command "no shut"\n\
 action 4.0 cli command "int tunnel '+str(count+1)+str(tunnel)+'"\n\
 action 4.1 cli command "no shut"\n\
 action 5.0 cli command "router eigrp '+str(aS)+'"\n\
 action 5.1 cli command "no passive-interface t'+str(count)+str(tunnel)+'"\n\
 action 5.2 cli command "no passive-interface t'+str(count+1)+str(tunnel)+'"\n\
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
 action 3.1 cli command "passive-interface t'+str(count)+str(tunnel)+'"\n\
 action 3.2 cli command "passive-interface t'+str(count+1)+str(tunnel)+'"\n\
 action 4.0 wait 10\n\
 action 5.0 cli command "enable"\n\
 action 5.1 cli command "config t"\n\
 action 6.0 cli command "int tunnel '+str(count)+str(tunnel)+'"\n\
 action 6.1 cli command "shut"\n\
 action 7.0 cli command "int tunnel '+str(count+1)+str(tunnel)+'"\n\
 action 7.1 cli command "shut"\n\
!\n\
ip route 216.66.221.'+str(tepRoute)+' 255.255.255.255 100.64.0.1\n\
ip route 208.72.255.'+str(tepRoute)+' 255.255.255.255 100.64.0.1\n\
!\n\"')


'''*********************************************************************************************
BUILDING OUT THE EIGRP FOR THE MPLS DIAL UP TUNNELS
*********************************************************************************************'''
def routerEIGRPmpls(x, y, z):
    return print("!\n\
!\n\
!\n\
router eigrp "+str(x)+"\n\
network 10.161."+str(y)+".0 0.0.1.255\n\
network 10.163."+str(y)+".0 0.0.1.255\n\
no distribute-list Dbu-Out out Dialer1\n\
no distribute-list Dbu-In in Dialer1\n\
no distribute-list Dbutest-Out out Dialer2\n\
no distribute-list Dbutest-In in Dialer2\n\
distribute-list Eigrp-To-Tunnels out Tunnel"+str(count)+str(z)+"\n\
distribute-list Eigrp-To-Tunnels out Tunnel"+str(count+1)+str(z)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel"+str(count)+str(z)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel"+str(count+1)+str(z)+"\n\
passive-interface Tunnel"+str(count)+str(z)+"\n\
passive-interface Tunnel"+str(count+1)+str(z)+"\n")

    
'''*********************************************************************************************
DBU TYPE FUNCTION: Adds additional output for type of router needed such as Internet facing IP
address and ACL for 4G DBU or Dialer config for Internet Dial-up type DBU utilizing GlobalPops
*********************************************************************************************'''       

      
def routeBuild(a, dbu):
    print ("no ip route 10.16"+str(a)+".255.0 255.255.255.0 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200")
    if (dbu) == "2":
        return print("ip route "+str(tep)+" 255.255.255.255 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
\n")


'''****************************************************************************************************************
DBU TYPE BUILDS:
****************************************************************************************************************'''
def dialBuild(x, y, z):
    return print ("no interface Dialer 1\n\
interface Dialer1\n\
 description Dialer1 for Production Traffic\n\
 bandwidth 6\n\
 ip address negotiated\n\
 ip hello-interval eigrp "+str(x)+" 4\n\
 ip hold-time eigrp "+str(x)+" 12\n\
 encapsulation ppp\n\
 dialer pool 1\n\
 dialer idle-timeout 300\n\
 dialer string 18445214686\n\
 dialer watch-group 10\n\
 dialer-group 1\n\
 ppp authentication chap callin\n\
 ppp pap sent-username "+str(y)+"@firstdata.com password "+str(z)+"\n\
 service-policy output Client_Traffic_Out\n")


'''****************************************************************************************************************
ROUTER TYPE/MODEL SELECTION:
****************************************************************************************************************'''

def asyncInterface (model1, model2):
    if model1 == "1" or model1 == "2":
        return "A0/1/0"
    elif model1 == "3":
        return "A0/1/0"
    if model2 == "1" or model2 == "3":
        return "A1"
    elif model2 == "2":
        return "A3"
    elif model2 == "4" or model2 == "5":
        return "A0/1/0"
    else:
        return "0"


'''****************************************************************************************************************
USER INPUT SECTION:
****************************************************************************************************************'''
router = input ("Enter the Router Type, 1 for MPLS, 2 for VPN: ")
if (router)== "1":
    model1 = input ("Select the MPLS router Model, '1' for 19xx, '2' for 28xx or '3' for 38xx :  ")
    model2 = "0"
elif (router)== "2":
    model2 = input ("Select the VPN router Model, '1' for G1-891, '2' for G2-891F, '3' for 18xx, '4' for 19xx, or '5' for 28xx : ")
    model1 = "0"
dbu = input ("Enter the type of backup connection, 1 for 4G Wireless, 2 for Internet DBU: ")
ip = input ("Enter the DBU tunnel IP address you were assigned: ")
if (dbu) == "2":
    userName = input ("Enter the router name for Dial up authentication: ")
    passWord = input ("Enter the password for the Dial up authenatication: ")


'''****************************************************************************************************************
CONFIGURE VARIABLES FROM INPUT:
****************************************************************************************************************'''
list = (ip.split("."))
zone = zoneValue(int(list[2]))
tunnel = tunnelValue(int(list[2]))
tep = tepValue(zone, 1, tunnel)
tuSub = tuSubValue(int(list[2]))
aS = asValue(zone)
site = [1, 3]
async = asyncInterface (model1, model2)
internet = internetInterface(model1, model2)
if dbu == "1":
    count = 7
else:
    count = 0

'''******************************************************************************************************************
PROGRAM SECTION:
******************************************************************************************************************'''
if (int(list[1]) == 161 or int(list[1]) == 163) and (int(list[3]) > 0 and int(list[3]) < 255):
    if int(list[0]) == 10:
        if tunnel != 1:
            if (router) == "1":
                routerMPLS(router)
            if (dbu) == "1":
                internetACL (router, dbu)
                addEEM (dbu, count, tep)
                internetInterfaceBuild(model1, model2)
            for l in site:
                count += 1
                tep = tepValue(zone, l, tunnel)
                tunnelBuild(tunnel, zone, l, count, tuSub, tep, internet)
                routeBuild(l, dbu)
            if (dbu) == "2":
                dialBuild(aS, userName, passWord)
            if (router) == "1":
                count -= 1
                routerEIGRPmpls(aS, tuSub, tunnel)
        else:
            print ("Invalid IP address!")
    else:
        print ("Invalid IP address!")
else:
    print ("Invalid IP address!")



