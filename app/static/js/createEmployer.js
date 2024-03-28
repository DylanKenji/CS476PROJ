const form = document.getElementById('infoForm');
const errorElement = document.getElementById('error');

const firstnameEntry = document.getElementById('firstnameEntry');
const lastnameEntry = document.getElementById('lastnameEntry');
const emailEntry = document.getElementById('emailEntry');
const companyEntry = document.getElementById('companyEntry');
const addressEntry = document.getElementById('addressEntry');
const phoneEntry = document.getElementById('phoneEntry');
const passwordEntry = document.getElementById('passwordEntry');
const confirmEntry = document.getElementById('confirmEntry');

form.addEventListener('submit', (e) => {
    let messages = []
    //first name field validation
    if (firstnameEntry.value === null || firstnameEntry.value === '') {
        messages.push('First name required');
    } 
    else if (!/^[A-Za-z-]+$/.test(firstnameEntry.value)) {
        messages.push('First name cannot contain numbers or special characters (Exception: Hypens)');
    }
    
    //last name field validation
    if (lastnameEntry.value === null || lastnameEntry.value === '' ) {
        messages.push('Last name required');
    }
    else if (!/^[A-Za-z- ]+$/.test(lastnameEntry.value)) {
        messages.push('Last name cannot contain numbers or special characters');
    }

    //email field validation
    if (emailEntry.value === null || emailEntry.value === '' ) {
        messages.push('Email required');
    }
    else if (!/\S+@\S+\.\S+/.test(emailEntry.value)) {
        messages.push('Invalid email format');
    }

    //company name field validation
    if (companyEntry.value === null || companyEntry.value === '' ) {
        messages.push('Company name required');
    }

    //company address field validation
    if (addressEntry.value === null || addressEntry.value === '' ) {
        messages.push('Company address required');
    } 
    else if (addressEntry.value.length < 5) {
        messages.push('Address must be at least 5 characters');
    }

    //company phone number validation
    if (phoneEntry.value === null || phoneEntry.value === '' ) {
        messages.push('Phone number required');
    } 
    else if (!/^\d{10}$/.test(phoneEntry.value)) {
        messages.push('Invalid phone number format. It should be a 10-digit number.');
    }

    //password field validation
    if (passwordEntry.value === null || passwordEntry.value === '' ) {
        messages.push('Password required');
    } 
    else {
        if (passwordEntry.value.length < 8) {
            messages.push('Password must be at least 8 characters long');
        }
        if (passwordEntry.value.length > 24) {
            messages.push('Password cannot be more than 24 characters long');
        }
        if (!/[A-Z]/.test(passwordEntry.value)) {
            messages.push('Password must contain at least one capital letter');
        }
        if (!/[a-z]/.test(passwordEntry.value)) {
            messages.push('Password must contain at least one lowercase letter');
        }
        if (!/\d/.test(passwordEntry.value)) {
            messages.push('Password must contain at least one number');
        }
    }
    

    //password confirmation field validation
    if(confirmEntry.value === null || confirmEntry.value === '' ) {
        messages.push('Password confirmation required');
    }
    else if (confirmEntry.value !== passwordEntry.value) {
        messages.push('Passwords do not match');
    }



    //if any errors exist, will prevent form from submitting
    if (messages.length > 0) {
        e.preventDefault();
        errorElement.style.color = 'red';
        errorElement.style.fontWeight = 'bold';
        errorElement.innerHTML = messages.join('<br>');
    }
    else {
        //if no errors, redirect the user
        window.location.href = "../Pages/home.html";
    }

}) 