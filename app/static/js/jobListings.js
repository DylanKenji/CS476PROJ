document.addEventListener('DOMContentLoaded', function () {
    const jobPostings = document.querySelectorAll('.jobPosting');

    jobPostings.forEach(function (jobPosting) {
        jobPosting.addEventListener('click', function () {
            const jobId = jobPosting.dataset.jobId;
            fetch(`/job/${jobId}`)
                .then(response => response.json())
                .then(data => {
                    // Update jobInfo section with fetched job details
                    const jobInfo = document.querySelector('.jobInfo');
                    jobInfo.querySelector('.mainImg').src = "static/library/media/avatars/" + data.avatar;
                    jobInfo.querySelector('.mainName').innerHTML = "<strong>Job Title:</strong> " + data.job_title;
                    jobInfo.querySelector('.mainCompany').innerHTML = "<strong>Company Name:</strong> " + data.company_name;
                    jobInfo.querySelector('.jobLocation').innerHTML = "<strong>Job Location:</strong> " + data.job_location;
                    jobInfo.querySelector('.datePosted').innerHTML = "<strong>Date Posted:</strong> " + data.date_created;
                    jobInfo.querySelector('.jobDesc').innerHTML = "<strong>Job Description:</strong> " + data.job_description;
                    jobInfo.querySelector('.jobMajor').innerHTML = "<strong>Major Required:</strong> " + data.major_required;
                    jobInfo.querySelector('.jobHours').innerHTML = "<strong>Hours:</strong> " + data.hours;
                    jobInfo.querySelector('.jobPay').innerHTML = "<strong>Pay:</strong> " + data.pay;


                    // Update other job details as needed

                    // Add event listener for Apply button
                    const applyButton = jobInfo.querySelector('.applyForm');
                    applyButton.addEventListener('submit', function(event) {
                        event.preventDefault(); // Prevent default form submission

                        // Send POST request to apply for the job
                        fetch('/apply_for_job', {
                            method: 'POST',
                            body: JSON.stringify({ job_id: jobId }), // Send job ID in request body
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        })
                        .then(response => {
                            if (response.ok) {
                                // Handle success response (e.g., show success message)
                                alert('Application submitted successfully!');
                            } else {
                                // Handle error response
                                alert('Failed to submit application. Please try again.');
                            }
                        })
                        .catch(error => console.error('Error submitting application:', error));
                    });
                })
                .catch(error => console.error('Error fetching job details:', error));
        });
    });
});