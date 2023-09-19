console.log("creating")
document.getElementById("submit-btn").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Extract values from the form fields
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const phone_number = document.getElementById("phone_number").value;
    const blood_type = document.getElementById("blood_type").value;
    const last_donation_date = document.getElementById("last_donation_date").value;
    const address = document.getElementById("address").value;
    const city = document.getElementById("city").value;
    // Extract other form field values here


    // Create an object with the extracted data
    const formData = {
        name: name,
        email: email,
        phone_number: phone_number,
        blood_type: blood_type,
        last_donation_date: last_donation_date,
        is_active: true,
        address: address,
        city: city,
    };

    // Convert the data to a JSON string
    const jsonData = JSON.stringify(formData);

    // Send a POST request to the endpoint
    fetch("http://127.0.0.1:8000/donor/create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: jsonData,
    })
    .then((response) => response.json())
    .then((data) => {
        console.log("Data sent successfully:", data);
        document.getElementById("name").value ='';
        document.getElementById("email").value = '';
        document.getElementById("phone_number").value ='';
        document.getElementById("blood_type").value ='';
        document.getElementById("last_donation_date").value ='';
        document.getElementById("address").value ='';
        document.getElementById("city").value ='';

        // Create and show the thank you alert
        const alert = document.getElementById('alert'); 
        alert.classList.remove('d-none')
        

        // Remove the alert after 5 seconds
        setTimeout(() => {
            alert.classList.add('d-none')
        }, 5000);

    })
    .catch((error) => {
        console.error("Error:", error);
    });
   
});