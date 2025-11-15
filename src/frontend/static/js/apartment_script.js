//Edited by Andrew Ponce on 6/6/2024

// Image Gallery Navigation
document.querySelectorAll('.image-gallery').forEach(gallery => {
    const images = gallery.querySelectorAll('.apartment-image'); // Connects to elements with class 'apartment-image'
    const dots = gallery.querySelectorAll('.dot'); // Connects to elements with class 'dot'
    let currentIndex = 0;

    // Click on gallery to go to next image
    gallery.addEventListener('click', (e) => {
        if (e.target.classList.contains('dot')) return; // Skip if clicking dot
        e.stopPropagation();
        
        images[currentIndex].classList.remove('active'); // Toggles 'active' class
        dots[currentIndex].classList.remove('active'); // Toggles 'active' class
        
        currentIndex = (currentIndex + 1) % images.length;
        
        images[currentIndex].classList.add('active'); // Toggles 'active' class
        dots[currentIndex].classList.add('active'); // Toggles 'active' class
    });

    // Click on dots for direct navigation
    dots.forEach((dot, index) => {
        dot.addEventListener('click', (e) => {
            e.stopPropagation();
            
            images[currentIndex].classList.remove('active'); // Toggles 'active' class
            dots[currentIndex].classList.remove('active'); // Toggles 'active' class
            
            currentIndex = index;
            
            images[currentIndex].classList.add('active'); // Toggles 'active' class
            dots[currentIndex].classList.add('active'); // Toggles 'active' class
        });
    });
});

// Flip card on click (except when clicking images, username, pic, or button)
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', (e) => {
        // Don't flip if clicking on image gallery, username, profile pic, or button
        if (e.target.closest('.image-gallery') || // Connects to '.image-gallery'
            e.target.closest('.username') || // Connects to '.username'
            e.target.closest('.user-pic') || // Connects to '.user-pic'
            e.target.closest('.choose-button')) { // Connects to '.choose-button'
            return;
        }
        card.classList.toggle('flipped'); // Toggles 'flipped' class
    });
});

// Filter Accordion
document.querySelectorAll('.filter-header').forEach(header => {
    header.addEventListener('click', () => {
        const section = header.parentElement; // Connects to parent element of '.filter-header'
        section.classList.toggle('collapsed'); // Toggles 'collapsed' class
    });
});

// Popup elements
const popup = document.getElementById('userPopup'); // Connects to element with ID 'userPopup'
const popupContent = popup.querySelector('.popup-content'); // Connects to '.popup-content' inside popup
const popupCloseBtn = popup.querySelector('.popup-close'); // Connects to '.popup-close' inside popup

// Open user popup
document.querySelectorAll('.username, .user-pic').forEach(el => { // Connects to '.username' and '.user-pic'
    el.addEventListener('click', e => {
        e.stopPropagation();
        const card = el.closest('.card'); // Connects to closest '.card'
        if (!card) return;

        const userName = card.querySelector('.username').textContent; // Connects to '.username' inside '.card'
        const bioElement = card.querySelector('.apartment-details p:nth-last-child(1)'); // Connects to last paragraph in '.apartment-details'
        const bio = bioElement ? bioElement.textContent.replace('Bio:', '').trim() : 'No bio available';

        popupContent.innerHTML = `
            <p><strong>Name:</strong> ${userName}</p>
            <p><strong>Bio:</strong> ${bio}</p>
            <p><strong>About:</strong> Verified user with positive reviews. Responsive to messages and reliable.</p>
            <p><strong>Member Since:</strong> January 2024</p>
            <p><strong>Response Rate:</strong> 95%</p>
            <p><strong>Verified:</strong> Yes ✓</p>
        `;
        popup.classList.add('active'); // Toggles 'active' class
    });
});

// Close popup
popupCloseBtn.addEventListener('click', () => {
    popup.classList.remove('active'); // Toggles 'active' class
});

popup.addEventListener('click', e => {
    if (e.target === popup) {
        popup.classList.remove('active'); // Toggles 'active' class
    }
});

// Choose button
document.querySelectorAll('.choose-button').forEach(button => { // Connects to '.choose-button'
    button.addEventListener('click', e => {
        e.stopPropagation();
        alert('Navigating to listing details page...'); // Placeholder for navigation logic
    });
});
