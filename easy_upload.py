import glob
import traceback
import time

import requests

TENANT_NAME = ""
USER_TOKEN = ""
FOLDER_PATH = ""

BASE_API_URL = f"https://${TENANT_NAME}.storage.api2.merklebot.com"


def get_uploaded_filenames():
    res = requests.get(BASE_API_URL + '/contents/', headers={'Authorization': USER_TOKEN})
    filenames = [content['filename'] for content in res.json()]
    return filenames


def process_files():
    print('Getting files...')
    files = glob.glob(f"{FOLDER_PATH}")
    files = reversed(sorted(files))
    print('Getting uploaded filenames...')
    uploaded_filenames = get_uploaded_filenames()
    print('Start file processing...')
    for file in files:
        while True:
            try:
                if file in uploaded_filenames:
                    continue
                print('processing ', file)
                res = upload_file(file)
                print(res)
                break
            except Exception:
                print("Retry - Failed to process", file)
                time.sleep(5)


def upload_file(filepath):
    files = {'file_in': open(filepath, 'rb')}
    res = requests.post(BASE_API_URL + '/contents/', files=files, headers={'Authorization': USER_TOKEN})
    try:
        result = res.json()
    except:
        print(res)
        traceback.print_exc()
    return result


if __name__ == '__main__':
    process_files()
