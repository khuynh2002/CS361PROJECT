import PySimpleGUI as sg
import players
from worldcup import get_winner
from worldcup import get_matches


sg.theme("DarkAmber")


def home():
    layout = [
        [sg.Button("Players", tooltip="Search for players in a vast database"),
         sg.Button("Clubs", tooltip="Search for clubs in a vast database using custom search or filters"),
         sg.Button("Competitions", tooltip="Soon to be released"), sg.Exit()]]

    window = sg.Window("Futbol database", layout, default_element_size=(45, 1), resizable=True, finalize=True)
    return window


def players_screen():
    layout = [
        [sg.Button("Home"), sg.Button('Search Player'), sg.Button('Reset Search')],
        [sg.Text("Type Player: "), sg.Input(key='-PLAYER-', do_not_clear=True, size=(20, 1), tooltip="Search using custom parameters")],
         [sg.Text('Age: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-AGE-')],
         [sg.Text('Nationality: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='NATION')],
         [sg.Text('Height: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-HEIGHT-')],
         [sg.Text('Weight: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-WEIGHT-')],
         [sg.Text('Team Name: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-TEAM_NAME-')]
         ]
    window = sg.Window("Search for players", layout, default_element_size=(45, 1), resizable=True, finalize=True)
    while True:
        event, values = window.read()
        if event == "Home" or event == sg.WIN_CLOSED:
            break
        if event == "Search Player":
            player_info = players.request_player_information(values['-PLAYER-'])
            window['-AGE-'].Update(player_info['age'])
            window['-NATION-'].Update(player_info['nationality'])
            window['-HEIGHT-'].Update(player_info['height'])
            window['-WEIGHT-'].Update(player_info['weight'])
            window['-TEAM_NAME-'].Update(player_info['team_name'])

    window.close()


def clubs_screen():
    layout = [
        [sg.Button("Home"), sg.Button('Search Club'), sg.Button("Reset Search")],
        [sg.Text("Search specifically:"), sg.Input(key='-CLUB-', do_not_clear=True, size=(20, 1))],
        [sg.Text("Filters:")],
        [sg.Text("Country:"), sg.Combo(['placeholder (none)'], key='tester')],
        [sg.Text("League:"), sg.Combo(['placeholder (none)'], key='tester')],
        [sg.Text("Cups:"), sg.Combo(['placeholder (none)'], key='tester')],
    ]

    win = sg.Window("Search for clubs", layout, default_element_size=(45, 1), resizable=True, finalize=True)
    while True:
        event, values = win.read()
        if event == "Home" or event == sg.WIN_CLOSED:
            break
    win.close()

def world_cup():
    layout = [
        [sg.Button("Home"), sg.Button("Reset Search")],
        [sg.Text("Year:"), sg.Input(key='-YEAR-', do_not_clear=True, size=(20, 1)), sg.Button('Search Winner') ],
        [sg.Text("Nation:"), sg.Input(key='-NATION-', do_not_clear=True, size=(20, 1)), sg.Button('Search Matches')],
        [sg.Text('', key='-OUT-',size=(20, 100))],
    ]

    win = sg.Window("World Cup Winners and Matches", layout, default_element_size=(45, 1), resizable=True, finalize=True)
    while True:
        event, values = win.read()
        if event == "Home" or event == sg.WIN_CLOSED:
            break
        if event == 'Search Winner':
            year = values["-YEAR-"]
            # output = competition(year)
            win['-OUT-'].update(get_winner(year))
        if event == 'Search Matches':
            year = values["-YEAR-"]
            nation = values["-NATION-"]
            # output = competition(year)
            win['-OUT-'].update(get_matches(year, nation))



    win.close()
window1, window2 = home(), None


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED or event == 'Exit':
        if sg.popup_yes_no('Are you sure to exit?') == "Yes":
            break
        elif sg.popup_yes_no('Are you sure to exit?') == "No":
            None
        if window == window2:
            window2 = None
        elif window == window1:
            break

    elif event == "Players" and not window2:
        players_screen()

    elif event == "Clubs" and not window2:
        clubs_screen()

    elif event == "Competitions":
        world_cup()

window.close()





