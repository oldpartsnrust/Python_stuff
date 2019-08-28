def dialTunnelVPNa(ipOMAa):
                if ".84." in (ipOMAa) or ".85." in (ipOMAa):
                        return 200
                elif ".86." in (ipOMAa) or ".87." in (ipOMAa):
                        return 201
                elif ".120." in (ipOMAa) or ".121." in (ipOMAa):
                        return 202
                elif ".124." in (ipOMAa) or ".125." in (ipOMAa):
                        return 203

def tunnelCNA(tunnel):
  if (dialTunnelVPNa(ipOMAa)) == 200:
        return tunnel200CNA()
  elif (dialTunnelVPNa(ipOMAa)) == 201:
        return tunnel201CNA()
  elif (dialTunnelVPNa(ipOMAa)) == 202:
        return tunnel202CNA()
  elif (dialTunnelVPNa(ipOMAa)) == 203:
        return tunnel203CNA()
  else:
       return print("Invalid entry")

               

def tunnel200CNA():
        return print("no interface tunnel 1200\n\
no interface tunnel 2200\n\
\n\
interface Tunnel1200\n\
 description DBU tunnel to USOMA1RTRCNA24A-T200\n\
 bandwidth 56\n\
 ip address "+(ipOMAa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.161.84.1 216.66.221.38\n\
 ip nhrp map multicast 216.66.221.38\n\
 ip nhrp network-id 200\n\
 ip nhrp nhs 10.161.84.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 216.66.221.38\n\
 tunnel key 200\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n\
 interface Tunnel2200\n\
 description DBU tunnel to USCHD1RTRCNA24A-T200\n\
 bandwidth 56\n\
 ip address "+(ipCHDa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.163.84.1 208.72.255.38\n\
 ip nhrp map multicast 208.72.255.38\n\
 ip nhrp network-id 200\n\
 ip nhrp nhs 10.163.84.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 208.72.255.38\n\
 tunnel key 200\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n")


def tunnel201CNA():
        return print("no interface tunnel 1201\n\
no interface tunnel 2201\n\
\n\
interface Tunnel1201\n\
 description DBU tunnel to USOMA1RTRCNA24A-T201\n\
 bandwidth 56\n\
 ip address "+(ipOMAa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.161.86.1 216.66.221.39\n\
 ip nhrp map multicast 216.66.221.39\n\
 ip nhrp network-id 201\n\
 ip nhrp nhs 10.161.86.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 216.66.221.39\n\
 tunnel key 201\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n\
 interface Tunnel2201\n\
 description DBU tunnel to USCHD1RTRCNA24A-T201\n\
 bandwidth 56\n\
 ip address "+(ipCHDa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.163.86.1 208.72.255.39\n\
 ip nhrp map multicast 208.72.255.39\n\
 ip nhrp network-id 201\n\
 ip nhrp nhs 10.163.86.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 208.72.255.39\n\
 tunnel key 201\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n")

def tunnel202CNA():
        return print("no interface tunnel1202\n\
no interface tunnel 2202\n\
\n\
interface Tunnel1202\n\
 description DBU tunnel to USOMA1RTRCNA24A-T202\n\
 bandwidth 56\n\
 ip address "+(ipOMAa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.161.120.1 216.66.221.20\n\
 ip nhrp map multicast 216.66.221.20\n\
 ip nhrp network-id 202\n\
 ip nhrp nhs 10.161.120.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 216.66.221.20\n\
 tunnel key 202\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n\
 interface Tunnel2202\n\
 description DBU tunnel to USCHD1RTRCNA24A-T202\n\
 bandwidth 56\n\
 ip address "+(ipCHDa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.163.120.1 208.72.255.20\n\
 ip nhrp map multicast 208.72.255.20\n\
 ip nhrp network-id 202\n\
 ip nhrp nhs 10.163.120.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 208.72.255.20\n\
 tunnel key 202\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n")


def tunnel203CNA():
        return print("no interface tunnel1203\n\
no interface tunnel 2203\n\
\n\
interface Tunnel1203\n\
 description DBU tunnel to USOMA1RTRCNA24A-T203\n\
 bandwidth 56\n\
 ip address "+(ipOMAa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.161.124.1 216.66.221.41\n\
 ip nhrp map multicast 216.66.221.41\n\
 ip nhrp network-id 203\n\
 ip nhrp nhs 10.161.124.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 216.66.221.41\n\
 tunnel key 203\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n\
 interface Tunnel2203\n\
 description DBU tunnel to USCHD1RTRCNA24A-T203\n\
 bandwidth 56\n\
 ip address "+(ipCHDa)+" 255.255.254.0\n\
 no ip redirects\n\
 ip mtu 1400\n\
 ip hello-interval eigrp 65329 4\n\
 ip hold-time eigrp 65329 12\n\
 ip nat outside\n\
 ip nhrp authentication C1y57f9D\n\
 ip nhrp map 10.163.124.1 208.72.255.41\n\
 ip nhrp map multicast 208.72.255.41\n\
 ip nhrp network-id 203\n\
 ip nhrp nhs 10.163.124.1\n\
 ip nhrp registration no-unique\n\
 ip virtual-reassembly in\n\
 load-interval 30\n\
 delay 500000\n\
 qos pre-classify\n\
 cdp enable\n\
 tunnel source Dialer1\n\
 tunnel destination 208.72.255.41\n\
 tunnel key 203\n\
 tunnel protection ipsec profile B2B-DMVPN\n\
 \n")

                
                
zone = int(input("Enter the client zone 1 for CN-A or 2 for CN-B: "))
routerType = int(input("1 for MPLS, 2 for VPN: "))
ip1 = str(input("Type the IP address of the current OMA dialup tunnel '('without the mask')': "))
if zone == 1:
        if "10.161." in ip1:
          ipOMAa = ip1
          ipCHDa = ip1.replace(".161.", ".163.")
        else:
          if "10.163" in ip1:
            ipCHDa = ip1
            ipOMAa = ip1.replace(".163.", ".161.")

elif zone == 2:
        if "10.161." in ip1:
          ipOMAb = ip1
          ipCHDb = ip1.replace(".161.", ".163.")
        else:
          if "10.163" in ip1:
            ipCHDb = ip1
            ipOMAb = ip1.replace(".163.", ".161.")
else:
        print("Invalid Entry")

tunnel = dialTunnelVPNa(ipOMAa)
tunnelCNA(tunnel)
'''
if (dialTunnelVPNa(ipOMAa)) == 200:
        tunnel200CNA()
elif (dialTunnelVPNa(ipOMAa)) == 201:
        tunnel201CNA()
elif (dialTunnelVPNa(ipOMAa)) == 202:
        tunnel202CNA()
elif (dialTunnelVPNa(ipOMAa)) == 203:
        tunnel203CNA()
else:
        print ("Invalid Entry")'''
        


