"""
Wifi scan test from
http://kbcarte.wordpress.com/2011/09/01/android-ase-wifi-scan-with-ui/
"""
#imports and get an object of android
import android, time
droid = android.Android()
 
#scan the wifi and assign vars to hold the results
#this is dirty, making sure WiFi is on, and
#toggling on if not would be better; API Browser =)
droid.wifiStartScan()
ap = droid.wifiGetScanResults()
aps = ap.result
 
#lists to hold the data from scan
x = []
o = []
 
#loop through results and grab the data we are interested in
#format the strings to be displayed in the UI
for point in aps:
  x.append(point[&quot;ssid&quot;])
  #capabilities are the encryption, if blank there is no encryption
  if point[&quot;capabilities&quot;] == &quot;&quot;:
    o.append(&quot;MAC: &quot;+point[&quot;bssid&quot;]+&quot;\nFreq: &quot;+str(point[&quot;frequency&quot;])+&quot;\nEencryp: [OPEN]&quot;)
  else:
    o.append(&quot;MAC: &quot;+point[&quot;bssid&quot;]+&quot;\nFreq: &quot;+str(point[&quot;frequency&quot;])+&quot;\nEencryp: &quot;+point[&quot;capabilities&quot;])
 
#set up UI dialog, populate, and present
droid.dialogCreateAlert(&quot;WiFi Scan&quot;, None)
droid.dialogSetItems(x)
droid.dialogShow()
#this grabs what the user has selected
result = droid.dialogGetResponse().result
 
#if selection not null, create new UI, populate, and present
if result.has_key(&quot;item&quot;):
  item = result[&quot;item&quot;]
  droid.dialogCreateAlert(&quot;Basic Info&quot;, o[item])
  droid.dialogShow()
