
/* Not too sure how the javascript works with the python but the id's for all the html inputs are here, the employer ones are not shown on the html as the javascript is adding them in when you swap options 



STUDENT:
firstnameEntry
lastnameEntry
emailEntry
idEntry
passwordEntry
confirmEntry

EMPLOYER:
firstnameEntry
lastnameEntry
emailEntry
companyEntry
addressEntry
phonenumberEntry
passwordEntry
confirmEntry


*/



function switchInputs(){

    //check if the value in the selection box is equal to student
    if(document.getElementById("account_Type").value == "Student"){

        location.href = "../Pages/accountcreateStudent.html"

   //check if the value in the selection box is equal to employer
    }else if(document.getElementById("account_Type").value == "Employer"){

        location.href = "../Pages/accountcreateEmployer.html"
    }

}


document.getElementById("account_Type").addEventListener("change", switchInputs);






