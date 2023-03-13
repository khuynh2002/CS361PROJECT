import requests
import json

import subprocess

def get_winner(year):
    url = "http://localhost:50555/get-winner?year=" + str(year)


    result = subprocess.run(["curl", url], capture_output=True, text=True)

    if result.returncode == 0:
        return result
    else:
        return "error"

def get_matches(year, nation):

    url = "http://localhost:50555/get-matches?year=" + str(year) + "&nation=" + nation
    result = subprocess.run(["curl", url], capture_output=True, text=True)

    if result.returncode == 0:
        return result
    else:
        return "error"



