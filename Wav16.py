from moviepy.editor import VideoFileClip

input_file = 'Video.mp4'
output_file = 'output.wav'

# Carregar o vídeo
video = VideoFileClip(input_file)

# Extrair o áudio
audio = video.audio

# Salvar o áudio no formato WAV
audio.write_audiofile(output_file, codec='pcm_s16le', fps=16000)
