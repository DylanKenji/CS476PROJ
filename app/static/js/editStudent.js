const form = document.getElementById('submitForm');
const errorElement = document.getElementById('error');

const studentfirstName = document.getElementById('studentfirstName');
const studentlastName = document.getElementById('studentlastName');
const studentEmail = document.getElementById('studentEmail');
const studentPassword = document.getElementById('studentPassword');
const studentconfirmPassword = document.getElementById('studentconfirmPassword');
const studentMajor = document.getElementById('studentMajor');
const studentResume = document.getElementById('studentResume');
const newstudentAvatar = document.getElementById('newstudentAvatar');


form.addEventListener('submit', (e) => {
    let messages = []
    //first name field validation
    if (studentfirstName.value === null || studentfirstName.value === '' ) {
        messages.push('First name required');
    }
    else if (!/^[A-Za-z]+$/.test(studentfirstName.value)) {
        messages.push('First name cannot contain numbers');
    }

    //last name field validation
    if (studentlastName.value === null || studentlastName.value === '' ) {
        messages.push('Last name required');
    }
    else if (!/^[A-Za-z]+$/.test(studentlastName.value)) {
        messages.push('Last name cannot contain numbers');
    }

    //email field validation
    if (studentEmail.value === null || studentEmail.value === '' ) {
        messages.push('Email required');
    }
    else if (!/\S+@\S+\.\S+/.test(studentEmail.value)) {
        messages.push('Invalid email format');
    }

    //password field validation
    if(studentPassword.value.length > 0) {
        if(studentPassword.value.length < 5) {
            messages.push('Password must be longer than 5 characters');
        }
    }
    if(studentPassword.value.length > 20) {
        messages.push('Password cannot be more than 20 characters');
    }

    //password confirmation field validation
   if (studentconfirmPassword.value !== studentPassword.value) {
        messages.push('Passwords do not match');
    }

    //major field validation
    //need to look into this further. Want to create a dropdown menu and the options should be fetching the available majors
    //from the database
    if (studentMajor.value === null || studentMajor.value === '' ) {
        messages.push('Major required');
    }

    //availability field validation
    //no validation is needed because it's possible that the student is NOT currently FOR HIRE

    //resume field validation
    if (studentResume.files.length === 0) {
        messages.push('Student resume (PDF) required');
    } else {
        const file = studentResume.files[0];
        const fileType = file.type;

        if (fileType !== 'application/pdf') {
            messages.push('Invalid file format. Please upload a PDF file for the resume.');
        }
    }

    //new avatar field validation
    if (newstudentAvatar.files.length > 0) {
        const file = newstudentAvatar.files[0];
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