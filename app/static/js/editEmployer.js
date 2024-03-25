const form = document.getElementById('submitForm');
const errorElement = document.getElementById('error');

const employerfirstName = document.getElementById('employerfirstName');
const employerlastName = document.getElementById('employerlastName');
const employerEmail = document.getElementById('employerEmail');
const companyName = document.getElementById('companyName');
const companyAddress = document.getElementById('companyAddress');
const companyNumber = document.getElementById('companyNumber');
const employerPassword = document.getElementById('employerPassword');
const employerconfirmPassword = document.getElementById('employerconfirmPassword');
const newemployerAvatar = document.getElementById('newemployerAvatar');

form.addEventListener('submit', (e) => {
    let messages = []
    //first name field validation
    if (employerfirstName.value === null || employerfirstName.value === '' ) {
        messages.push('First name required');
    }
    else if (!/^[A-Za-z-]+$/.test(employerfirstName.value)) {
        messages.push('First name cannot contain numbers');
    }

    //last name field validation
    if (employerlastName.value === null || employerlastName.value === '' ) {
        messages.push('Last name required');
    }
    else if (!/^[A-Za-z-]+$/.test(employerlastName.value)) {
        messages.push('Last name cannot contain numbers');
    }

    //email field validation
    if (employerEmail.value === null || employerEmail.value === '' ) {
        messages.push('Email required');
    }
    else if (!/\S+@\S+\.\S+/.test(employerEmail.value)) {
        messages.push('Invalid email format');
    }

    //company name field validation
    if (companyName.value === null || companyName.value === '' ) {
        messages.push('Company name required');
    }

    //company address field validation
    if (companyAddress.value === null || companyAddress.value === '' ) {
        messages.push('Company address required');
    } 
    else if (companyAddress.value.length < 5) {
        messages.push('Address must be at least 5 characters');
    }

    //company phone number validation
    if (companyNumber.value === null || companyNumber.value === '' ) {
        messages.push('Phone number required');
    } 
    else if (!/^\d{10}$/.test(companyNumber.value)) {
        messages.push('Invalid phone number format. It should be a 10-digit number.');
    }

    //password field validation
        //password field validation
        if(employerPassword.value.length > 0) {
            if(employerPassword.value.length < 5) {
                messages.push('Password must be longer than 5 characters');
            }
        }
        if(employerPassword.value.length > 20) {
            messages.push('Password cannot be more than 20 characters');
        }

    //password confirmation field validation
    if (studentconfirmPassword.value !== studentPassword.value) {
        messages.push('Passwords do not match');
    }

    //new avatar field validation
    if (newemployerAvatar.files.length > 0) {
        const file = newemployerAvatar.files[0];
        const fileType = file.type;
        const validFileTypes = ['image/jpeg', 'image/png', 'image/gif'];
    
        if (!validFileTypes.includes(fileType)) {
            messages.push('Invalid file format. Please upload a JPEG, PNG, or GIF file for the avatar.');
        }
    }



    //if any errors exist, will prevent form from submitting
    if (messages.length > 0) {
        e.preventDefault();
        errorElement.style.color = 'red';
        errorElement.style.fontWeight = 'bold';
        errorElement.innerText = messages.join('. ');
    }
}) 