import speech_recognition as sr
import webbrowser
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()


def record(ask=False):
    if ask:
        print(ask)


with sr.Microphone() as source:
    audio = r.listen(source)
    voice = ''
    try:
    voice = r.recognize_google(audio, language='tr-TR')
    except sr.UnknownValueError:
        print("tekrarlar misin anlayamadim")

    except sr.RequestError:
        print('devam edebilirsiniz')

    return voice

def response(voice):
    if  'nasilsin' in voice:
        print('teşekkürler sen nasilsin')
        if 'havalar nasil' in voice:
            print('güzel')
            if 'arama yap' in voice:
            search.record('ne aramıstiniz')
            url='https://google.com/search?g='+search
            webbrowser.get().open(url)
            print(search + ' icin bulduklarim:')
            exit()
            
            def speak(string):
                gTTS(string,lang='tr')
                rand=random.randint(1,10000)
                file= 'audio'+str(rand)+'.mp3'
                tts.save(file)
                playsound(file)
                os.remove(file)


    print("nasil yardimci olabilirim")
    voice = record()
    print(voice)
