<<<<<<< HEAD
// Image Gallery Navigation
document.querySelectorAll('.image-gallery').forEach(gallery => {
=======
// Edited by Andrew Ponce on 6/6/2024

// Image Gallery Navigation
document.querySelectorAll('.image-gallery').forEach(gallery => {
    /**
     * Handles image gallery navigation.
     * - Clicking on the gallery cycles through images.
     * - Clicking on dots navigates directly to the corresponding image.
     * Edited by Andrew Ponce on 6/6/2024
     */
>>>>>>> apartments
    const images = gallery.querySelectorAll('.apartment-image');
    const dots = gallery.querySelectorAll('.dot');
    let currentIndex = 0;

<<<<<<< HEAD
    // Click on gallery to go to next image
    gallery.addEventListener('click', (e) => {
        if (e.target.classList.contains('dot')) return; // Skip if clicking dot
=======
    gallery.addEventListener('click', (e) => {
        /**
         * Cycles to the next image when the gallery is clicked.
         * Skips if a dot is clicked.
         * Edited by Andrew Ponce on 6/6/2024
         */
        if (e.target.classList.contains('dot')) return;
>>>>>>> apartments
        e.stopPropagation();
        
        images[currentIndex].classList.remove('active');
        dots[currentIndex].classList.remove('active');
        
        currentIndex = (currentIndex + 1) % images.length;
        
        images[currentIndex].classList.add('active');
        dots[currentIndex].classList.add('active');
    });

<<<<<<< HEAD
    // Click on dots for direct navigation
    dots.forEach((dot, index) => {
=======
    dots.forEach((dot, index) => {
        /**
         * Navigates directly to the selected image when a dot is clicked.
         * Edited by Andrew Ponce on 6/6/2024
         */
>>>>>>> apartments
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
<<<<<<< HEAD
    card.addEventListener('click', (e) => {
        // Don't flip if clicking on image gallery, username, profile pic, or button
=======
    /**
     * Toggles the "flipped" class on a card when clicked.
     * Skips flipping if the click is on an image, username, user picture, or button.
     * Edited by Andrew Ponce on 6/6/2024
     */
    card.addEventListener('click', (e) => {
>>>>>>> apartments
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
<<<<<<< HEAD
=======
    /**
     * Toggles the "collapsed" class on a filter section when its header is clicked.
     * Edited by Andrew Ponce on 6/6/2024
     */
>>>>>>> apartments
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
<<<<<<< HEAD
=======
    /**
     * Opens the user popup with details when a username or user picture is clicked.
     * Edited by Andrew Ponce on 6/6/2024
     */
>>>>>>> apartments
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
<<<<<<< HEAD
=======
    /**
     * Closes the user popup when the close button is clicked.
     * Edited by Andrew Ponce on 6/6/2024
     */
>>>>>>> apartments
    popup.classList.remove('active');
});

popup.addEventListener('click', e => {
<<<<<<< HEAD
=======
    /**
     * Closes the user popup when clicking outside the popup content.
     * Edited by Andrew Ponce on 6/6/2024
     */
>>>>>>> apartments
    if (e.target === popup) {
        popup.classList.remove('active');
    }
});

// Choose button
document.querySelectorAll('.choose-button').forEach(button => {
<<<<<<< HEAD
=======
    /**
     * Handles the "Choose" button click event.
     * Displays an alert and navigates to the listing details page.
     * Edited by Andrew Ponce on 6/6/2024
     */
>>>>>>> apartments
    button.addEventListener('click', e => {
        e.stopPropagation();
        alert('Navigating to listing details page...');
    });
});
