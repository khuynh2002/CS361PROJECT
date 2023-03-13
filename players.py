import requests
import json


def process_response(response):
    response_dict = json.loads(response)
    print(response_dict)
    required_data_dict = {"name": response_dict["player"]["name"], "age": response_dict["player"]["age"], "nationality": response_dict["player"]["nationality"],
                          "height": response_dict["player"]["height"], "weight": response_dict["player"]["weight"],
                          "team_name": response_dict["statistics"]["team"]["name"]}

    return required_data_dict


def request_player_information(player):
    url = ("https://footapi7.p.rapidapi.com/api/search")

    querystring = {"name": player}

    headers = {
        "X-RapidAPI-Key": "ff366d3cacmshd6ce21cb5443bb4p133600jsnb4717b3c2ed9",
        "X-RapidAPI-Host": "footapi7.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    process_response(process_response(response.text))

    return process_response

