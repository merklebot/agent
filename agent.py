#!/usr/bin/python3

import glob
import traceback
import time

import requests
import sys
import json

PLATFORM_API_URL="http://134.209.120.80:8000"
class Config:
    def __init__(self, tenant, user_token, filepath):
        self.BASE_API_URL = f"https://{tenant}.storage.api2.merklebot.com"
        self.USER_TOKEN = user_token
        self.FILESPATH = filepath
config = None
def get_uploaded_filenames():
    global config
    res = requests.get(config.BASE_API_URL+'/contents/', headers={'Authorization': config.USER_TOKEN})
    filenames = [content['filename'] for content in res.json()]
    return filenames
def process_files():
    global config
    print('Getting files...')
    bags = glob.glob(config.FILESPATH)
    bags = reversed(sorted(bags))
    print('Getting uploaded filenames...')
    uploaded_filenames = get_uploaded_filenames()
    print('Start file processing...')
    for bag in bags:
        while True:
            try:
                print('processing ', bag)
                res = upload_file(bag)
                print(res)
                break
            except Exception:
                print("Retry - Failed to process", bag)
                time.sleep(5)

def upload_file(filepath):
    global config
    files = {'file_in': open(filepath, 'rb')}
    res = requests.post(config.BASE_API_URL+'/contents/', files=files, headers={'Authorization': config.USER_TOKEN})
    try:
        result = res.json()
    except:
        print(res)
        traceback.print_exc()
    return result


if __name__=='__main__':
    args = sys.argv[1:]

    print(args)
    API_KEY = args[0]
    robot_data = requests.get(PLATFORM_API_URL+'/robots/'+API_KEY).json()
    robot_name = robot_data['name']
    robot_config = json.loads(robot_data['config'])

    config = Config(tenant=robot_config['tenant'], user_token=robot_config['user_token'], filepath=robot_config['filepath'])
    print('Accessing robot', robot_name)
    print('Config loaded')
    print('Files will be uploaded from', config.FILESPATH)
    process_files()
