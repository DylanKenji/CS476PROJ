const form = document.getElementById('submitForm');
const errorElement = document.getElementById('error');

const studentfirstName = document.getElementById('studentfirstName');
const studentlastName = document.getElementById('studentlastName');
const studentEmail = document.getElementById('studentEmail');
const studentPassword = document.getElementById('newPassword');
const studentconfirmPassword = document.getElementById('confirmPassword');
const studentMajor = document.getElementById('studentMajor');
const studentResume = document.getElementById('newResume');
const newstudentAvatar = document.getElementById('newstudentAvatar');



form.addEventListener('submit', (e) => {
    let messages = []
    //first name field validation
    if (studentfirstName.value === null || studentfirstName.value === '' ) {
        messages.push('First name required');
    }
    else if (!/^[A-Za-z-]+$/.test(studentfirstName.value)) {
        messages.push('First name cannot contain numbers');
    }

    //last name field validation
    if (studentlastName.value === null || studentlastName.value === '' ) {
        messages.push('Last name required');
    }
    else if (!/^[A-Za-z\s-]+$/.test(studentlastName.value)) {
        messages.push('Last name cannot contain numbers or special characters');
    }

    //email field validation
    if (studentEmail.value === null || studentEmail.value === '' ) {
        messages.push('Email required');
    }
    else if (!/\S+@\S+\.\S+/.test(studentEmail.value)) {
        messages.push('Invalid email format');
    }

    //password field validation
    if (studentPassword.value !== null && studentPassword.value !== '' ) {
       

        if (studentPassword.value.length < 8) {
            messages.push('Password must be at least 8 characters long');
        }
        if (studentPassword.value.length > 24) {
            messages.push('Password cannot be more than 24 characters long');
        }
        if (!/[A-Z]/.test(studentPassword.value)) {
            messages.push('Password must contain at least one capital letter');
        }
        if (!/[a-z]/.test(studentPassword.value)) {
            messages.push('Password must contain at least one lowercase letter');
        }
        if (!/\d/.test(studentPassword.value)) {
            messages.push('Password must contain at least one number');
        }
    }

    //password confirmation field validation
   if (studentconfirmPassword.value !== studentPassword.value) {
        messages.push('Passwords do not match');
    }

    //major field validation
    if (studentMajor.value === null || studentMajor.value === '' ) {
        messages.push('Major required');
    }

    //availability field validation
    //no validation is needed because it's possible that the student is NOT currently FOR HIRE

    
    //new avatar field validation
    if (newstudentAvatar.files.length > 0) {
        const file = newstudentAvatar.files[0];
        const fileType = file.type;
        const validFileTypes = ['image/png', 'image/jpg', 'image/jpeg', 'image/gif', ];
    
        if (!validFileTypes.includes(fileType)) {
            messages.push('Invalid file format. Please upload a PNG, JPG, JPEG, or GIF file for the avatar.');
        }
    }


    //if any errors exist, will prevent form from submitting
    if (messages.length > 0) {
        e.preventDefault();
        errorElement.style.color = 'red';
        errorElement.style.fontWeight = 'bold';
        errorElement.innerHTML = messages.join('<br>');
    }
}) 