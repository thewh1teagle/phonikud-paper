// Prevent several audio/video files from playing at the same time
const mediaElements = Array.from(document.querySelectorAll('audio, video'));
mediaElements.forEach(function(media) {
    media.addEventListener('play', (event) => {
        mediaElements.forEach(function(otherMedia) {
            if(otherMedia !== event.target) {
                otherMedia.pause();
            }
        });
    });
});
