import urllib.request
import re
import time

#defines a dictionary mapping years to daily double wagers
daily_doubles = {}

def has_key(key, dict):
    '''
    Helper function for the daily_double_search function: determines if a key is in a dictionary in O(n) time
    :param key:(string, int, etc.), a key to a dictionary
    :param dict: dictionary, any object of type dict
    :return: boolean value, returns true if key is in the dictionary, returns false otherwise
    '''
    if (key in dict.keys()):
        return True
    return False

def daily_double_search(game_id):
    global daily_doubles
    '''
    Mines the cateogy type from the game Jeopardy! from j-archive.com using regular expressions
    :param game_id: int, the game_id is used to access the individual game itself, the game id denotes the php link
    :return: None, adds values to a list instead when the function is called
    '''
    # defines regular expressions for searching for daily double wagers and years of the wagers
    game_year = re.compile(r"<div id=\"game_title\"><h1>Show #[0-9]* - [A-Za-z ,]*[0-9 ]*, (.*)</h1></div>")
    dd_val = re.compile(r"<td class=\"clue_value_daily_double\">DD: \$([0-9,]*)</td>")

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
    yr_findr = re.compile(game_year)
    dd_findr = re.compile(dd_val)
    values = []
    year = ""

    # search for possible matches to categories by recognizing patterns of html code
    for match in yr_findr.finditer(text):
        year = (match.group(1))
    for match in dd_findr.finditer(text):
        values.append(match.group(1))

    # if the year is already accounted for, add values
    if (year != "" and has_key(year, daily_doubles)):
        for each in values:
            daily_doubles[year].append(each)
    # if the year is not in the dictionary, add the values
    elif (year != ""):
        daily_doubles[year] = values

# counts the time to execute the code
itr = 100
t0 = time.time()
for i in range(itr):
    daily_double_search(i)
t1 = time.time()
time=t1-t0

print("Total Time to run this code:", round(time,2), "seconds")
