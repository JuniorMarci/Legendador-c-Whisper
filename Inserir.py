import subprocess

ffmpeg_path = ".\\ffmpeg-2023-05-15-git-2953ebe7b6-full_build\\bin\\ffmpeg.exe"
video_file = "Video.mp4"
subtitle_file = "Legendas.srt"
output_file = "video_com_legendas.mp4"

# Comando FFmpeg para adicionar legendas ao vídeo
command = f'{ffmpeg_path} -i "{video_file}" -vf subtitles="{subtitle_file}" "{output_file}"'

# Executa o comando FFmpeg
subprocess.call(command, shell=True)
