"""
this module creates simple security report 
based on the scan result
"""
import analyzer

def generate_report(target, scan_result, analyse):
    #creer le fichier rapport
    with open ("security_report.txt", "w") as report:
        report.write("Security Scan Report\n")
        report.write("======================\n")
        report.write(f"Target: {target}\n\n")

        report.write("Scan Result:\n")
        report.write(scan_result)

        report.write(analyse)

    print("\n\nReport generated: security_report.txt")