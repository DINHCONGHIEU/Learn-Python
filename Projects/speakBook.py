import pyttsx3
import PyPDF2


sach = open()
bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice',voices[1].id)
bot.say("Hello anh Hiếu đẹp trai")


bot.runAndWait()