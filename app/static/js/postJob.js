const form = document.getElementById('jobForm');
const errorElement = document.getElementById('error');

const jobtitleEntry = document.getElementById('jobtitleEntry');
const jobdescEntry = document.getElementById('jobdescEntry');
const jobaddressEntry = document.getElementById('jobaddressEntry');
const major = document.getElementById('major');
const jobType = document.getElementById('jobType');
const wage = document.getElementById('wage');


form.addEventListener('submit', (e) => {
    let messages = []
    //job title validation
    if (jobtitleEntry.value === null || jobtitleEntry.value === '' ) {
        messages.push('Job title required');
    }
    else if (jobtitleEntry.value.length < 5) {
        messages.push('Job title must be at least 5 characters');
    }

    //job description validation
    if (jobdescEntry.value === null || jobdescEntry.value === '' ) {
        messages.push('Job description required');
    }
    else if (jobdescEntry.value.length < 50) {
        messages.push('Job description must be at least 50 characters');
    }

    //job address validation
    if (jobaddressEntry.value === null || jobaddressEntry.value === '' ) {
        messages.push('Job address required');
    }
    else if (jobaddressEntry.value.length < 5) {
        messages.push('Address must be at least 5 characters');
    }

    //job deadline validation
    if (jobdeadlineEntry.value === null || jobdeadlineEntry.value === '' ) {
        messages.push('Job deadline required');
    }


    if (major.value === null || major.value === '' ) {
        messages.push('Major required');
    }

    if (jobType.value === null || jobType.value === '' ) {
        messages.push('Job type required');
    }

    if (wage.value === null || wage.value === '' ) {
        messages.push('Wage required');
    }


    //if any errors exist, will prevent form from submitting
    if (messages.length > 0) {
        e.preventDefault();
        errorElement.style.color = 'red';
        errorElement.style.fontWeight = 'bold';
        errorElement.innerHTML = messages.join('<br>');
    }
}) 