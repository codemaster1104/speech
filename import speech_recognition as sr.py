import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    #r.adjust_for_ambient_noise(source,duration=0.5)
    audio = r.listen(source)

try:
   
    #print(r.recognize_google(audio, show_all=True))
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


