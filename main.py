import requests

API_KEY = "ff6414e7cf4130ce0fcaa0e9e12d83962039bbfa715277100ff5fe7023274f04"


def upload_file(path):
    url = "https://www.virustotal.com/api/v3/files"
    files = { "file": ("virus2", open("virus2", "rb"), "application/octet-stream") }
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY,
        "content-type": "multipart/form-data"
    }

    response = requests.post(url, files=files, headers=headers)

    return response.json()["data"]["links"]["self"]

result = upload_file("virus2")
print(result)

