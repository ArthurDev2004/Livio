const items = [
  // IMPORTANT: All starting items now include the 'category' property.
  { id: 1, title: "240", name: "Vintage Desk Lamp", description: "Classic brass lamp, fully functional. Needs new bulb. Great for late-night studying.", condition: "Used - Good", category: "Home & Garden", img: "https://i.imgur.com/CcFf1mJ.jpeg" },
  { id: 2, title: "250", name: "Leather Sofa", description: "Three-seater leather sofa, great condition, smoke-free home. Comfortable and spacious for movie nights.", condition: "Used - Good", category: "Home & Garden", img: "https://i.imgur.com/Vb9Fv8S.jpeg" },
  { id: 3, title: "170", name: "Mini Fridge", description: "Compact refrigerator, perfect for dorms or garages. Works great and holds beverages/snacks.", condition: "Used - Good", category: "Electronics & Media", img: "https://i.imgur.com/7czJ1Pm.jpeg" },
  { id: 4, title: "300", name: "Noise-Cancelling Headphones", description: "Brand new, sealed in box. Excellent sound quality with active noise cancellation, perfect for focus.", condition: "New", category: "Electronics & Media", img: "https://i.imgur.com/OuMNxYx.jpeg" },
  { id: 5, title: "220", name: "Mountain Bike (Mens)", description: "Used mountain bike, needs new tires and a quick tune-up. Frame is solid, ready for trails or commute.", condition: "Used - Fair", category: "Sports & Outdoors", img: "https://i.imgur.com/0DRK0gE.jpeg" },
  { id: 6, title: "190", name: "Textbook Bundle", description: "Used psychology and sociology textbooks from Fall semester. Pages are highlighted, but notes are helpful.", condition: "Used - Good", category: "Collectibles & Art", img: "https://i.imgur.com/j8jhTnM.jpeg" },
];

// --- DOM Element Selection ---
const itemGrid = document.getElementById("itemGrid");
const addItemModal = document.getElementById("addItemModal");
const itemDetailModal = document.getElementById("itemDetailModal"); 

const openModalBtn = document.getElementById("openModalBtn");
const fabAddItem = document.getElementById("fabAddItem");
const closeModalBtn = document.getElementById("closeModalBtn");
const closeDetailModalBtn = document.getElementById("closeDetailModalBtn"); 
const addItemForm = document.getElementById("addItemForm");

// Filter Elements
const applyFiltersBtn = document.querySelector('.apply-btn');
const categoryCheckboxes = document.querySelectorAll('#categoryFilter input[type="checkbox"]');
// Selecting condition checkboxes, assuming they are the second .checkbox-group in the filter-panel
const conditionCheckboxes = document.querySelectorAll('.filter-panel .checkbox-group:nth-of-type(2) input[type="checkbox"]'); 
const minPriceInput = document.getElementById('minPrice');
const maxPriceInput = document.getElementById('maxPrice');
const searchBar = document.querySelector('.search-bar');
const searchBtn = document.querySelector('.search-btn');


// --- Modal Handlers: Add Item ---

/**
 * Opens the "Post New Listing" modal.
 */
function openAddItemModal() {
    addItemModal.classList.remove("hidden");
    addItemModal.style.display = 'flex';
}

/**
 * Closes the "Post New Listing" modal with a fade-out effect.
 */
function closeAddItemModal() {
    addItemModal.classList.add("hidden");
    // Wait for the opacity transition to complete before hiding display
    setTimeout(() => {
        addItemModal.style.display = 'none';
    }, 300); 
}


// --- Modal Handlers: Item Details ---

/**
 * Opens the item detail modal and populates it with data for the given item ID.
 * @param {number} itemId - The unique ID of the item to display.
 */
