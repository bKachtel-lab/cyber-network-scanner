""" 
Cyber Network Scanner
this script scans a target machine using Nmap and extracts open ports

Author: Kachtel Boukhalfa
"""

import subprocess
import analyzer
import report_generator

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

#analyser les resultats
analyse = analyzer.analyze_scan(result)
print(analyse)

#création du rapport de securité
report_generator.generate_report(target, result, analyse)