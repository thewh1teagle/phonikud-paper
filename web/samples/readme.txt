normal ffmpeg -i input.wav -af loudnorm=I=-14:TP=-1.0:LRA=11 output_regular.wav
mid ffmpeg -i input.wav -af loudnorm=I=-17:TP=-1.5:LRA=11 output_mid.wav
mid + ffmpeg -i input.wav -af loudnorm=I=-15.5:TP=-1.0:LRA=11 output_mid_plus.wav
loud ffmpeg -i input.wav -af loudnorm=I=-11:TP=-1.0:LRA=11 output_high.wav
