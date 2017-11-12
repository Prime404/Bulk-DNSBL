from pydnsbl import DNSBLChecker
from pathlib import Path
import getopt, sys

checker = DNSBLChecker()
servers = []
nodnsbl = []
inputfile=""

def main(argv):
    try:
        (opts, args) = getopt.getopt(argv, 'hi:', ['ifile='])
    except getopt.GetoptError:
        print ('dnsbl_check.py -i <listofserver>')
        sys.exit(2)
    for (opt, arg) in opts:
        if opt == '-h':
            print ('dnsbl_check.py -i <listofserver>')
            sys.exit()
        elif opt in ('-i', '--ifile'):
            inputfile = arg
    serverlist = Path(inputfile)
    
    if serverlist.is_file():
        with open(serverlist, "r") as items:
            for item in items:
                servers.append(item.strip())
    else:
        print ("Error: The list does not exist")
        quit()
        
    for hostnames in servers:
        result = checker.check_ip(hostnames)
        if result.blacklisted:
            print(result)
            detections = result.detected_by
            for providers in detections.keys():
                print(providers)
        else:
            nodnsbl.append(hostnames)

    for ul_server in nodnsbl:
        print("<DNSBLResult:",ul_server,"was not found on any blacklist>")
        
if __name__ == "__main__":
    main(sys.argv[1:])