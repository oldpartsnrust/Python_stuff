'''*********************************************************************************************
TUNNEL BUILD FUNCTION: Takes IP address and determines the correct configuration for the TUNNELS
*********************************************************************************************'''
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
    else:
        return 1

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
BUILDING OUT THE EIGRP FOR THE MPLS DIAL UP TUNNELS
*********************************************************************************************'''
def routerEIGRP(x, y, z):
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
distribute-list Eigrp-To-Tunnels out Tunnel1"+str(z)+"\n\
distribute-list Eigrp-To-Tunnels out Tunnel2"+str(z)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel1"+str(z)+"\n\
distribute-list Eigrp-From-Tunnels in Tunnel2"+str(z)+"\n\
no passive-interface Tunnel1"+str(z)+"\n\
no passive-interface Tunnel2"+str(z)+"\n")

    
'''*********************************************************************************************
DBU TYPE FUNCTION: Adds additional output for type of router needed such as Internet facing IP
address and ACL for 4G DBU or Dialer config for Internet Dial-up type DBU utilizing GlobalPops
*********************************************************************************************'''        
def dbuType(z):
    if (z)=="1":
        return print("!\n\
!\n\
!\n\
! This is a placeholder for 4G stuff\n\
\n")
    elif (z) == "2":
        return print("!\n\
!\n\
!\n\
! This ia a placeholder for GlobalPops stuff\n\
\n")
    else:
        return print("Invalid entry")
      
def routeBuild(a):
    return print("no ip route 10.16"+str(a)+".255.0 255.255.255.0 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
ip route "+str(tep)+" 255.255.255.255 Dialer1 250 name B2B-DBU-TUNNEL-DEST track 200\n\
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


'''****************************************************************************************************************
USER INPUT SECTION:
****************************************************************************************************************'''
router = input ("Enter the Router Type, 1 for MPLS, 2 for VPN: ")
if (router)== "1":
    model1 = input ("Select the MPLS router Model, '1' for 19xx, '2' for 28xx or '3' for 38xx :  ")
    model2 = "0"
elif (router)== "2":
    model2 = input ("Select the VPN router Model, '1' for G1-891, '2' for G2-891F, '3' for 1811, '4' for 1921, or '5' for 2811 : ")
    model1 = "0"
dbu = input ("Enter the type of backup connection, 1 for 4G Wireless, 2 for Internet DBU: ")
ip = input ("Enter the DBU tunnel IP address you were assigned: ")
if (dbu) == "1":
    dbuDialup = input ("Enter the router type, 1 for 891, 2 for 1800 series, 3 for 1900 series and 4 for 891F/ISR4K: ")    
elif (dbu) == "2":
    userName = input ("Enter the router name for Dial up authentication: ")
    passWord = input ("Enter the password for the Dial up authenatication: ")


'''****************************************************************************************************************
CONFIGURE VARIABLES:
****************************************************************************************************************'''
list = (ip.split("."))
zone = zoneValue(int(list[2]))
tunnel = tunnelValue(int(list[2]))
tuSub = tuSubValue(int(list[2]))
aS = asValue(zone)
site = [1, 3]


'''******************************************************************************************************************
PROGRAM SECTION:
******************************************************************************************************************'''
if (int(list[1]) == 161 or int(list[1]) == 163) and (int(list[3]) > 0 and int(list[3]) < 255):
    if int(list[0]) == 10:
        if tunnel != 1: 
            if (router) == "1":
                routerMPLS(router)
            elif (router) == "2":
                print ("\n")           
            else:
                print ("Invalid Router Type!:  "+(router))
            if (dbu) == "1":
                print ("This is not yet supported in this script.")
            elif (dbu) == "2":
                count = 0
                for l in site:
                  count += 1
                  tep = tepValue(zone, l, tunnel)
                  tunnelBuild(tunnel, zone, l, count, tuSub, tep)
                  routeBuild(l)
                dialBuild(aS, userName, passWord)
                if (router) == "1":
                    routerEIGRP(aS, tuSub, tunnel)
            else:
                print ("Invalid Backup Type!:  "+(dbu))
        else:
            print ("Invalid IP address!")
else:
    print ("Invalid IP address!")
print ("Model 1 = "+str(model1))
print ("Model 2 = "+str(model2))


