function switchInputs(){

    //check if the value in the selection box is equal to student
    if(document.getElementById("account_Type").value == "Student"){

        location.href = "../Pages/createStudent.html"

   //check if the value in the selection box is equal to employer
    }else if(document.getElementById("account_Type").value == "Employer"){

        location.href = "../Pages/createEmployer.html"
    }

}

document.getElementById("account_Type").addEventListener("change", switchInputs);






