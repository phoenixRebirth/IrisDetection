import urllib.request
import json
import service.file_reader as file_reader

def get_url_content(url):
    try:
        file_content = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Could not access to the api: ' + str(e))
        exit(-1)

    return file_content

def get_url_content_as_json(url):
    file_content = get_url_content(url)

    return file_reader.read_json(file_content)