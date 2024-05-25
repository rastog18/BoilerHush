import math
import time

import requests
import static as static
from flask import Flask, url_for, request, redirect
from flask import render_template

# ------------------------------------- Call Scraper --------------------------------------#
list_of_places = ["HIKS Hicks (John W.) Undergraduate Library", "HSSE Library",
                  "KCTR Krannert Center for Executive Education and Research", "BCC Black Cultural Center",
                  "KRCH Krach Leadership Center", "WALC Wilmeth (Thomas S. and Harvey D.) Active Learning Center",
                  "CREC Córdova (France A.) Recreational Sports Center"]


class server():
    def __init__(self):
        self.data = []
        self.distance = []
        self.duration = []


server_obj = server()

# The following code helps you acquire the name, address, time, and popular times of study spots.

obj = scrape.Scraper()
for i in list_of_places:
    obj.scrape(i + " Purdue")
    try:
        obj.scrape(i + " Purdue")
    except:
        print(f"unable to scrape: {i}")
obj.close()
file = open("data.dat", "rb")
data = []
while True:
    try:
        data.append(pickle.load(file))
    except:
        file.close()
        break;
server_obj.data = data
file.close()

#EXAMPLE OF DATA
# server_obj.data = [{'name': 'Hicks Undergraduate Library Purdue',
#                     'address': 'Ground, 504 W State St, West Lafayette, IN 47907',
#                     'Time': 'Open ⋅ Closes 12\u202fam',
#                     'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
#                    {'name': 'HSSE Purdue',
#                     'address': '504 W State St, West Lafayette, IN 47907',
#                     'Time': 'Open ⋅ Closes 12\u202fam',
#                     'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]}]

# Follwoing code was used to make the .dat file:
# obj = scrape.Scraper()
# first = True
# avail = available_keywords[160:]
# for building in avail:
#     if first:
#         coords = obj.start_distance(building)
#     else:
#         coords = obj.distance(building)
#     location_dict[building] = coords
# obj.close()
# print(location_dict)
file = open("co-ordinates.txt", "r")
file_data = file.readlines()
location_dict = {}
for line in file_data:
    line = line.split(":")
    coords = line[1].split(",")
    coords[0] = coords[0].strip()
    coords[1] = coords[1].strip()
    location_dict[line[0]] = [coords[0], coords[1]]
              

#EXAMPLE OF LOCATION_DICT
# location_dict = {
#     "Asian American and Asian Resource and Cultural Center": [
#         "40.42914",
#         "-86.91753"
#     ],
#     "AAPF Ag Alumni Seed Phenotyping Facility": [
#         "40.42299",
#         "-86.91896"
#     ],
# }


def reorder_data(order):
    try:
        new_order = []
        new_data = {}
        for dest in order:
            if dest.endswith('km'):
                dest = float(dest.rstrip('km')) * 1000
            else:
                dest = float(dest.rstrip('m'))
            new_order.append(dest)
        for i in range(0, len(order)):
            new_data[new_order[i]] = server_obj.data[i]
        new_order.sort()
        new_data = {i: new_data[i] for i in new_order}
        server_obj.distance = new_order
        server_obj.data = [new_data[item] for item in new_data]
    except:
        server_obj.distance = ['', '', '', '', '', '', '']


# --------------------------------------- Server ------------------------------------#
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return_location = request.get_json()
        location = return_location['value']
        location_list = location_dict[location]
        # Your API key
        key = '-----------------------------------------------------'
        for dest in list_of_places:
            # Construct the URL
            url = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={location_list[0]},{location_list[1]}&destinations={location_dict[dest][0]},{location_dict[dest][1]}&key={key}"
            response = requests.get(url=url)
            response = response.json()
            server_obj.distance.append(response["rows"][0]["elements"][0]["distance"]["text"])
            server_obj.duration.append(response["rows"][0]["elements"][0]["duration"]["text"])
        reorder_data(server_obj.distance)
        time.sleep(4)
    output = render_template("index.html")
    url_for('static', filename='assets/css/cover.css')
    url_for('static', filename='assets/img/lp.png')
    url_for('static', filename='assets/js/script.js')
    return output


@app.route("/loading")
def get_loading():
    output = render_template("load.html")
    return output


@app.route("/where")
def get_list():
    output = render_template("list.html", data=server_obj.data, distance=server_obj.distance,
                             duration=server_obj.duration)
    url_for('static', filename='assets/css/list.css')
    return output


if __name__ == "__main__":
    app.run(debug=True)
