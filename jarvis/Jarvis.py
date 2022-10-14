from subprocess import call
import speech_recognition as sr # > install pyaudio <
from gtts import gTTS
from requests import get
from bs4 import BeautifulSoup
import webbrowser as browser # abre navegador com url's especificadas
from paho.mqtt import publish

##### CONFIGURAÇÕES #####
hotword = 'jarvis'
# with open('------api_credential_cloud_console_google.json-------') as credenciais_google:
#    credenciais_google = credenciais_google.read()


##### FUNÇÕES PRINCIPAIS #####

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando o comando: ")
            audio = microfone.listen(source)

            # Teste se o google pegou o que foi dito e transformou em texto
            # -------------------------------------------------------------
            try:
                #trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language="pt-BR")
                trigger = microfone.recognize_google(audio, language="pt-BR")
                trigger = trigger.lower()

                if (hotword in trigger):
                    print("Comando: ", trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google could not understand audio")
            except sr.RequestError as e:
                print("Google find an error: {0}".format(e))
    return trigger

def responde(arquivo):
    call(['aplay', 'audios/' + arquivo + '.mp3'])

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save('audios/mensagem.mp3')
    print('Jarvis: ', mensagem)
    call(['aplay', 'audios/mensagem.mp3'])

def executa_comandos(trigger):
    if ('noticias' in trigger):
        ultimas_noticias()
    elif ('ouvir' in trigger and 'achismos' in trigger):
        playlists('achismos')
    elif ('toca minha playlist' in trigger or 'toca aquela' in trigger):
        playlists('')
    elif ('tempo agora' in trigger):
        previsao_tempo(tempo=True)
    elif ('previsão do tempo' in trigger):
        previsao_tempo(mimax=True)
    elif ('liga os leds' in trigger):
        publica_mqtt('office/iluminacao/status', '1')
    elif ('apaga os leds' in trigger):
        publica_mqtt('office/iluminacao/status', '0')
    else:
        mensagem = trigger.strip(hotword) # Remove a hotword da frase para o Jarvis repetir o que entendeu
        cria_audio(mensagem)
        print('Comando inválido', mensagem)
        responde('comando_invalido')

##### FUNÇÕES COMANDOS #####

def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')

    for item in noticias.findAll('item')[:5]:
        mensagem = item.title.text
        cria_audio(mensagem)

def playlists(album):
    if (album == 'achismos'):
        browser.open('https://open.spotify.com/episode/6px11NcOpwuJMhVDShNXib?si=af2aa1023b88416a')
    else:
        browser.open('https://open.spotify.com/track/69CmX6WtBZ2VmB2kCXknkY?si=86f7ef40457440e5')

def previsao_tempo(tempo = False, mimax = False):
    site = get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=160d6a05ef5cf2f7cf8970b584452491&units=metric&lang=pt')
    clima = site.json()
    temperatura = clima['main']['temp']
    minima = clima['main']['temp_min']
    maxima = clima['main']['temp_max']
    descricao = clima['weather'][0]['description']

    if (tempo):
        mensagem = f'No momento fazem {temperatura} graus com: {descricao}'
    if (mimax):
        mensagem = f'Mínima de {minima} e máxima de {maxima}'

    cria_audio(mensagem)

##### MAIN #####
def publica_mqtt(topic, payload):
    publish.single(topic, payload=payload, qos=1, retain=True, hostname='m10.cloudmqtt.com',
                   port=12892, client_id="jarvis",
                   auth={'username': 'osvkktcs', 'password': 'XYTc9FUbvmb7'})
    if (payload == '1'):
        mensagem = "Leds ligados"
    else:
        mensagem = "Leds desligados"
    cria_audio(mensagem)

def main():
    while True:
        monitora_audio()

main()

