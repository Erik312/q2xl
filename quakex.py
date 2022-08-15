import os
import sys
import requests
import openpyxl
import json





def grabdata(url):
    try:
        
        
        r = requests.get(url)
        print("Working.....")
        print("############################################################")
        
        new_l = []
        final_l = []
        
        try:

            data = json.loads(r.text)
        except:
            sys.exit("ERROR: An error occured with json.")
        
        for i in data["features"]:
            
            new_l.append(i)
        for k in new_l:
            the_one = [k["properties"]["mag"],k["properties"]["place"],k["properties"]["time"],k["properties"]["detail"],k["properties"]["tsunami"]]
            final_l.append(the_one)
        
        return final_l
    except requests.exceptions.RequestException as e:
        sys.exit(e)
        
    





def parsedata(data):
    file_name = "quake_data.xlsx"
    try:
        print("Parsing data to excel")
        wb = openpyxl.Workbook()
        ws = wb.active

        ws.append(["Magnitude","Location","Time","Detail","Tsunami"])
        for row in data:
            ws.append(row)

        wb.save(file_name)




        print("###################################################################")
        print(f'File {file_name} succesfully created in this programs directory.')
    except:
        sys.exit("Error parsing to excel.")



def main():
    #input start date: year-month-day(xxxx-xx-xx):
    print("Length of dates gap must be within 30 days or error is thrown.")
    start_date = input("input start date: year-month-day(xxxx-xx-xx): ")
    
    #input end date: year-month-day(xxxx-xx-xx):
    end_date = input("input end date: year-month-day(xxxx-xx-xx): ")

    if len(start_date) <= 0 or len(end_date) <= 0:
        print("###########################")
        sys.exit("Invalid input..exiting")
    else:

        url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}"

        req_data = grabdata(url)
        parsedata(req_data)
        print("#" * 31)
        sys.exit("Exiting program.")



if __name__ == "__main__":
    main()
