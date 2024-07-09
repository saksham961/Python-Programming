import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

user_input = input("Please enter the text you want to convert to speech: ")

engine.say(user_input)
engine.runAndWait()
