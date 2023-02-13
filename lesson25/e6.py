from concurrent.futures import ThreadPoolExecutor

import requests
import time

seconds = int(input("Insert seconds: "))

def send_req():
    response = requests.get("https://api.kanye.rest")
    print(response.text)


with ThreadPoolExecutor(max_workers=10) as executor:
    while seconds > 0:
        print(f"{round(seconds, 1)} seconds left")
        time.sleep(0.1)
        seconds -= 0.1
        if round(seconds, 1) == int(seconds):
            print("sending request")
            executor.submit(send_req) # not blocking

print("DONE")
