import os
from pathlib import Path
import requests
import zipfile

def data_path_setup(current_directory, zip_link):
    path_of_data = Path(current_directory / 'data')
    if path_of_data.is_dir():
        print('%s already exists' % (path_of_data))
    else:
        print('%s does not exist, creating now...' % (path_of_data))
        path_of_data.mkdir(parents=True, exist_ok=True)

    filename = os.path.basename(zip_link)
    link_no_ext = os.path.splitext(filename)[0]
    zip_ext = os.path.splitext(filename)[1]

    if zip_ext != '.zip':
        print('This is not a zip file')
        print(zip_ext)
    else:
        pass

    image_path = Path(path_of_data / link_no_ext)
    if image_path.is_dir():
        print('%s already exists' % (image_path))
    else:
        print('%s does not exist, creating now...' % (image_path))
        image_path.mkdir(parents=True, exist_ok=True)

    with open(path_of_data / filename, 'wb') as data_file:
        request = requests.get(zip_link)
        print('Downloading Data from: ', zip_link)
        data_file.write(request.content)
    
    with zipfile.ZipFile(path_of_data / filename, 'r') as zip_ref:
        print('Unzipping ', filename)
        zip_ref.extractall(image_path)

current_directory = Path.cwd()
zip_link = input('Enter the name of the zip link: ')

data_path_setup(current_directory, zip_link)
