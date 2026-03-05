""" 
Cyber Network Scanner
this script scans a target machine using Nmap and extracts open ports

Author: Kachtel Boukhalfa
"""

import subprocess

#demander l'adresse IP cible à l'utilisateur
target = input("Enter target IP address: ")
print(f"\n Scanning target : {target}\n")

#lancer la commande nmap 
scan = subprocess.run(
    ["nmap", "-Pn", "-sV", target],
     capture_output=True,
     text=True
 )

#récupérer le resultat du scan 
result = scan.stdout

#afficher le resultat
print(result)

#Analyser les services détectés
if "21/tcp" in result:
    print("[!] FTP service detected - check for anonymous login")

if "80/tcp" in result:
    print("[!] HTTP service detected - web server running")

if "445/tcp" in result:
    print("[!] SMB service detected - possible SMB vulnerabilities")