const results = document.querySelector('#results');
const cityInput = document.querySelector('#city');
const bloodTypeInput = document.querySelector('#bloodType');

cityInput.addEventListener('input', fetchData);
bloodTypeInput.addEventListener('input', fetchData);
var Donors = [];


async function fetchData() {
  try {
    const response = await fetch(`http://127.0.0.1:8000/donor/all?blood_type=${bloodTypeInput.value}&city=${cityInput.value}`);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    Donors = data.results;
    // Call a function to process or display the Donors data
    processDonors();
    console.log('fetching data')
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
}

function processDonors() {
  // Now you can work with the JSON data
  results.innerHTML = ''
  Donors.map((Donor)=>{
   results.innerHTML += `
   <div class="card py-3  px-4 mt-2" key=${Donor.id}>
          <div
            class="user-info row" 
          >
            <div class="d-flex gap-1 justify-content-start align-items-center col-12 col-md-8">
              <span class="h3 mb-0 pr-2">${Donor.name}</span>
              <span>${Donor.city}, Pk</span>
            </div>
            <div class="col-12 col-md-4 d-flex justify-content-md-end">
              <h2 class="text-danger">${Donor.blood_type}</h2>
            </div>
          </div>
          <div class="contact-info d-flex justify-content-between  row">
            <span class="col-12 col-md-6 text-start d-flex">Phone: <span>${Donor.phone_number}</span>
            </span>
            <span class="col-12 col-md-6 d-flex justify-content-md-end">Address: <span>${Donor.address}</span>
            </span>
           
          </div>
          <div class="date-info row ">
            <div class="col-12 col-md-6 d-flex">
              <span>Last Donation Date: <span> ${Donor.last_donation_date}</span>  </span>
            </div>
            <div class="col-12 col-md-6 d-flex justify-content-md-end">
              <span>Active: <span>${Donor.is_active? `<span class="text-success">Available<span>`:`<span class="text-danger">Not Available<span>`}</span>  </span>
            </div>
          </div>
        </div>
`

  })
}


// Call the async function to fetch and process the data
fetchData();
