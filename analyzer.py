"""analyser les resultat Nmap
détécter services suspects
afficher alertes sécurité
"""

#Analyser les services détectés
def analyze_scan(result):
    print("\n[ Security Analysis ]\n")
    #FTP
    if "21/tcp" in result:
        print("[!] FTP service detected - check for anonymous login")
    #HTTP
    if "80/tcp" in result:
        print("[!] HTTP service detected - check web vulnerabilities")

    #SMB
    if "445/tcp" in result:
        print("[!] SMB service detected - possible network sharing risk")