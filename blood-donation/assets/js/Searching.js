// List of cities in Pakistan (you can expand this list)
const cities = [
    "Lahore", "Karachi", "Islamabad", "Faisalabad", "Rawalpindi", 
    "Multan", "Gujranwala", "Peshawar", "Quetta", "Sialkot", 
    // Add more cities here...
];

const cityInput = document.getElementById("cityInput");
const citySelect = document.getElementById("citySelect");

// Function to update the dropdown options based on user input
function updateOptions() {
    const userInput = cityInput.value.toLowerCase();
    const matchingCities = cities.filter(city => city.toLowerCase().startsWith(userInput));
    
    // Clear the previous options
    citySelect.innerHTML = "";

    // Display matching city options
    matchingCities.forEach(city => {
        const option = document.createElement("option");
        option.value = city;
        citySelect.appendChild(option);
    });
}

// Add event listener to update options on input change
cityInput.addEventListener("input", updateOptions);
