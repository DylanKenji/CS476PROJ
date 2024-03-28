document.addEventListener('DOMContentLoaded', function () {
    const jobPostings = document.querySelectorAll('.jobPosting');

    //Store the last clicked variable for the jobId
    let lastClickedJobId; 

      //Hide the remove button if no job is selected
      function hideRemoveButton() {
        const removeButtonForm = document.querySelector('.removepostForm');
        removeButtonForm.style.display = 'none';
        }

    //Hide the remove button right away
    hideRemoveButton();

    jobPostings.forEach(function (jobPosting) {
        jobPosting.addEventListener('click', function () {
            const jobId = jobPosting.dataset.jobId;

            //Update the last clicked jobId
            lastClickedJobId = jobId; 

             //Show the remove posting button when a job is selected
             const removeButtonForm = document.querySelector('.removepostForm');
             removeButtonForm.style.display = 'block';

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
                    
                    
                    //Fetch applicants for job clicked
                    fetch(`/job/${jobId}/applicants`)
                    .then(response => response.json())
                    .then(applicants => {
                        //Query the applicant div
                        const jobApplicantsContainer = document.querySelector('.jobApplicants');
                
                        //Remove any previous applicants from the container
                        jobApplicantsContainer.innerHTML = '';
                
                        //Iterate through each applicant 
                        for (let i = applicants.length - 1; i >= 0; i--) {
                            const applicant = applicants[i];
                
                            //Create a div for each applicant
                            const applicantDiv = document.createElement('div');
                            applicantDiv.classList.add('applicant');
                
                            //Add the avatar of the applicant
                            const avatarImg = document.createElement('img');
                            avatarImg.src = "static/library/media/avatars/" + applicant.avatar;
                            avatarImg.classList.add("appImg");
                            avatarImg.alt = 'Applicant Avatar';
                            applicantDiv.appendChild(avatarImg);
                
                            //Add the applicants name 
                            const namePara = document.createElement('p');
                            namePara.textContent = applicant.first_name + " " +  applicant.last_name;
                            applicantDiv.appendChild(namePara);
                
                            //Adds form that links to the applicants resume
                            const form = document.createElement('form');
                            form.classList.add("resumeForm");
                            console.log(applicant.resume);
                            form.action = "static/library/media/resumes/" +  applicant.resume;
                            form.method = "get";
                            form.target = "_blank";
                            applicantDiv.appendChild(form);
                
                            //Adds a button that submits the resume form to bring the pdf to a new tab
                            const resumeButton = document.createElement("button");
                            resumeButton.classList.add("viewResume", "resumeButton");
                            resumeButton.onclick = function() {
                                form.submit();
                            };
                            resumeButton.type = "button";
                            resumeButton.textContent = "View Resume";
                            form.appendChild(resumeButton);
                
                            //Append the div to the applicant container
                            jobApplicantsContainer.appendChild(applicantDiv);
                        }
                    })
                    .catch(error => console.error('Error fetching applicants:', error));




                })
                .catch(error => console.error('Error fetching job details:', error));
            });
    });

    //Query the posting form
    const deleteButton = document.querySelector('.removepostForm');

    //Event listener for submiting the delete button
    deleteButton.addEventListener('submit', function (event) {
        //Prevents default form submission
        event.preventDefault(); 

        //Send a post request to delete the clicked job
        fetch('/delete_job', {
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
                alert('Job removed successfully!');
                window.location.href = '/profileEmployer';
            } else {
                //Alert if the job was unsuccessful
                alert('Failed to remove job. Please try again.');
            }
        })
        .catch(error => console.error('Error submitting application:', error));
    });


});

