from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "ок"

    return app


    @app.route('/CreateInputFile', methods=['GET', 'POST'])
    def login():
        result = "-"
        if request.method == 'GET':
            diagramName = request.form['diagramName']
            get_settings()
            result = CreateInputFile(diagramName)
        return result


import time
import xml.etree.ElementTree as ET


def get_settings():
    data_file = '/home/sas/myproject/settings.xml'
    xml_data = ET.parse(data_file)
    root = xml_data.getroot()
    for i in root.iter():
        if i.tag == 'AppAdress':
            AppAdress = i.text
        if i.tag == 'Login':
            Login = i.text
        if i.tag == 'Pass':
            Pass = i.text
         if i.tag == 'Domain':
            Domain = i.text
         if i.tag == 'BusinessContextName':
            BusinessContextName = i.text



start_time = time.time()

my_subdiagram = []
my_process = []


def CreateInputFile(diagramName)
    my_file = open("BabyFile.txt", "w+")
    my_file.write('''<MAExtractRequest>
    <CampaignDO detail="ALL">
        <Name operator="=">'''diagramName'''</Name>
        <CampaignType operator="=">decisionCampaign</CampaignType>
    </CampaignDO>
</MAExtractRequest> ''')
    my_file.close()



def find_subdiagram(data_file):
    xml_data = ET.parse(data_file)
    root = xml_data.getroot()
    for i in root.iter():
        if i.tag == 'SubdiagramName':
            my_subdiagram.append(i.text)
    print(my_subdiagram)


def find_process(subdiagram):
    xml_data = ET.parse(subdiagram)
    root = xml_data.getroot()
    for i in root.iter():
        if i.tag == 'ProcessNodeDataDO':
            name_process = i.find('NodeName').text
            my_process.append(name_process)
    print(my_process)

process_file = 'C:\\Users\\Илья\\Documents\\ГПБ_Хакатон_2021\\input.xml'
sub_diagram = 'C:\\Users\\Илья\\Documents\\ГПБ_Хакатон_2021\\output.xml'

find_subdiagram(process_file)
find_process(sub_diagram)

finish_time = time.time() - start_time
print(finish_time, 'cek')