import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import requests
import json
import time
from datetime import date

# from datetime import datetime
z = 0
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[z].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 15)
nm = "Chitttteeee"
dic = {"mayank": "mayank1220241@jmit.ac.in", "himanshu": "himanshu1220216@jmit.ac.in", "jai": "jai1220219@jmit.ac.in",
       "jatin": "jatin1220223@jmit.ac.in", "lovekesh": "lovekesh1220235@jmit.ac.in",
       "none": "If you want to write to someone else then Please enter his/her e-mail id"}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir.")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir.")
    speak(f".     My name is {nm} . I am here for your service. How can I assist you?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        speak("Listening......")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        speak("Recognizing, Please wait......")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except Exception as e:
        print(e)
        return "none"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f = open("ps.txt", "r")
    ct = f.read()
    server.login('stevenprakashpatnavale@gmail.com', ct)
    server.sendmail('stevenprakashpatnavale@gmail.com', to, content)
    server.close()


def pl(a):
    print("--" * a)


if __name__ == '__main__':
    wishme()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('wikipedia', ' ')
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia", end=" ")
            print(results)
            speak("According to wikipedia.")
            speak(results)
        elif 'open pycharm' in query:
            os.startfile(
                "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2022.1.3.lnk")
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open leetcode' in query:
            speak("Opening Leetcode")
            webbrowser.open("leetcode.com")
            time.sleep(10)
        elif 'open google' in query:
            speak("Opening Google")

            webbrowser.open("google.com")
            time.sleep(10)
        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")
        elif 'open Instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("Instagram.com")
        elif 'open javatpoint' in query:
            speak("Opening javatpoint")
            webbrowser.open("javatpoint.com")
        elif 'play music' in query:
            music_dir = r"C:\Users\hp\Music\mysongs"
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, len(songs))
            print(n)
            os.startfile(os.path.join(music_dir, songs[n]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
        elif 'email' in query:
            try:
                speak("Here are some of the receivers from your gmail Inbox. Whom do you want to Email?")
                print("Mayank\nHima\nJo\nJan\nkesh\nnone\n")
                to1 = takeCommand().lower()
                to = dic[to1]
                print(to)
                speak(to)
                if(to1=="none"):
                    to=input()
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak(f"You said {content}")

                speak("Email sent successfully!")
                print("EMAIL SENT SUCCESSFULLY")
            except Exception as e:
                print(f"ERROR GENERATED:- {e}")
                speak(f"ERROR GENERATED:- {e}")
        elif 'feedback' in query:
            try:
                speak("Sending feedback")
                print("Sending feedback........")
                #to1 = takeCommand().lower()
                to = "mayankmakhija00@gmail.com"

                print(f"To:-{to}")
                #content = "https://docs.google.com/forms/d/e/1FAIpQLSeFSZOkB8AddQOUofBS397mHWqV2C3kRBGVEcul1HZFa70hTw/viewform?usp=sf_link"

                sendEmail(to, "FEEDBACK LINK :-  https://docs.google.com/forms/d/e/1FAIpQLSeFSZOkB8AddQOUofBS397mHWqV2C3kRBGVEcul1HZFa70hTw/viewform?usp=sf_link")
                #sendEmail(to,content)

                speak("Feedback sent successfully via E-mail!")
                print("FEEDBACK SENT SUCCESSFULLY VIA E-MAIL SERVICE")
            except Exception as e:
                print(f"ERROR GENERATED:- {e}")
                speak(f"ERROR GENERATED:- {e}")


        elif 'news' in query:
            i = 1
            pl(50)
            pl(50)
            print("Top 10 headlines from BBC news.... Lets begin with our first headline")
            speak("Top 10 headlines from BBC news.... Lets begin with our first headline")
            pl(50)
            pl(50)
            url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=b0645f84eb2b46feb2b4f2e900ca70f6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                print(f"Headline No. {i} "+article['title'])
                i += 1
                speak(article['title'])
                if i < 11:
                    speak(f"Moving on to the next news. Here is headline number {i}")

            speak("Thanks for listening...")
        elif 'date' in query:
            today = date.today()
            d2 = today.strftime("%B %d, %Y")
            print("Today's date is", d2)
            speak(f"Today's date is {d2}")

        elif 'can you do' in query:
            speak("I can play music from your playlist.")
            speak("I can read news headline to you.")
            speak("Moreover, I can open websites like facebook,google,leetcode etcetra")
            speak("I can display time too")
            speak("I can search wikepedia and send E-mail")
            speak("I can also play a game")
        elif 'voice' in query:
            if z == 0:
                z = 1
                nm = "ZOEY"
            elif z == 1:
                z = 0
                nm = "Chitttteeee"
            # voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[z].id)
            speak("Changes applied successfully")
            wishme()
        elif 'exit' in query:
            speak("VOICE ASSISTANT PROGRAM TERMINATED")
            exit()
        elif ('weather' or 'temperature') in query:
            print("Which location?")
            speak("Which location?")
            location = takeCommand().lower()
            complete_api = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=546b5b655cd60b05db5bc7586cd2c8c8"
            api_link = requests.get(complete_api)
            api_data = api_link.json()
            if location == 'none':
                print("Type the city name:")
                location = input()

            temp = ((api_data['main']['temp']) - 273.15)
            desc = api_data['weather'][0]['description']
            min_tmp = (api_data['main']['temp_min'] - 273.15)
            max_tmp = (api_data['main']['temp_max'] - 273.15)
            hmd = api_data['main']['humidity']
            wnd = api_data['wind']['speed']
            date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            pl(50)
            print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
            pl(50)

            print(f"Current temperature is: {round(temp, 2)} deg C")
            print(f"Current weather description is {desc}")
            print(f"Maximum Temperature is {round(max_tmp, 2)} degree Celsius")
            print(f"Minimum Temperature is {round(min_tmp, 2)} degree Celsius")
            print(f"Current Humidity is {hmd} %")
            print(f"Current wind speed {wnd} kmph")
            speak(f"Current temperature is {round(temp, 2)} degree Celsius")
            speak(f"Current weather description is {desc}")
            speak(f"Maximum Temperature is {round(max_tmp, 2)} degree Celsius")
            speak(f"Minimum Temperature is {round(min_tmp, 2)} degree Celsius")
            speak(f"Current Humidity is {hmd} %")
            speak(f"Current wind speed {wnd} kilo meter per hour")



        elif 'play game' in query:
            l1 = ["snake", "water", "gun"]
            chances = 3
            win = 0
            # k=1
            pl(100)
            pl(100)
            print("                                                                  SNAKE 🐍 WATER 💦 AND GUN 🔫 GAME")
            pl(100)
            pl(100)
            print("You are given with 3 chances,You have to win atleast 2 times in order to win")
            speak("You are given with 3 chances,You have to win atleast 2 times in order to win")
            print("You have to choose among snake,water,gun")
            speak("You have to Choose among snake,water,gun")
            print("Gun defeats Snake\nWater defeats gun\nSnake defeats water.")
            speak("Gun defeats Snake, Water defeats gun, Snake defeats water.")
            while chances != 0:
                speak("Choose now")
                choice = takeCommand()
                m = random.choice(l1)
                if m == choice:
                    print("It's a Tie\nNO SCORE FOR TIE GAME")
                    speak("It's a Tie . NO SCORE FOR TIE GAME")
                    pl(20)

                else:
                    if (choice == "snake") or (choice == "water") or (choice == "gun"):
                        if m == "snake" and choice == "gun":
                            print("You Win")
                            speak("You Win")
                            win = win + 1
                            # speak(f"Opponent's choice was {m}")
                        elif m == "snake" and choice == "water":
                            print("You Lost")
                            speak("You Lost")
                            # speak(f"Opponent's choice was {m}")
                        elif m == "water" and choice == "gun":
                            print("You Lost")
                            speak("You Lost")
                            # speak(f"Opponent's choice was {m}")
                        elif m == "water" and choice == "snake":
                            print("You Win")
                            speak("You Win")
                            win = win + 1
                            # speak(f"Opponent's choice was {m}")
                        elif m == "gun" and choice == "water":
                            print("You Win")
                            speak("You Win")
                            # speak(f"Opponent's choice was {m}")
                            win = win + 1
                        elif m == "gun" and choice == "snake":
                            print("You lost")
                            speak("You Lost")
                        elif choice=="exit":
                            exit()
                        chances=chances-1
                        print(f"Opponent's choice was {m}")
                        speak(f"Opponent's choice was {m}")


                    else:
                        speak("Didn't get that")
                        speak("Please try again")



                    pl(20)
            if win >= 2:
                print(f"You win the game by {win} wins out of 3")
                speak(f"You win the game by {win} wins out of 3")
            else:
                print(f"You lost the game by {win} wins out of 3")
                speak(f"You lost the game by {win} wins out of 3")

            pl(50)

        else:
            speak("Sorry, Can you please repeat..?")
            print("Sorry, Can you please repeat..?")