function openItemDetailModal(itemId) {
    // Find the item by its ID
    const item = items.find(i => i.id === itemId);

    if (!item) {
        console.error("Item not found for ID:", itemId);
        return;
    }

    // Populate the modal content with all required details
    document.getElementById('detailImg').src = item.img;
    document.getElementById('detailTitle').textContent = item.name;
    // Format price to two decimal places, or show placeholder text
    document.getElementById('detailPrice').textContent = parseFloat(item.title) ? `$${parseFloat(item.title).toFixed(2)}` : 'Contact for Price';
    document.getElementById('detailCondition').textContent = item.condition;
    document.getElementById('detailCategory').textContent = item.category; // Display category
    document.getElementById('detailDescription').textContent = item.description;

    // Show the modal
    itemDetailModal.classList.remove("hidden");
    itemDetailModal.style.display = 'flex';
}

/**
 * Handles the closing of the "View Details" modal.
 */
function closeItemDetailModal() {
    itemDetailModal.classList.add("hidden");
    setTimeout(() => {
        itemDetailModal.style.display = 'none';
    }, 300); 
}

// --- Filtering Logic ---

/**
 * Reads all filter inputs (categories, conditions, price, search) and returns the filtered array of items.
 */
function applyFilters() {
    let filteredItems = [...items];

    // 1. Category Filter Logic
    const selectedCategories = Array.from(categoryCheckboxes)
        .filter(cb => cb.checked)
        .map(cb => cb.dataset.filter);
        
    if (selectedCategories.length > 0) {
        filteredItems = filteredItems.filter(item => selectedCategories.includes(item.category));
    }
    
    // 2. Condition Filter Logic
    const selectedConditions = Array.from(conditionCheckboxes)
        .filter(cb => cb.checked)
        .map(cb => cb.dataset.filter);
        
    if (selectedConditions.length > 0) {
        filteredItems = filteredItems.filter(item => selectedConditions.includes(item.condition));
    }

    // 3. Price Filter Logic - FIXED
    const minPrice = parseFloat(minPriceInput.value);
    const maxPrice = parseFloat(maxPriceInput.value);
    
    // Filter items where the price (stored in item.title) falls within the range.
    if (!isNaN(minPrice) || !isNaN(maxPrice)) {
        filteredItems = filteredItems.filter(item => {
            // Convert the item's price string to a number. If it can't be parsed, treat it as null/0.
            const itemPrice = parseFloat(item.title);

            // Skip items with invalid or zero price when filtering by price.
            if (isNaN(itemPrice) || itemPrice <= 0) {
                // If we are filtering by price, we might want to exclude non-priced items, 
                // but for now, we only exclude if price is zero/invalid AND both min/max are set.
                // However, the original code allowed prices to be 0 or invalid, so we just
                // check if the price meets the criteria.
                return true; 
            }

            const passesMin = isNaN(minPrice) || itemPrice >= minPrice;
            const passesMax = isNaN(maxPrice) || itemPrice <= maxPrice;

            return passesMin && passesMax;
        });
    }

    // 4. Search Bar Logic (for text matching name/description)
    const searchTerm = searchBar.value.toLowerCase().trim();
    if (searchTerm) {
        filteredItems = filteredItems.filter(item => 
            item.name.toLowerCase().includes(searchTerm) || 
            item.description.toLowerCase().includes(searchTerm)
        );
    }

    return filteredItems;
}


// --- Rendering Logic ---

/**
 * Renders the given array of items to the grid. (Renamed from loadItems)
 * @param {Array} itemsToRender - The array of items to display.
 */
