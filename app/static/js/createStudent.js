const form = document.getElementById('infoForm');
const errorElement = document.getElementById('error');

const firstnameEntry = document.getElementById('firstnameEntry');
const lastnameEntry = document.getElementById('lastnameEntry');
const emailEntry = document.getElementById('emailEntry');
const idEntry = document.getElementById('idEntry');
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
    if (lastnameEntry.value === null || lastnameEntry.value === '') 
    {
        messages.push('Last name required');
    } 
    else if (!/^[A-Za-z\s-]+$/.test(lastnameEntry.value)) 
    {
        messages.push('Last name cannot contain numbers or special characters');
    }

    //email field validation
    if (emailEntry.value === null || emailEntry.value === '' ) {
        messages.push('Email required');
    }
    else if (!/\S+@\S+\.\S+/.test(emailEntry.value)) {
        messages.push('Invalid email format');
    }

    //student ID field validation
    if (idEntry.value === null || idEntry.value === '') {
        messages.push('SID required');
    } 
    else if (!/^200\d{6}$/.test(idEntry.value)) {
        messages.push('SID can only be 9 digits and start with 200');
    }

    //password field validation
    if(passwordEntry.value === null || passwordEntry.value === '' ) {
        messages.push('Password required');
    }
    if(passwordEntry.value.length < 5) {
        messages.push('Password must be longer than 5 characters');
    }
    if(passwordEntry.value.length > 20) {
        messages.push('Password cannot be more than 20 characters');
    }

    //password confirmation field validation
    if(confirmEntry.value === null || confirmEntry.value === '' ) {
        messages.push('Password confirmation required');
    }
    else if (confirmEntry.value !== passwordEntry.value) {
        messages.push('Passwords do not match');
    }


    
    // If any errors exist, prevent form submission
    if (messages.length > 0) {
        e.preventDefault();
        errorElement.style.color = 'red';
        errorElement.style.fontWeight = 'bold';
        errorElement.innerHTML = messages.join('<br>');
    }
    else {
        // If no errors, redirect the user
        window.location.href = "../Pages/home.html";
    }
}) 