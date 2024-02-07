import requests

API_KEY = "ff6414e7cf4130ce0fcaa0e9e12d83962039bbfa715277100ff5fe7023274f04"


def upload_file(path):
    url = "https://www.virustotal.com/api/v3/files"

    files = { "file": (path, open(path, "rb"))}
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }

    response = requests.post(url, files=files, headers=headers)

    return response.json()["data"]["links"]["self"]


def git_info_files(path):

    url = upload_file(path)

    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    print(response.text)

result = git_info_files("text.txt")

print(result)