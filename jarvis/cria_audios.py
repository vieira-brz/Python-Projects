from gtts import gTTS # Texto em voz
from subprocess import call

#MACOS call (['afplay', 'audios/hello.mp3'])

#LINUX call (['aplay', 'audios/hello.mp3'])

# WINDOWS
# Incluir: from playsound import playsound
#          playsound('audios/hello.mp3')

def cria_audio(audio):
    tts = gTTS(audio, lang="pt-br")
    tts.save('audios/comando_invalido.mp3'.format(audio))
    call(['aplay', 'audios/comando_invalido.mp3'.format(audio)])

cria_audio('Desculpe senhor, não pude realizar seu pedido!')