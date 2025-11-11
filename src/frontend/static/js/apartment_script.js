// Image Gallery Navigation
document.querySelectorAll('.image-gallery').forEach(gallery => {
    const images = gallery.querySelectorAll('.apartment-image');
    const dots = gallery.querySelectorAll('.dot');
    let currentIndex = 0;

    // Click on gallery to go to next image
    gallery.addEventListener('click', (e) => {
        if (e.target.classList.contains('dot')) return; // Skip if clicking dot
        e.stopPropagation();
        
        images[currentIndex].classList.remove('active');
        dots[currentIndex].classList.remove('active');
        
        currentIndex = (currentIndex + 1) % images.length;
        
        images[currentIndex].classList.add('active');
        dots[currentIndex].classList.add('active');
    });

    // Click on dots for direct navigation
    dots.forEach((dot, index) => {
        dot.addEventListener('click', (e) => {
            e.stopPropagation();
            
            images[currentIndex].classList.remove('active');
            dots[currentIndex].classList.remove('active');
            
            currentIndex = index;
            
            images[currentIndex].classList.add('active');
            dots[currentIndex].classList.add('active');
        });
    });
});

// Flip card on click (except when clicking images, username, pic, or button)
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', (e) => {
        // Don't flip if clicking on image gallery, username, profile pic, or button
        if (e.target.closest('.image-gallery') || 
            e.target.closest('.username') || 
            e.target.closest('.user-pic') || 
            e.target.closest('.choose-button')) {
            return;
        }
        card.classList.toggle('flipped');
    });
});

// Filter Accordion
document.querySelectorAll('.filter-header').forEach(header => {
    header.addEventListener('click', () => {
        const section = header.parentElement;
        section.classList.toggle('collapsed');
    });
});

// Popup elements
const popup = document.getElementById('userPopup');
const popupContent = popup.querySelector('.popup-content');
const popupCloseBtn = popup.querySelector('.popup-close');

// Open user popup
document.querySelectorAll('.username, .user-pic').forEach(el => {
    el.addEventListener('click', e => {
        e.stopPropagation();
        const card = el.closest('.card');
        if (!card) return;

        const userName = card.querySelector('.username').textContent;
        const bioElement = card.querySelector('.apartment-details p:nth-last-child(1)');
        const bio = bioElement ? bioElement.textContent.replace('Bio:', '').trim() : 'No bio available';

        popupContent.innerHTML = `
            <p><strong>Name:</strong> ${userName}</p>
            <p><strong>Bio:</strong> ${bio}</p>
            <p><strong>About:</strong> Verified user with positive reviews. Responsive to messages and reliable.</p>
            <p><strong>Member Since:</strong> January 2024</p>
            <p><strong>Response Rate:</strong> 95%</p>
            <p><strong>Verified:</strong> Yes ✓</p>
        `;
        popup.classList.add('active');
    });
});

// Close popup
popupCloseBtn.addEventListener('click', () => {
    popup.classList.remove('active');
});

popup.addEventListener('click', e => {
    if (e.target === popup) {
        popup.classList.remove('active');
    }
});

// Choose button
document.querySelectorAll('.choose-button').forEach(button => {
    button.addEventListener('click', e => {
        e.stopPropagation();
        alert('Navigating to listing details page...');
    });
});
