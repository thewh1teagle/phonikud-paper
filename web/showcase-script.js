// Showcase page functionality

document.addEventListener('DOMContentLoaded', function() {
    initializeFilters();
    initializeCardInteractions();
});

function initializeFilters() {
    const filterTabs = document.querySelectorAll('.filter-tab');
    const showcaseCards = document.querySelectorAll('.showcase-card');

    filterTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Update active tab
            filterTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Get filter value
            const filterValue = tab.dataset.filter;

            // Filter cards
            showcaseCards.forEach(card => {
                if (filterValue === 'all' || card.dataset.category === filterValue) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
}

function initializeCardInteractions() {
    const showcaseCards = document.querySelectorAll('.showcase-card');

    showcaseCards.forEach(card => {
        // Skip contribute card
        if (card.classList.contains('contribute-card')) return;

        card.addEventListener('click', () => {
            // Add click interaction - could open modal or navigate
            console.log('Card clicked:', card.querySelector('.card-title')?.textContent);
            
            // Example: Add a subtle animation
            card.style.transform = 'scale(0.98)';
            setTimeout(() => {
                card.style.transform = '';
            }, 150);
        });

        // Add loading simulation for video placeholders
        const videoPlaceholder = card.querySelector('.video-placeholder');
        if (videoPlaceholder) {
            videoPlaceholder.addEventListener('click', (e) => {
                e.stopPropagation();
                simulateVideoLoad(videoPlaceholder);
            });
        }
    });
}

function simulateVideoLoad(placeholder) {
    const playIcon = placeholder.querySelector('i');
    
    // Show loading state
    playIcon.className = 'fas fa-spinner fa-spin';
    
    // Simulate load time
    setTimeout(() => {
        playIcon.className = 'fas fa-play';
        // Here you could open a modal or navigate to video
        console.log('Video would load here');
    }, 1500);
}

// Utility function to add new showcase items dynamically
function addShowcaseItem(item) {
    const gridContainer = document.querySelector('.grid-container');
    const contributeCard = document.querySelector('.contribute-card');
    
    const newCard = createShowcaseCard(item);
    gridContainer.insertBefore(newCard, contributeCard);
}

function createShowcaseCard(item) {
    const card = document.createElement('div');
    card.className = 'showcase-card';
    card.dataset.category = item.category;
    
    card.innerHTML = `
        <div class="card-media">
            <div class="video-placeholder">
                <i class="fas fa-play"></i>
                <div class="video-duration">${item.duration}</div>
            </div>
        </div>
        <div class="card-content">
            <h3 class="card-title">${item.title}</h3>
            <p class="card-description">${item.description}</p>
            <div class="card-meta">
                <span class="card-tag">${item.tag}</span>
                <span class="card-date">${item.date}</span>
            </div>
        </div>
    `;
    
    return card;
}
