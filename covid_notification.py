from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\WebD\Python Projects\images\icon2.ico",
        timeout = 3
    )


def detData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":

    notifyMe("Anubh", "Lets stop the spread of the Corona virus together")

    # url = "https://www.mohfw.gov.in/"
    url = "https://www.mygov.in/covid-19"
    myHtmlData = detData(url)

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    myDataStr = ""
    # for tr in soup.find_all('thead')[0].find_all('tr'):
    #     myDataStr += tr.text()

    for tr in soup.find(id='stateCount').find_all('span'):
        myDataStr += tr.get_text()
    # print(myDataStr)

    # myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")
    # print(itemList)      

    for item in itemList:
        print(item.split('\n'))
