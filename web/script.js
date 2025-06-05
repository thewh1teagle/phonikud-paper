// Prevent several audio files from playing at the same time
const tracks = Array.from(document.querySelectorAll('audio'));
tracks.forEach(function(track) {
    track.addEventListener('play', (event) => {
      tracks.forEach(function(track) {
        if(track !== event.target) track.pause();
      })
    })
})

// Copy citation function
function copyToClipboard() {
    const citation = document.querySelector('.citation-box pre code').textContent;
    navigator.clipboard.writeText(citation).then(() => {
        const btn = document.querySelector('.copy-btn');
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
        setTimeout(() => {
            btn.innerHTML = originalText;
        }, 2000);
    });
}