
document.addEventListener('DOMContentLoaded', function () {
    const jobPostings = document.querySelectorAll('.jobPosting');
    let lastClickedJobId; // Variable to store the ID of the last clicked job

    jobPostings.forEach(function (jobPosting) {
        jobPosting.addEventListener('click', function () {
            const jobId = jobPosting.dataset.jobId;
            lastClickedJobId = jobId; // Update the last clicked job ID

            fetch(`/job/${jobId}`)
                .then(response => response.json())
                .then(data => {
                    // Update jobInfo section with fetched job details
                    const jobInfo = document.querySelector('.jobInfo');
                    jobInfo.querySelector('.mainImg').src = "static/library/media/avatars/" + data.avatar;
                    jobInfo.querySelector('.mainName').innerHTML = "<strong>Job Title:</strong> <u>" + data.job_title + "</u>";
                    jobInfo.querySelector('.mainCompany').innerHTML = "<strong>Company Name:</strong> " + data.company_name;
                    jobInfo.querySelector('.jobLocation').innerHTML = "<strong>Job Location:</strong> " + data.job_location;
                    jobInfo.querySelector('.datePosted').innerHTML = "<strong>Date Posted:</strong> " + data.date_created;
                    jobInfo.querySelector('.jobDesc').innerHTML = "<strong>Job Description:</strong> " + data.job_description;
                    jobInfo.querySelector('.jobMajor').innerHTML = "<strong>Major Required:</strong> " + data.major_required;
                    jobInfo.querySelector('.jobHours').innerHTML = "<strong>Job Type:</strong> " + data.hours;
                    jobInfo.querySelector('.jobPay').innerHTML = "<strong>Hourly Wage: $</strong> " + data.pay;

                    // Update other job details as needed
                })
                .catch(error => console.error('Error fetching job details:', error));
        });
    });

    // Event listener for applying to the last clicked job
    const applyButton = document.querySelector('.applyForm');
    applyButton.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        // Send POST request to apply for the last clicked job
        fetch('/apply_for_job', {
            method: 'POST',
            body: JSON.stringify({ job_id: lastClickedJobId }), // Send last clicked job ID in request body
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // Handle success response (e.g., show success message)
                alert('Application submitted successfully!');
                window.location.href = '/profileStudent';
            } else {
                // Handle error response
                alert('Failed to submit application. Please try again.');
            }
        })
        .catch(error => console.error('Error submitting application:', error));
    });
});