import requests

if __name__ == '__main__':
    genderize_url = "https://api.genderize.io"
    response = requests.get(genderize_url, 
                 params={'name': 'herut'})
    if response.status_code == 200:
        print(response.json()['gender'])


