const monthSelect = document.getElementById('month');
const daySelect = document.getElementById('day');
const searchButton = document.getElementById('search');

// Function to populate days based on selected month
function populateDays(month) {
  const daysInMonth = new Date(2024, month, 0).getDate(); // Using 2000 as a placeholder year
  daySelect.innerHTML = ''; // Clear previous options
  for (let i = 1; i <= daysInMonth; i++) {
    const option = document.createElement('option');
    option.value = i;
    option.text = i;
    daySelect.appendChild(option);
  }
}

// Event listener for month change
monthSelect.addEventListener('change', () => {
  const selectedMonth = monthSelect.value;
  populateDays(selectedMonth);
  document.getElementById('search').setAttribute( "onClick", "window.open('/date/" + monthSelect.value.padStart(2, "0") + "/" + daySelect.value.padStart(2, "0") + "', '_self')" );
});

// Event listener for day change
daySelect.addEventListener('change', () => {
  const selectedDay = daySelect.value;
  document.getElementById('search').setAttribute( "onClick", "window.open('/date/" + monthSelect.value.padStart(2, "0") + "/" + daySelect.value.padStart(2, "0") + "', '_self')" );
});

// Initial population of days
populateDays(1); // Default to January