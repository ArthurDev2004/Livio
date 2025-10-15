// ORIGINAL START DATE PICKER CODE (DO NOT MODIFY)
const datepick = document.querySelector('.datepick');
const dateinput = document.querySelector('.date-input');
const yearinput = datepick.querySelector('.year-input');
const monthinput = datepick.querySelector('.month-input');
const cancelBtn = datepick.querySelector('.cancel');
const applyBtn = datepick.querySelector('.apply');
const nextBtn = datepick.querySelector('.next');
const prevBtn = datepick.querySelector('.prev');    
const date = datepick.querySelector('.date');

let selectdate = new Date();
let year = selectdate.getFullYear();
let month = selectdate.getMonth();

dateinput.addEventListener('click', () => {
  datepick.hidden = false;
});

cancelBtn.addEventListener('click', () => {
  datepick.hidden = true;
});

applyBtn.addEventListener('click', () => {
  dateinput.value = selectdate.toLocaleDateString('en-US', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
  datepick.hidden = true;
  calculatePrice();
});

nextBtn.addEventListener('click', () => {
  if (month === 11) year++;
  month = (month + 1) % 12;
  displayDate();
});

prevBtn.addEventListener('click', () => {
  if (month === 0) year--;
  month = (month - 1 + 12) % 12;
  displayDate();
});

monthinput.addEventListener('change', () => {
  month = monthinput.selectedIndex;
  displayDate();
});

yearinput.addEventListener('change', () => {
  year = yearinput.value;
  displayDate();
});

const updateYearMonth = () => {
  monthinput.selectedIndex = month;
  yearinput.value = year;
};

// Updated to prevent past-date selection
const handleDateClick = (e) => {
  const button = e.target;
  const selectedDay = parseInt(button.textContent);
  
  // Candidate date for the day clicked
  const candidateDate = new Date(year, month, selectedDay);
  
  // Compare only date (set hours to midnight)
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  candidateDate.setHours(0, 0, 0, 0);

  if (candidateDate < today) {
    alert("Invalid date.");
    return;
  }

  const selected = date.querySelector('.selected');
  selected && selected.classList.remove('selected');
  button.classList.add('selected');
  selectdate = candidateDate;
};

const displayDate = () => {
  updateYearMonth();
  date.innerHTML = "";
  
  const lastofPrevMonth = new Date(year, month, 0);
  for (let i = 0; i <= lastofPrevMonth.getDay(); i++) {
    const text = lastofPrevMonth.getDate() - lastofPrevMonth.getDay() + i;
    const button = createButton(text, true);
    date.appendChild(button);
  }
  
  const lastofMonth = new Date(year, month + 1, 0);
  for (let i = 1; i <= lastofMonth.getDate(); i++) {
    const button = createButton(i, false);
    button.addEventListener('click', handleDateClick);
    date.appendChild(button);
  }
  
  const firstofNextMonth = new Date(year, month + 1, 1);
  for (let i = firstofNextMonth.getDay(); i < 7; i++) {
    const text = firstofNextMonth.getDate() - firstofNextMonth.getDay() + i;
    const button = createButton(text, true);
    date.appendChild(button);
  }
};

const createButton = (text, isDisabled = false) => {  
  const currentDate = new Date();
  const isToday =
    currentDate.getDate() === text &&
    currentDate.getFullYear() === year &&
    currentDate.getMonth() === month;
  
  const select =
    selectdate.getDate() === text &&
    selectdate.getFullYear() === year &&
    selectdate.getMonth() === month;
  
  const button = document.createElement('button');
  button.textContent = text;
  button.disabled = isDisabled;
  button.classList.toggle('today', isToday);
  button.classList.toggle('select', select);
  return button;
};

displayDate();

// NEW: END DATE PICKER CODE (ADDED WITHOUT MODIFYING ORIGINAL)
const datepickEnd = document.querySelector('.datepick-end');
const dateinputEnd = document.querySelector('.date-input-end');
const yearinputEnd = datepickEnd.querySelector('.year-input-end');
const monthinputEnd = datepickEnd.querySelector('.month-input-end');
const cancelBtnEnd = datepickEnd.querySelector('.cancel-end');
const applyBtnEnd = datepickEnd.querySelector('.apply-end');
const nextBtnEnd = datepickEnd.querySelector('.next-end');
const prevBtnEnd = datepickEnd.querySelector('.prev-end');
const dateEnd = datepickEnd.querySelector('.date-end');

let selectdateEnd = new Date();
let yearEnd = selectdateEnd.getFullYear();
let monthEnd = selectdateEnd.getMonth();

dateinputEnd.addEventListener('click', () => {
  datepickEnd.hidden = false;
});

cancelBtnEnd.addEventListener('click', () => {
  datepickEnd.hidden = true;
});

applyBtnEnd.addEventListener('click', () => {
  dateinputEnd.value = selectdateEnd.toLocaleDateString('en-US', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
  datepickEnd.hidden = true;
  calculatePrice();
});

nextBtnEnd.addEventListener('click', () => {
  if (monthEnd === 11) yearEnd++;
  monthEnd = (monthEnd + 1) % 12;
  displayDateEnd();
});

prevBtnEnd.addEventListener('click', () => {
  if (monthEnd === 0) yearEnd--;
  monthEnd = (monthEnd - 1 + 12) % 12;
  displayDateEnd();
});

monthinputEnd.addEventListener('change', () => {
  monthEnd = monthinputEnd.selectedIndex;
  displayDateEnd();
});

yearinputEnd.addEventListener('change', () => {
  yearEnd = yearinputEnd.value;
  displayDateEnd();
});

const updateYearMonthEnd = () => {
  monthinputEnd.selectedIndex = monthEnd;
  yearinputEnd.value = yearEnd;
};

const handleDateClickEnd = (e) => {
  const button = e.target;
  const selectedDay = parseInt(button.textContent);
  const candidateDate = new Date(yearEnd, monthEnd, selectedDay);
  
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  candidateDate.setHours(0, 0, 0, 0);

  if (candidateDate < today) {
    alert("Invalid date.");
    return;
  }

  const selected = dateEnd.querySelector('.selected');
  selected && selected.classList.remove('selected');
  button.classList.add('selected');
  selectdateEnd = candidateDate;
};

const displayDateEnd = () => {
  updateYearMonthEnd();
  dateEnd.innerHTML = "";
  
  const lastofPrevMonthEnd = new Date(yearEnd, monthEnd, 0);
  for (let i = 0; i <= lastofPrevMonthEnd.getDay(); i++) {
    const text = lastofPrevMonthEnd.getDate() - lastofPrevMonthEnd.getDay() + i;
    const button = createButtonEnd(text, true);
    dateEnd.appendChild(button);
  }

  const lastofMonthEnd = new Date(yearEnd, monthEnd + 1, 0);
  for (let i = 1; i <= lastofMonthEnd.getDate(); i++) {
    const button = createButtonEnd(i, false);
    button.addEventListener('click', handleDateClickEnd);
    dateEnd.appendChild(button);
  }

  const firstofNextMonthEnd = new Date(yearEnd, monthEnd + 1, 1);
  for (let i = firstofNextMonthEnd.getDay(); i < 7; i++) {
    const text = firstofNextMonthEnd.getDate() - firstofNextMonthEnd.getDay() + i;
    const button = createButtonEnd(text, true);
    dateEnd.appendChild(button);
  }
};

const createButtonEnd = (text, isDisabled = false) => {  
  const currentDate = new Date();
  const isToday =
    currentDate.getDate() === text &&
    currentDate.getFullYear() === yearEnd &&
    currentDate.getMonth() === monthEnd;
  
  const select =
    selectdateEnd.getDate() === text &&
    selectdateEnd.getFullYear() === yearEnd &&
    selectdateEnd.getMonth() === monthEnd;
  
  const button = document.createElement('button');
  button.textContent = text;
  button.disabled = isDisabled;
  button.classList.toggle('today', isToday);
  button.classList.toggle('select', select);
  return button;
};

displayDateEnd();

// Pop-ups for the datepickers and room clash resistant
dateinput.addEventListener('click', () => {
  datepick.hidden = false;
  datepickEnd.hidden = true;
});

dateinputEnd.addEventListener('click', () => {
  datepickEnd.hidden = false;
  datepick.hidden = true;
});

const roomSelect = document.querySelector('select[name="room-type"]');
roomSelect.addEventListener('focus', () => {
  datepick.hidden = true;
  datepickEnd.hidden = true;
});

// PER NIGHT CALCULATOR LOGIC
function calculatePrice() {
  const roomType = roomSelect.value;
  if (!dateinput.value || !dateinputEnd.value || !roomType || roomType === "Select Room") {
    return;
  }

  const startParts = dateinput.value.split('/');
  const endParts = dateinputEnd.value.split('/');
  const startDate = new Date(startParts[2], startParts[0] - 1, startParts[1]);
  const endDate = new Date(endParts[2], endParts[0] - 1, endParts[1]);

  let weekdayPrice = 0;
  let weekendPrice = 0;
  if (roomType === "Standard") {
    weekdayPrice = 100;
    weekendPrice = 140;
  } else if (roomType === "Deluxe") {
    weekdayPrice = 140;
    weekendPrice = 180;
  } else if (roomType === "Suite") {
    weekdayPrice = 180;
    weekendPrice = 220;
  }

  let totalPrice = 0;
  let nights = 0;
  for (let d = new Date(startDate); d < endDate; d.setDate(d.getDate() + 1)) {
    nights++;
    let day = d.getDay();
    if (day === 0 || day === 6) {
      totalPrice += weekendPrice;
    } else {
      totalPrice += weekdayPrice;
    }
  }
  document.getElementById('nights-display').textContent = "Nights: " + nights;
  document.getElementById('total-price').textContent = "Total Price: $" + totalPrice;
}

dateinput.addEventListener('change', calculatePrice);
dateinputEnd.addEventListener('change', calculatePrice);
roomSelect.addEventListener('change', calculatePrice);


/* ----- NEW: Allow manual typing of dates ----- */
// For the start date input:
dateinput.addEventListener('change', () => {
  const typedDate = new Date(dateinput.value);
  if (!isNaN(typedDate.getTime())) {
    selectdate = typedDate;
    year = typedDate.getFullYear();
    month = typedDate.getMonth();
    displayDate();
    calculatePrice();
  } else {
    alert("Invalid date typed. Please use a valid format (e.g. MM/DD/YYYY).");
  }
});

// For the end date input:
dateinputEnd.addEventListener('change', () => {
  const typedDateEnd = new Date(dateinputEnd.value);
  if (!isNaN(typedDateEnd.getTime())) {
    selectdateEnd = typedDateEnd;
    yearEnd = typedDateEnd.getFullYear();
    monthEnd = typedDateEnd.getMonth();
    displayDateEnd();
    calculatePrice();
  } else {
    alert("Invalid end date typed. Please use a valid format (e.g. MM/DD/YYYY).");
  }
});
