// Single media playback functionality is in single-media-playback.js

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


function scrollToNext() {
  const nextSection = document.querySelector('.architecture');
  if (nextSection) {
    nextSection.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    });
  }
}