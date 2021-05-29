import http.client
import json
import pprint
import winsound
import time
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 5000  # Set Duration To 1000 ms == 1 second

conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
payload = ''
headers = {}
print("Welcome to Simple Vaccine Slot finder for Hyderabad and Rangareddy. The app checks Cowin Public API and makes a long beep sound when slots are found for 18+ beneficiaries")
print("Developed by Samrat Majumder. Source code at https://github.com/sammyblues/vaccineslotfinder")
loop = True
checkdate = input("Please enter search date in DD-MM-YYYY format. Eg: 28-05-2021:: ")
if checkdate == "":
    loop = False
while loop:
    print("Checking API Setu......")
    conn.request("GET", "/api/v2/appointment/sessions/public/findByDistrict?district_id=603&date="+checkdate, payload, headers)
    res = conn.getresponse()
    data = res.read()
    jsondata = json.loads(data.decode("utf-8"))
    for session in jsondata["sessions"]:
        if session["available_capacity_dose1"] > 0 and session["min_age_limit"] == 18:
            print("PIN:" + str(session["pincode"]) + " Name: " + str(session["name"]) + " SlotsAVLBL: " + str(
                session["available_capacity_dose1"]) + " MinAge: " + str(session["min_age_limit"]))
            winsound.Beep(frequency, duration)

    conn.request("GET", "/api/v2/appointment/sessions/public/findByDistrict?district_id=581&date="+checkdate, payload, headers)
    res = conn.getresponse()
    data = res.read()
    jsondata = json.loads(data.decode("utf-8"))
    for session in jsondata["sessions"]:
        if session["available_capacity_dose1"] > 0 and session["min_age_limit"] == 18:
            print("PIN:" + str(session["pincode"]) + " Name: " + str(session["name"]) + " SlotsAVLBL: " + str(
                session["available_capacity_dose1"]) + " MinAge: "+str(session["min_age_limit"]))
            winsound.Beep(frequency, duration)
    winsound.Beep(400,200)
    time.sleep(20)
