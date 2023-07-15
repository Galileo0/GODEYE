import nmap3

def scanTarget(Target):
    scanTop10(Target)


def scanTop10(Target):
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(Target)
    print(results)