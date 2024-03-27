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
                    jobInfo.querySelector('.mainName').textContent = "Job Title: " + data.job_title;
                    jobInfo.querySelector('.mainCompany').textContent = "Company Name: " + data.company_name;
                    jobInfo.querySelector('.jobLocation').textContent = "Job Location: " + data.job_location;
                    jobInfo.querySelector('.datePosted').textContent = "Date Posted: " + data.date_created;
                    jobInfo.querySelector('.jobDesc').textContent = "Job Description: " + data.job_description;
                    jobInfo.querySelector('.jobMajor').textContent = "Major Required: " + data.major_required;
                    jobInfo.querySelector('.jobHours').textContent = "Hours: " + data.hours;
                    jobInfo.querySelector('.jobPay').textContent = "Pay: " + data.pay;


                        // Fetch applicants for the selected job
                        fetch(`/job/${jobId}/applicants`)
                            .then(response => response.json())
                            .then(applicants => {
                                const jobApplicantsContainer = document.querySelector('.jobApplicants');

                                // Clear previous applicant divs if any
                                jobApplicantsContainer.innerHTML = '';

                                // Iterate through each applicant and create divs
                                applicants.forEach(applicant => {
                                    const applicantDiv = document.createElement('div');
                                    applicantDiv.classList.add('applicant');

                                    const avatarImg = document.createElement('img');
                                    avatarImg.src = "static/library/media/avatars/" + applicant.avatar;
                                    avatarImg.classList.add("appImg");
                                    avatarImg.alt = 'Applicant Avatar';
                                    applicantDiv.appendChild(avatarImg);

                                    const namePara = document.createElement('p');
                                    namePara.textContent = applicant.first_name + " " +  applicant.last_name;
                                    applicantDiv.appendChild(namePara);

                                    const form = document.createElement('form');
                                    form.classList.add("resumeForm");
                                    console.log(applicant.resume);
                                    form.action = "static/library/media/resumes/" +  applicant.resume;
                                    form.method = "get";
                                    form.target = "_blank";
                                    applicantDiv.appendChild(form);

                                    const resumeButton = document.createElement("button");
                                    resumeButton.classList.add("greenButton", "resumeButton");
                                    resumeButton.type = "submit";
                                    resumeButton.textContent = "View Resume";
                                    form.appendChild(resumeButton);

                                    // Append the applicant div to the container
                                    jobApplicantsContainer.appendChild(applicantDiv);
                                });
                            })
                    .catch(error => console.error('Error fetching applicants:', error));
                })
                .catch(error => console.error('Error fetching job details:', error));
        });
    });
});