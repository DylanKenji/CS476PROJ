
document.addEventListener('DOMContentLoaded', function () {
    const jobPostings = document.querySelectorAll('.jobPosting');

    //Store the last clicked variable for the jobId
    let lastClickedJobId;

    jobPostings.forEach(function (jobPosting) {
        jobPosting.addEventListener('click', function () {
            const jobId = jobPosting.dataset.jobId;

            //Update the last clicked jobId
            lastClickedJobId = jobId;

             //Find the jobId based on job clicked
            fetch(`/job/${jobId}`)
                .then(response => response.json())
                .then(data => {

                    //Update all of the html job description elements with the job based on the fetched jobId
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

                })
                .catch(error => console.error('Error fetching job details:', error));
        });
    });


    // Event listener for applying to the last clicked job
    const applyButton = document.querySelector('.applyForm');

    //Event listener for submiting the apply button
    applyButton.addEventListener('submit', function (event) {

        //Prevents default form submission
        event.preventDefault();

      //Send a post request to delete the clicked job
        fetch('/apply_for_job', {
            method: 'POST',
            body: JSON.stringify({ job_id: lastClickedJobId }), 
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
              //If the database returns a correct response
            if (response.ok) {
                //Move the window href to the employer profile page
                alert('Application submitted successfully!');
                window.location.href = '/profileStudent';
            } else {
                //Alert if the job was unsuccessful
                alert('Failed to submit application. Please try again.');
            }
        })
        .catch(error => console.error('Error submitting application:', error));
    });
});

document.addEventListener("DOMContentLoaded", function() {
    //Query the job postings
    const jobPostings = document.querySelectorAll(".jobPosting");

    //Toggle visibility of apply button
    function toggleApplyButtonVisibility() {
        const applyButton = document.querySelector(".applyButton");
        if (applyButton) {
            //If a job posting is selected show the job button
            applyButton.style.display = document.querySelector(".jobPosting.selected") ? "block" : "none";
        }
    }

    //Add event listener to see when a job is clicked
    jobPostings.forEach(function(jobPosting) {
        jobPosting.addEventListener("click", function() {
            //Remove class from all other jobs
            jobPostings.forEach(function(posting) {
                posting.classList.remove("selected");
            });
            //Add class to current job
            jobPosting.classList.add("selected");

            //Toggle the apply button visibility
            toggleApplyButtonVisibility();
        });
    });

    //Toggle the apply button visibility
    toggleApplyButtonVisibility();
});