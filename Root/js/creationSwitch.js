
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

    let mainForm = document.getElementById("infoForm");


    //check if the value in the selection box is equal to student
    if(document.getElementById("account_Type").value == "Student"){

        //remove previous inputs
        document.querySelectorAll('.space').forEach(e => e.remove());

        //creating html elements to append to form to switch from employer to student inputs

        //firstName
        let inputField = document.createElement("section");
        inputField.classList = "space";
        

        let label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "First Name:"
        inputField.append(label);

        let input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "First Name"
        input.id="firstnameEntry";

        inputField.append(input);

        mainForm.append(inputField)


        //lastName
        inputField = document.createElement("section");
        inputField.classList = "space";
       

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Last Name:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "Last Name"
        input.id="lastnameEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //email
        inputField = document.createElement("section");
        inputField.classList = "space";
      

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Email:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "email";
        input.placeholder = "Email"
        input.id="emailEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //ID
        inputField = document.createElement("section");
        inputField.classList = "space";
        

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Student ID:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "Student ID"
        input.id="idEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //Password
        inputField = document.createElement("section");
        inputField.classList = "space";
     

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Password:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "password";
        input.placeholder = "Password"
        input.id="passwordEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //Password confirm
        inputField = document.createElement("section");
        inputField.classList = "space";
       

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Confirm Password:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "password";
        input.placeholder = "Confirm Password"
        input.id="confirmEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //adding button
        inputField = document.createElement("section");
        inputField.classList = "space buttonHolder";
       

        button = document.createElement("button");
        button.classList = "createButton greenButton";
        button.type = "submit";
        button.value = "Create Account";
        button.id = "createAccount";
        button.textContent = "Create Account";
        inputField.append(button);
        

        mainForm.append(inputField)

   //check if the value in the selection box is equal to employer
    }else if(document.getElementById("account_Type").value == "Employer"){


        document.querySelectorAll('.space').forEach(e => e.remove());
        //creating html elements to append to form to switch from employer to student inputs
        
        //firstName
        let inputField = document.createElement("section");
        inputField.classList = "space";
     

        let label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "First Name:"
        inputField.append(label);

        let input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "First Name"
        input.id="firstnameEntry";

        inputField.append(input);

        mainForm.append(inputField)


        //lastName
        inputField = document.createElement("section");
        inputField.classList = "space";
      

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Last Name:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "Last Name"
        input.id="lastnameEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //email
        inputField = document.createElement("section");
        inputField.classList = "space";
       

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Email:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "email";
        input.placeholder = "Email"
        input.id="emailEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //Company name
        inputField = document.createElement("section");
        inputField.classList = "space";
     

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Company Name:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "Company Name"
        input.id="companyEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //Company address
        inputField = document.createElement("section");
        inputField.classList = "space";
     

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Company Address:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "Company Address"
        input.id="addressEntry";

        inputField.append(input);

        mainForm.append(inputField)
        
        //Company phonenumber
        inputField = document.createElement("section");
        inputField.classList = "space";
       

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Company Phone Number:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "text";
        input.placeholder = "Company Phone Number"
        input.id="phonenumberEntry";

        inputField.append(input);

        mainForm.append(inputField)   
        
        //Password
        inputField = document.createElement("section");
        inputField.classList = "space";
   

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Password:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "password";
        input.placeholder = "Password"
        input.id="passwordEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //Password confirm
        inputField = document.createElement("section");
        inputField.classList = "space";
     

        label = document.createElement("label");
        label.classList = "inputLabel float-left"
        label.textContent = "Confirm Password:"
        inputField.append(label);

        input = document.createElement("input");
        input.classList = "inputBox";
        input.type = "password";
        input.placeholder = "Confirm Password"
        input.id="confirmEntry";

        inputField.append(input);

        mainForm.append(inputField)

        //adding button
        inputField = document.createElement("section");
        inputField.classList = "space buttonHolder";
        

        button = document.createElement("button");
        button.classList = "createButton greenButton";
        button.type = "submit";
        button.value = "Create Account";
        button.id = "createAccount";
        button.textContent = "Create Account";
        inputField.append(button);
         
 
         mainForm.append(inputField)


    }

}


document.getElementById("account_Type").addEventListener("change", switchInputs);






