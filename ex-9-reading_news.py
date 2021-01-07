import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
if __name__ == '__main__':
    speak('News for today')
    url  = "http://newsapi.org/v2/top-headlines?country=in&apiKey=4ca2bdb7c7f742f9b95ef35050ff3d11"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for articles in arts:
        speak(articles['title'])
        speak("moving on to the next news..")
    speak("All news are read.")