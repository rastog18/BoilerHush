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

# obj = scrape.Scraper()
# for i in list_of_places:
#     obj.scrape(i + " Purdue")
#     # try:
#     #     obj.scrape(i + " Purdue")
#     # except:
#     #     print(f"unable to scrape: {i}")
# obj.close()
# file = open("data.dat", "rb")
# data = []
# while True:
#     try:
#         data.append(pickle.load(file))
#     except:
#         file.close()
#         break;

server_obj.data = [{'name': 'Hicks Undergraduate Library Purdue',
                    'address': 'Ground, 504 W State St, West Lafayette, IN 47907',
                    'Time': 'Open ⋅ Closes 12\u202fam',
                    'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
                   {'name': 'HSSE Purdue',
                    'address': '504 W State St, West Lafayette, IN 47907',
                    'Time': 'Open ⋅ Closes 12\u202fam',
                    'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
                   {'name': 'Parrish Library Purdue',
                    'address': 'Krannert, 403 W State St bldg 2nd floor, West Lafayette, IN 47907',
                    'Time': 'Open ⋅ Closes 12\u202fam',
                    'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
                   {'name': 'Black Cultural Center Library Purdue Purdue',
                    'address': 'Purdue University, 1100 3rd Street, West Lafayette, IN 47907',
                    'Time': 'Open ⋅ Closes 10\u202fpm',
                    'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
                   {'name': 'Krach Leadership Center Purdue',
                    'address': '1198 3rd Street, West Lafayette, IN 47907',
                    'Time': 'Open ⋅ Closes 7\u202fpm',
                    'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
                   {'name': 'WALC Purdue',
                    'address': '340 Centennial Mall Dr, West Lafayette, IN 47907',
                    'Time': 'Open ⋅ Closes 12\u202fam',
                    'popular_times': [3, 3, 31, 48, 15, 65, 65, 69, 73, 75, 73, 65, 54, 44, 31, 22, 19, 19]},
                   {'name': 'Corec Purdue',
                    'address': '355 N Martin Jischke Dr, West Lafayette, IN 47906',
                    'Time': 'Closed ⋅ Opens 10\u202fam Sat',
                    'popular_times': []}]
location_dict = {
    "Asian American and Asian Resource and Cultural Center": [
        "40.42914",
        "-86.91753"
    ],
    "AAPF Ag Alumni Seed Phenotyping Facility": [
        "40.42299",
        "-86.91896"
    ],
    "ABE Agricultural and Biological Engineering": [
        "40.42166",
        "-86.91645"
    ],
    "ADDL Animal Disease Diagnostic Laboratory": [
        "40.41813",
        "-86.91589"
    ],
    "ADM ADM Agricultural Innovation Center": [
        "40.41629",
        "-86.91960"
    ],
    "Admissions, Office of (Stewart Center 102)": [
        "40.42503",
        "-86.91254"
    ],
    "ADPA-C Aspire at Discovery Park": [
        "40.42363",
        "-86.92456"
    ],
    "AGAD Agricultural Administration Building": [
        "40.42405",
        "-86.91397"
    ],
    "AHF Animal Holding Facility": [
        "40.41862",
        "-86.91403"
    ],
    "AQUA Burke (Morgan J.) Boilermaker Aquatic Center": [
        "40.42814",
        "-86.92316"
    ],
    "AR Armory": [
        "40.42809",
        "-86.91614"
    ],
    "ARMS Armstrong (Neil) Hall of Engineering": [
        "40.43102",
        "-86.91474"
    ],
    "ASB Airport Service Building (Shop Services)": [
        "31.00199",
        "-13.24759"
    ],
    "BALY Bailey (Ralph and Bettye) Hall": [
        "40.42727",
        "-86.90995"
    ],
    "BCC Black Cultural Center": [
        "40.42753",
        "-86.91941"
    ],
    "BCHM Biochemistry Building": [
        "40.42287",
        "-86.91616"
    ],
    "BHEE Brown (Max W & Maileen) Family Hall": [
        "40.428729837576164", "-86.9120039317277"
    ],
    "BIDC Bechtel Innovation Design Center": [
        "40.42745",
        "-86.91878"
    ],
    "BIND Bindley Bioscience Center": [
        "40.42293",
        "-86.92329"
    ],
    "BRK Birck Nanotechnology Center": [
        "40.42274",
        "-86.92448"
    ],
    "BRNG Beering (Steven C.) Hall of Liberal Arts and Education": [
        "40.42558",
        "-86.91610"
    ],
    "BRWN Brown (Herbert C.) Laboratory of Chemistry": [
        "40.42659",
        "-86.91177"
    ],
    "Car/Van Rentals and Charter Bus (MMDC)": [
        "40.41534",
        "-86.91778"
    ],
    "CHAS Chaney-Hale Hall of Science": [
        "40.42864",
        "-86.91519"
    ],
    "CL50 Class of 1950 Lecture Hall": [
        "40.42636",
        "-86.91495"
    ],
    "CONT Continuum": [
        "40.42337",
        "-86.92754"
    ],
    "CONV Convergence": [
        "40.42374",
        "-86.92710"
    ],
    "CREC Córdova (France A.) Recreational Sports Center": [
        "40.42825",
        "-86.92225"
    ],
    "CRTN Creighton (Hobart and Russell) Hall of Animal Sciences": [
        "40.42119",
        "-86.91867"
    ],
    "DANL Daniel (William H.) Turfgrass Research Center": [
        "40.44198",
        "-86.92993"
    ],
    "DAUC Dauch (Dick and Sandy) Alumni Center": [
        "40.42194",
        "-86.91060"
    ],
    "DLR Hall for Discovery and Learning Research": [
        "40.42122",
        "-86.92235"
    ],
    "DMNT DeMent (Clayton W.) Fire Station": [
        "40.42776",
        "-86.92384"
    ],
    "DOYL Doyle (Leo Philip) Laboratory": [
        "40.41872",
        "-86.91540"
    ],
    "DRUG Drug Discovery": [
        "40.42177",
        "-86.91745"
    ],
    "DUDL Dudley Hall": [
        "40.42721",
        "-86.91117"
    ],
    "DYE Pete Dye Clubhouse": [
        "40.44043",
        "-86.92648"
    ],
    "ECEC Purdue University Early Care and Education Center": [
        "40.42486",
        "-86.93296"
    ],
    "EEL Entomology Environmental Laboratory": [
        "40.42298",
        "-86.91464"
    ],
    "EHSA Equine Health Sciences Annex": [
        "40.41756",
        "-86.91405"
    ],
    "EHSB Equine Health Sciences Building": [
        "40.41873",
        "-86.91478"
    ],
    "ELLT Elliott (Edward C.) Hall of Music": [
        "40.42787",
        "-86.91490"
    ],
    "FLEX Flex Laboratories": [
        "40.42122",
        "-86.92353"
    ],
    "FOPN Flight Operations Building": [
        "40.42009",
        "-86.92549"
    ],
    "FPRD Forest Products Building": [
        "40.42265",
        "-86.91407"
    ],
    "FRNY Forney Hall of Chemical Engineering": [
        "40.42946",
        "-86.91385"
    ],
    "FWLR Fowler (Harriet O. and James M., Jr.) Memorial House": [
        "40.42486",
        "-86.92213"
    ],
    "GCMB Golf Course Maintenance Barn": [
        "40.43843",
        "-86.92865"
    ],
    "GMF Grounds Maintenance Facility": [
        "40.41543",
        "-86.91903"
    ],
    "GMGF Grounds Maintenance Greenhouse Facilities": [
        "40.41518",
        "-86.91977"
    ],
    "The Graduate School (Young Hall - first floor)": [
        "40.42265",
        "-86.91057"
    ],
    "Grand Prix Track (see Northwest Athletic Complex Inset)": [
        "40.43775",
        "-86.94159"
    ],
    "GRIS Grissom Hall": [
        "40.42643",
        "-86.91068"
    ],
    "GRS Grounds Service Building": [
        "40.41802",
        "-86.91939"
    ],
    "HAAS Haas (Felix) Hall": [
        "40.42696",
        "-86.91639"
    ],
    "HAGL Hagle (Marc and Sharon) Hall": [
        "40.42711",
        "-86.91873"
    ],
    "HAMP Hampton (Delon and Elizabeth) Hall of Civil Engineering": [
        "40.43015",
        "-86.91473"
    ],
    "HANS Hansen (Arthur G.) Life Sciences Research Building": [
        "40.42227",
        "-86.91694"
    ],
    "HEAV Heavilon Hall": [
        "40.42623",
        "-86.91174"
    ],
    "HERL Herrick Acoustics": [
        "40.42289",
        "-86.92083"
    ],
    "HGRH Horticultural Greenhouse": [
        "40.43671",
        "-86.92615"
    ],
    "HIKS Hicks (John W.) Undergraduate Library": [
        "40.42455744119984",
        "-86.91261347405518"
    ],
    "HLAB Herrick Laboratories": [
        "40.42199",
        "-86.91972"
    ],
    "HMMT Hazardous Materials Management Trailer": [
        "40.41599",
        "-86.91110"
    ],
    "HNLY Hanley (Bill and Sally) Hall": [
        "40.42472",
        "-86.92275"
    ],
    "HOCK Hockmeyer (Wayne T. and Mary T.) Hall of Structural Biology": [
        "40.42105",
        "-86.92106"
    ],
    "HSSE Library": [
        "40.42506278003401",
        "-86.91328206056427"
    ],
    "HORT Horticulture Building": [
        "40.43469",
        "-86.92572"
    ],
    "HOVD Hovde (Frederick L.) Hall of Administration": [
        "40.42823",
        "-86.91431"
    ],
    "HULL Hull All-American Marching Band": [
        "40.42784",
        "-86.92485"
    ],
    "JNSN Johnson (Helen R.) Hall of Nursing": [
        "40.42944",
        "-86.91540"
    ],
    "KCTR Krannert Center for Executive Education and Research": [
        "40.42348",
        "-86.91139"
    ],
    "KNOY Knoy (Maurice G.) Hall of Technology": [
        "40.42778",
        "-86.91109"
    ],
    "KRAN Krannert Building": [
        "40.42353",
        "-86.91081"
    ],
    "KRCH Krach Leadership Center": [
        "40.42761",
        "-86.92110"
    ],
    "LAMB Lambert (Ward L.) Fieldhouse and Gymnasium": [
        "40.43226",
        "-86.91581"
    ],
    "LCCP Latino Cultural Center at Purdue": [
        "40.42902",
        "-86.91754"
    ],
    "Library, Main (see HIKS)": [
        "40.42453",
        "-86.91252"
    ],
    "LILY Lilly Hall of Life Sciences": [
        "40.42348",
        "-86.91790"
    ],
    "LMBS Lambertus Hall": [
        "40.42721",
        "-86.91139"
    ],
    "LMSB Laboratory Materials Storage Building": [
        "40.41541",
        "-86.91100"
    ],
    "LMST Laboratory Materials Storage Trailer": [
        "40.41596",
        "-86.91093"
    ],
    "LOLC Land O’Lakes Center for Experiential Learning and Purina Pavilion": [
        "40.42103",
        "-86.91835"
    ],
    "LSPS Life Science Plant and Soils Laboratory": [
        "40.42310",
        "-86.91882"
    ],
    "LWSN Lawson (Richard and Patricia) Computer Science Building": [
        "40.42760",
        "-86.91681"
    ],
    "LYLE Lyles-Porter Hall": [
        "40.42064",
        "-86.91623"
    ],
    "LYNN Lynn (Charles J.) Hall of Veterinary Medicine": [
        "40.41949",
        "-86.91468"
    ],
    "MACK Mackey (Guy J.) Arena": [
        "40.433325437811085", "-86.91609044521837"
    ],
    "MANN Mann (Gerald D. and Edna E.) Hall": [
        "40.42303",
        "-86.92258"
    ],
    "MATH Mathematical Sciences Building": [
        "40.42614",
        "-86.91553"
    ],
    "ME Mechanical Engineering Building": [
        "40.42826650005268",
        "-86.91285811122168"
    ],
    "MJIS Jischke (Martin C.) Hall of Biomedical Engineering": [
        "40.42221",
        "-86.92095"
    ],
    "MMDC Materials Management and Distribution Center": [
        "40.41523",
        "-86.91775"
    ],
    "MMS1 Materials Management Storage Building 1": [
        "40.41485",
        "-86.91883"
    ],
    "MOLL Mollenkopf Athletic Center": [
        "40.43553",
        "-86.91666"
    ],
    "MRGN Morgan (Burton D.) Center for Entrepreneurship": [
        "40.42368",
        "-86.92273"
    ],
    "MRRT Marriott Hall": [
        "40.42459",
        "-86.91687"
    ],
    "MSEE Materials and Electrical Engineering Building": [
        "40.42931",
        "-86.91225"
    ],
    "MTHW Matthews Hall": [
        "40.42472",
        "-86.91624"
    ],
    "NACC Native American Educational and Cultural Center": [
        "40.42916",
        "-86.91685"
    ],
    "NISW Niswonger Aviation Technology Building": [
        "40.41649",
        "-86.92936"
    ],
    "NLSN Nelson (Philip E.) Hall of Food Science": [
        "40.42157",
        "-86.91536"
    ],
    "OLMN Ollman (Melvin L.) Golfcart Barn": [
        "40.44001",
        "-86.92704"
    ],
    "PAGE Page (Thomas A.) Pavilion": [
        "40.41089",
        "-86.91576"
    ],
    "Parking Facilities (MMDC)": [
        "40.41527",
        "-86.91822"
    ],
    "PAO Pao (Yue-Kong) Hall of Visual and Performing Arts": [
        "40.42254",
        "-86.91286"
    ],
    "PFEN Pfendler (David C.) Hall of Agriculture": [
        "40.42355",
        "-86.91525"
    ],
    "PFSB Physical Facilities Service Building": [
        "40.41412",
        "-86.91649"
    ],
    "PGSC Purdue Graduate Student Center": [
        "40.42987",
        "-86.91183"
    ],
    "Pharmacy (Purdue University Retail Pharmacy - RHPH)": [
        "40.42970",
        "-86.91627"
    ],
    "PHYS Physics Building": [
        "40.43013",
        "-86.91297"
    ],
    "PJEC Jischke (Patty) Early Care and Education Center Purdue Research Park": [
        "40.45706",
        "-86.92696"
    ],
    "PMRI Purdue Magnetic Resonance Imaging Facility": [
        "40.42127",
        "-86.91538"
    ],
    "PMU Purdue Memorial Union": [
        "40.42473",
        "-86.91044"
    ],
    "PMUC Purdue Memorial Union Club": [
        "40.42571",
        "-86.91071"
    ],
    "POTR Potter (A.A.) Engineering Center": [
        "40.42733",
        "-86.91201"
    ],
    "PRCE Peirce Hall": [
        "40.42666",
        "-86.91494"
    ],
    "PSYC Psychological Sciences Building": [
        "40.42704",
        "-86.91483"
    ],
    "PTCA Purdue Technology Center Aerospace": [
        "40.42368",
        "-86.93990"
    ],
    "PUSH Purdue University Student Health Center": [
        "40.430564171709264",
        "-86.91634047405488"
    ],
    "PVAB Purdue Village Administration Building": [
        "40.42024",
        "-86.92381"
    ],
    "RAIL American Railway Building": [
        "40.42799",
        "-86.91269"
    ],
    "RAWL Rawls (Jerry S.) Hall": [
        "40.42385",
        "-86.90970"
    ],
    "RHPH Heine (Robert E.) Pharmacy Building": [
        "40.42978",
        "-86.91579"
    ],
    "SC Stanley Coulter Hall": [
        "40.42641",
        "-86.91424"
    ],
    "SCHM Helen B. Schleman Hall": [
        "40.42585",
        "-86.91506"
    ],
    "SCPA Slayter Center of Performing Arts": [
        "40.43188",
        "-86.92244"
    ],
    "SIML Holleman-Niswonger Simulator Center": [
        "40.41671",
        "-86.93484"
    ],
    "SMTH Smith Hall": [
        "40.42350",
        "-86.91673"
    ],
    "STDM Ross-Ade Stadium": [
        "40.43437",
        "-86.91833"
    ],
    "STEW Stewart Center (includes Welcome Center)": [
        "40.42506",
        "-86.91284"
    ],
    "STON Stone (Winthrop E.) Hall": [
        "40.42462",
        "-86.91511"
    ],
    "Student Health Center": [
        "40.43052",
        "-86.91624"
    ],
    "TEL Telecommunications Building": [
        "40.42604",
        "-86.91690"
    ],
    "TERY Terry (Oliver P.) House": [
        "40.42228",
        "-86.92213"
    ],
    "TREC Turf Recreation Exercise Center": [
        "40.42851",
        "-86.92413"
    ],
    "TSWF Transportation Service Wash Facility": [
        "40.41349",
        "-86.91447"
    ],
    "UC University Church": [
        "40.42601162573786",
        "-86.91009185941412"
    ],
    "UNIV University Hall": [
        "40.42527",
        "-86.91506"
    ],
    "WADE Wade (Walter W.) Utility Plant": [
        "40.41728",
        "-86.91225"
    ],
    "WALC Wilmeth (Thomas S. and Harvey D.) Active Learning Center": [
        "40.4273502372413",
        "-86.91320208940054"
    ],
    "WANG Wang (Seng-Liang) Hall": [
        "40.43043",
        "-86.91234"
    ],
    "WSLR Whistler": [
        "40.42314",
        "-86.91551"
    ],
    "Whistler (Roy L.) Hall of Agricultural Research G8": [
        "40.42321",
        "-86.91559"
    ],
    "Wetherill (Richard Benbridge) Laboratory of Chemistry G7": [
        "40.42647",
        "-86.91296"
    ],
    "Young (Ernest C.) Hall H8": [
        "40.42277",
        "-86.91059"
    ],
    "Cary (Franklin Levering) Quadrangle F4": [
        "40.4319405989537",
        "-86.91846901943283"
    ],
    "Duhme (Ophelia) Residence Hall E7": [
        "40.42548",
        "-86.92057"
    ],
    "Earhart (Amelia) Residence Hall D7": [
        "40.42563",
        "-86.92481"
    ],
    "Ford (Fred and Mary) Dining Court E4": [
        "40.43212",
        "-86.91945"
    ],
    "First Street Towers D7": [
        "40.42496",
        "-86.92445"
    ],
    "Harrison (Benjamin) Residence Hall C7": [
        "40.42485524105517",
        "-86.92662436056422"
    ],
    "Hawkins (George A.) Hall H8": [
        "40.42283",
        "-86.91165"
    ],
    "Honors College and Residences North E7": [
        "40.42713",
        "-86.91953"
    ],
    "Hillenbrand Residence Hall C7": [
        "40.42689",
        "-86.92633"
    ],
    "Hilltop Apartments E3": [
        "40.43389",
        "-86.92162"
    ],
    "McCutcheon (John T.) Residence Hall C7": [
        "40.42468",
        "-86.92799"
    ],
    "Meredith (Virginia C.) Residence Hall D7": [
        "40.42631",
        "-86.92316"
    ],
    "Owen (Richard) Residence Hall E4": [
        "40.43225",
        "-86.92060"
    ],
    "Parker (Frieda) Residence Hall (formerly Griffin Residence Halls) E6": [
        "40.42848",
        "-86.91943"
    ],
    "Purdue Village Community Center C8": [
        "40.42248",
        "-86.92856"
    ],
    "Shealy (Frances M.) Residence Hall E7": [
        "40.42615",
        "-86.92063"
    ],
    "Tarkington (Newton Booth) Residence Hall E5": [
        "40.43083",
        "-86.92062"
    ],
    "Vawter (Everett B.) Residence Hall E6": [
        "40.42710",
        "-86.92059"
    ],
    "Warren (Martha E. and Eugene K.) Residence Hall E7": [
        "40.42647",
        "-86.92058"
    ],
    "Wiley Dining Court E6": [
        "40.42853",
        "-86.92072"
    ],
    "Wiley (Harvey W.) Residence Hall E6": [
        "40.42948",
        "-86.92060"
    ],
    "Wood (Elizabeth G. and William R.) Residence Hall E7": [
        "40.42631",
        "-86.92141"
    ]
}


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
        key = 'I9HwPBO74oJNa5yj4QdIqZg5LmbtcqNMH7DK8B54rmqdo2IMowPIsGHQ5ps0RASw'
        for dest in list_of_places:
            # Construct the URL
            url = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={location_list[0]},{location_list[1]}&destinations={location_dict[dest][0]},{location_dict[dest][1]}&key={key}"
            response = requests.get(url=url)
            print(url)
            response = response.json()
            server_obj.distance.append(response["rows"][0]["elements"][0]["distance"]["text"])
            server_obj.duration.append(response["rows"][0]["elements"][0]["duration"]["text"])
        reorder_data(server_obj.distance)
        time.sleep(4)
        # return redirect(url_for('get_list', tobe_passed_list=data))
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
