import subprocess
import Wav16


comando = 'move "output.wav" "Whisper\Audio.wav"'
subprocess.call(comando, shell=True)


import Whisper



comando = 'move "Whisper\Audio.wav.srt" Legendas.srt'
subprocess.call(comando, shell=True)


import Inserir