function renderItems(itemsToRender) {
  itemGrid.innerHTML = ''; // Clear existing items
  
  if (itemsToRender.length === 0) {
      itemGrid.innerHTML = '<p style="color: #ccc; grid-column: 1 / -1; text-align: center;">No items match your current filter criteria.</p>';
      return;
  }
    
  itemsToRender.forEach(item => {
    const card = document.createElement("div");
    card.classList.add("item-card");
    
    // Fallback display name and formatted price
    const displayName = item.name || `Item (ID: ${item.id})`;
    const priceValue = parseFloat(item.title) ? `$${parseFloat(item.title).toFixed(2)}` : 'Contact for Price';

    card.innerHTML = `
      <img src="${item.img}" alt="${displayName}" onerror="this.onerror=null; this.src='https://placehold.co/400x300/1e204a/fff?text=No+Image';">
      <h4>${displayName}</h4> 
      <p>${item.condition}</p>
      <p class="price">${priceValue}</p>
      <div class="card-actions">
          <button class="view-details-btn" data-item-id="${item.id}">View Details</button> 
          <button class="make-offer-btn">Make Offer</button>
      </div>
    `;
    itemGrid.appendChild(card);
  });
  
  // Attach event listeners to the new "View Details" buttons
  document.querySelectorAll('.view-details-btn').forEach(button => {
      button.addEventListener('click', (e) => {
          // Retrieve the item ID from the button's data attribute and parse it to an integer
          const itemId = parseInt(e.target.dataset.itemId);
          openItemDetailModal(itemId);
      });
  });
}

/**
 * Main function to apply filters and update the displayed items.
 */
function updateMarketplace() {
    const itemsToDisplay = applyFilters();
    renderItems(itemsToDisplay);
}


/**
 * Handles the form submission for a new item listing.
 * @param {Event} e - The form submission event.
 */
function handleAddItemSubmission(e) {
    e.preventDefault();
    
    // 1. Collect Form Data
    const name = document.getElementById('itemTitle').value.trim(); 
    const category = document.getElementById('itemCategory').value; 
    const price = document.getElementById('itemPrice').value;
    const condition = document.getElementById('itemCondition').value;
    const description = document.getElementById('itemDescription').value.trim();
    const pictureFile = document.getElementById('itemPicture').files[0];

    // Simple validation
    if (!name || !category || !price || !condition || !description) { 
        console.error("All required fields must be filled.");
        return;
    }

    // 2. Determine the image URL. Use a placeholder if no file is uploaded.
    let imageUrl = 'https://placehold.co/400x300/1e204a/fff?text=NEW+LISTING';
    
    if (pictureFile) {
        // Create a temporary local URL for the image display
        imageUrl = URL.createObjectURL(pictureFile); 
    }

    // 3. Create the new item object with a unique ID
    const newItem = {
        id: Date.now(), // Unique ID based on timestamp
        title: price,   
        name: name,     
        condition: condition,
        category: category, 
        img: imageUrl,  
        description: description 
    };
    
    // 4. Add the new item to the local array (at the beginning so it shows up first)
    items.unshift(newItem); 

    console.log(`Successfully added new listing: ${name} in category: ${category}`);

    // 5. Update the UI to show the new item
    updateMarketplace(); // Use the main update function
    
    // 6. Clear form and close modal
    addItemForm.reset();
    closeAddItemModal();
}


// --- Global Event Listeners ---

// Add Item Modal Listeners
// openModalBtn.addEventListener('click', openAddItemModal); // Removed: Redundant button
fabAddItem.addEventListener('click', openAddItemModal);
closeModalBtn.addEventListener('click', closeAddItemModal);

// Close Add Item Modal when clicking outside the content area
addItemModal.addEventListener('click', (e) => {
    if (e.target === addItemModal) {
        closeAddItemModal();
    }
});
addItemForm.addEventListener('submit', handleAddItemSubmission);

// View Details Modal Listener
closeDetailModalBtn.addEventListener('click', closeItemDetailModal);

// Close Detail Modal when clicking outside the content area
itemDetailModal.addEventListener('click', (e) => {
    if (e.target === itemDetailModal) {
        closeItemDetailModal();
    }
});

// Filter Listeners
applyFiltersBtn.addEventListener('click', updateMarketplace);
searchBtn.addEventListener('click', updateMarketplace);

// Add listener to search bar for 'Enter' key press
searchBar.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        updateMarketplace();
    }
});

// Initial load of items when the script runs
window.onload = updateMarketplace;
