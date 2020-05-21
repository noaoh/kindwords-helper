#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
import argparse
import configparser


def download_notification_webpage(notification_url):
    resp = urllib.request.urlopen(notification_url)
    data = resp.read()
    text = data.decode("utf-8")
    return text


def parse_notification_webpage(notification_webpage):
    soup = BeautifulSoup(notification_webpage, "html.parser")
    messageDiv = soup.find("p")
    message = messageDiv.text.strip()
    return message


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    # This means it's the first time using this helper
    if config['settings']['notification_url'] == "": 
        print('''
        Welcome friend!
        I see that it's your first time using this little helper!
        I have only one simple request:
        Open the game.
        Then click the start button.
        Then click the button with three dots in the lower right corner.
        Then then click on the notifications button.
        That should open a page in your web browser.
        '''
        )
        notification_url = input("Paste the url of that page into here: ")
        config['settings']['notification_url'] = notification_url 
        with open("config.ini", "w") as configfile:
            config.write(configfile)
        print('''
        Thanks for the info friend!
        Hope you enjoy using this little tool as much as I enjoyed making it!
        ''')

    t = download_notification_webpage(config['settings']['notification_url'])
    print(parse_notification_webpage(t))


