Normalize volume with ffmpeg -i audio.wav -af loudnorm=I=-14:TP=-1.0:LRA=11 output.wav
Softer: ffmpeg -i phonikud_112.wav -af loudnorm=I=-17:TP=-1.5:LRA=11 phonikud_1.wav