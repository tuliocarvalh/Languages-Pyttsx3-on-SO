import pyttsx3

engine = pyttsx3.init()
#For each language on OS // Para cada linguagem no SO
for voice in engine.getProperty('voices'):
    print(voice)
    