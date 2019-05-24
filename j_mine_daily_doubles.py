import urllib.request
import re

# defines empty list for categories to be added to as strings
dd = []

def category_search(game_id):
    '''
    Mines the locatoin of the daily double from the game Jeopardy! from j-archive.com using regular expressions
    :param game_id: int, the game_id is used to access the individual game itself, the game id denotes the php link
    :return: None, adds values to a list instead when the function is called
    '''
    # defines regular expressions for searching for categories
    dd_location = re.compile(r"class=\"category_name\">(.*)</td>") # TODO: Update DD Regex

    # data mined from j-archive.com, which some categories are displayed as links to nothing (frustrating)
    # these regexes allow the links to be deconstructed into string
    a_inner = re.compile(r"target=\"_blank\">(.*)</a>")
    e_inner = re.compile(r"class=\"underline\">(.*)</em>")

    # if the link doesn't open, move on to the next game_id
    try:
        link = "http://www.j-archive.com/showgame.php?game_id=" + str(game_id)
        connection = urllib.request.urlopen(link)
    except urllib.HTTPError as e:
        if e.code == 404:
            return None
        else:
            raise

    # if the link does open, read and decode
    text = connection.read().decode("utf-8")
    d_findr = re.compile(dd_location)

    # search for possible matches to categories by recognizing patterns of html code
    for match in d_findr.finditer(text):
        ans = (match.group(1))
        dd.append(ans)

# will search through n number of games
number_of_games = 100
for i in range(number_of_games):
    category_search(i)
print(categories)
