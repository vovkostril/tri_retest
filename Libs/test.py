import os
import xml.etree.ElementTree as ET
from datetime import datetime
import time
import päivittäjä


date = datetime.today().strftime('%Y-%m-%d')

# Running Redu Tests
# os.system("python3 -m robot Redu_Tests.robot")
os.system("mv log.html redu_log.html")

# Checking Number of Tests passed
tree = ET.parse("output.xml")
root = tree.getroot()
for total in root.iter('stat'):
    at = str(total.attrib)
    parts = at.split("'")
    passed = parts[3]
    failed = parts[7]
    skipped = parts[11]
    if at.__contains__("'fail': '0'"):
        break

# Redu Tests into zip
os.system("zip "+date+"_Redu.zip redu_log.html reduconsoleone.txt reduconsoletwo.txt")
os.system("rm redu_log.html")
os.system("rm reduconsoleone.txt")
os.system("rm reduconsoletwo.txt")

total = int(passed) + int(failed) + int(skipped)
Text += "Redu Tests Passed: "+passed+"/"+str(total)+"\n"
time.sleep(100)


#Sends Mail of the test results
# os.system('mail -s "Automated Test Results" anton.paavola@dnwpartners.com -A '+date+'_PoE.zip -A '+date+'_Redu.zip -A '+date+'_ERPS.zip -rlab-test@dnwpartners.com < mail.txt')
# os.system('mail -s "Automated Test Results" liisa.niemela@dnwpartners.com -A '+date+'_PoE.zip -A '+date+'_Redu.zip -A '+date+'_ERPS.zip -rlab-test@dnwpartners.com < mail.txt')
# os.system('mail -s "Automated Test Results" juha.koskelainen@dnwpartners.com -A '+date+'_PoE.zip -A '+date+'_Redu.zip -A '+date+'_ERPS.zip -rlab-test@dnwpartners.com < mail.txt')
# os.system('mail -s "Automated Test Results" maija.latva-maenpaa@dnwpartners.com -A '+date+'_PoE.zip -A '+date+'_Redu.zip -A '+date+'_ERPS.zip -rlab-test@dnwpartners.com < mail.txt')
# os.system('mail -s "Automated Test Results" aleksi.blinnikka@dnwpartners.com -A '+date+'_PoE.zip -A '+date+'_Redu.zip -A '+date+'_ERPS.zip -rlab-test@dnwpartners.com < mail.txt')
os.system('mail -s "Automated Test Results" anastasiia.vovkostril@dnwpartners.com -A '+date+'_PoE.zip -A '+date+'_Redu.zip -A '+date+'_ERPS.zip -rlab-test@dnwpartners.com < mail.txt')

#Stores the zip-files
# os.system('mv '+date+'_PoE.zip PoE_Library/')
os.system('mv '+date+'_Redu.zip Redu_Library/')
# os.system('mv '+date+'_ERPS.zip ERPS_Library/')
