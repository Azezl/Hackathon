from io import BytesIO
import requests
import zipfile
from zipfile import ZipFile
from urllib.request import urlopen
import os
import string
import shutil


def far_api_download_files(test_id):
    url = 'http://css-far-stag-03.lab.sandisk.com/fvtlog/{}'.format(test_id)
    try:
        shutil.rmtree(r'C:\Users\1000284173\PycharmProjects\Hackathon\venv\{}'.format(test_id))
    except:
        pass
    os.mkdir(r'C:\Users\1000284173\PycharmProjects\Hackathon\venv\{}'.format(test_id))
    os.chdir(r'C:\Users\1000284173\PycharmProjects\Hackathon\venv\{}'.format(test_id))
    r = requests.get(url, stream=True)
    print(r)

    try:
        r = r.content.decode("utf-8")
        log_path = open("{}.txt".format(test_id), "w")
        log_path.write(r)
        log_path.close()
        
    except:
        z = zipfile.ZipFile(BytesIO(r.content))
        #zipfile = ZipFile(BytesIO.B(r.read()))
        z.extractall()


        

def far_01_api_id(str1):
    url = 'http://css-far-stag-01.lab.sandisk.com:90/progapi/alltests'
    #far_test_link = 'https://css-far-prod-01.lab.sandisk.com/test/6193a09abe17ea1c085bc360'
    far_test_link = str1
    print(type(far_test_link))
    print("IN Far API , "+far_test_link)
    far_id = far_test_link.split('test/')[1]
    post_data = {
                "findquery": {
                                "_id": far_id
                },
                "neededfields": ""
                }
    res = requests.post(url, json=post_data)
    print(res.json())
    response_json = res.json()
    if response_json['statusmessage'] == 'success':
        test_id = response_json['output'][0]['test_id']
        far_api_download_files(test_id)
        return response_json['output'][0]
    else:
        fail ='Test does not exist in FAR'
        return fail


def far_01_api_product_testName(product,testName):
    url = 'http://css-far-stag-01.lab.sandisk.com:90/progapi/alltests'
    #product = 'Vulcan'
    #testName = 'XOR001_LowPowerState_SLC'
    post_data = {
                "findquery": {
                                "product": product,
                                "test_name": testName
                },
                "neededfields": ""
                }
    res = requests.post(url, json=post_data)
    print(res.json())
    response_json = res.json()
    if response_json['statusmessage'] == 'success':
        return response_json['output']
        #for i in range(0, len(response_json['output'])):
            #test_id = response_json['output'][i]['test_id']
            #far_api_download_files(test_id)
            #Show Table of instances to user
    else:
        print('Test does not exist in FAR')


if __name__ == "__main__":
    far_01_api_id()
    #far_01_api_product_testName()
