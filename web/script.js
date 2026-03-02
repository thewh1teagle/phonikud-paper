// Initialize Lucide icons
lucide.createIcons();

// Single media playback functionality is in single-media-playback.js

// Copy citation function
function copyToClipboard() {
    const citation = document.querySelector('.citation-box pre code').textContent;
    navigator.clipboard.writeText(citation).then(() => {
        const btn = document.querySelector('.copy-btn');
        const originalHTML = btn.innerHTML;
        btn.innerHTML = '<i data-lucide="check"></i>';
        btn.style.color = '#16a34a';
        lucide.createIcons({ nodes: [btn] });
        setTimeout(() => {
            btn.innerHTML = originalHTML;
            btn.style.color = '';
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