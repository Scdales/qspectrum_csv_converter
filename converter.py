import csv
import datetime
now = datetime.datetime.now()
import sys

with open(sys.argv[1], 'r') as f:
    print("\nOpening: " + sys.argv[1])
    reader = csv.reader(f)
    freq_list = list(reader)

name = sys.argv[1][:len(sys.argv[1])-4]
wwb_list = []
wsm_list = []

def wwbFrequency(MHz):
    return MHz[:3] + '.' + MHz[3:6]

def wsmFrequency(MHz):
    return MHz[:6]

for freq in freq_list:
    if len(freq) == 3:
        wwb_list.append([wwbFrequency(freq[0]), freq[1]])
        wsm_list.append([wsmFrequency(freq[0]), '', freq[1]])

with open(name + '_WWB.csv', 'w', newline='') as wwbcsvfile:
    writer = csv.writer(wwbcsvfile, delimiter=',', quotechar='"')
    writer.writerows(wwb_list)
    print('Saved: ' + name + '_WWB.csv')

with open(name + '_WSM.csv', 'w', newline='') as wsmcsvfile:
    wsm_newlist = [['Receiver',''],['Date/Time',''],['RFUnit','dBm'],['Owner',''],['ScanCity',''],['ScanComment',''],['ScanCountry',''],['ScanDescription',''],['ScanInteriorExterior',''],['ScanLatitude',''],['ScanLongitude',''],['ScanName',now.strftime("%Y-%m-%d %H:%M")],['ScanPostalCode',''],['Frequency Range [kHz]',wsm_list[0][0][:6],wsm_list[len(wsm_list)-1][0][:6],str(int(wsm_list[1][0][:6])-int(wsm_list[0][0][:6]))],['Frequency','RF level (%)','RF level']]
    wsm_newlist.extend(wsm_list)
    writer = csv.writer(wsmcsvfile, delimiter=';')
    writer.writerows(wsm_newlist)
    print('Saved: ' + name + '_WWB.csv')

print("\nDone\n")