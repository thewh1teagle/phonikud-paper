## Convert to opus

```console
mkdir -p ./output
for f in ./input/*.wav; do 
    filename=$(basename "$f" .wav) 
    ffmpeg -y -i "$f" -c:a aac -b:a 128k "./output/${filename}.m4a" 
done
```