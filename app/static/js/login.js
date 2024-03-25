const form = document.getElementById('loginForm');
const errorElement = document.getElementById('error');

const emailKey = document.getElementById('emailKey');
const passwordKey = document.getElementById('passwordKey');


form.addEventListener('submit', (e) => {
    let messages = []
    //password field validation
    let email = emailKey.value.trim(); // Trim whitespace
    email = email.toLowerCase(); // Convert email to lowercase
    if (email === null || email === '') {
        messages.push('Email required');
    }


    //password confirmation field validation
    if(passwordKey.value === null || passwordKey.value === '' ) {
        messages.push('Password required');
    }


    //if any errors exist, will prevent form from submitting
    if (messages.length > 0) {
        e.preventDefault();
        errorElement.style.color = 'red';
        errorElement.style.fontWeight = 'bold';
        errorElement.innerText = messages.join('. ');
    }
    else {
        // If no errors, redirect the user
        window.location.href = "../Pages/home.html";
    }

}) 