window.onload = init;
window.onsubmit = onSubmit;

function init() {
	setControls();
}

function onSubmit(){
	var result = true;
	result = checkFirstName() && result;
	result = checkLastName() && result;
	result = checkHan() && result;
	result = checkEmail() && result;
	result = checkDate() && result;
	result = checkUname() && result;
	result = checkPassword() && result;
	return result;
}

//Reset default texts and hide error messages on resetting form
window.onreset = function(e){
	init();
	e.preventDefault();
};

function hideErrors(){
	var errorElem = document.getElementsByClassName('errorText');
	for (var i=0; i<errorElem.length; i++) {
		errorElem[i].style.display = 'none';
	}
}

//Set default texts and validation functions
function setControls() {
	//containing default texts and corresponding validation functions
	var setupArray = [
		 {
		 	defaultText: 'Enter your first name',
		    validate: checkFirstName 
		 },
		 {
		 	defaultText: 'Enter your last name',
			validate: checkLastName
		 },
		 {
		 	defaultText: 'Enter your email address',
			validate: checkEmail
		 },
		 {
			 defaultText: 'Enter a user name',
			 validate: checkUname
		 },
		 {
			 defaultText: 'Enter a password',
			 validate: checkPassword
		 }
	];
	
// Set required fields
	var requiredFields = document.getElementsByClassName('required');
	//Displaying default text in each field
	for (var i=0; i<requiredFields.length; i++) {
		requiredFields[i].value = setupArray[i].defaultText;
		requiredFields[i].style.color = '#a8a8a8';
		requiredFields[i].style.fontStyle = 'italic';
		
		// Assigning each object to the corresponding field 
		requiredFields[i].setupObject = setupArray[i];
		
		requiredFields[i].onfocus = function() {
			if (this.value === this.setupObject.defaultText) {
				this.value = '';
				this.style.color = '#000';
				this.style.fontStyle = 'normal';
			}
		} //end focus
		requiredFields[i].onblur = function() {
			if (this.value === '') {
				this.value = this.setupObject.defaultText;
				this.style.color = '#a8a8a8';
				this.style.fontStyle = 'italic';
			}
			this.setupObject.validate();
		} //end blur
	} //end for loop
	
// Set date field
	var dateField = document.getElementById('date');
	dateField.value = '';
	dateField.onblur = checkDate;
	
	hideErrors();
} //end setup

// Set focus on first field
function selectFocus () {
	var firstElem = document.getElementById('fname');
	firstElem.focus();
} //end focus

// Validation functions
function checkFirstName() {
	var fName = document.getElementById('fname');
	var errFName = document.getElementById('errFName');
	if (fName.value === '' || fName.value === 'Enter your first name') {
		errFName.innerHTML='Please enter your first name';
		errFName.style.display='block';
		return false;
	} else {
		errFName.style.display='none';
	}
	return true;
}

function checkLastName(){
	var lName = document.getElementById('lname');
	var errLName = document.getElementById('errLName');
	if (lName.value === '' || lName.value === 'Enter your last name') {
		errLName.innerHTML='Please enter your last name';
		errLName.style.display='block';
		return false;
	} else {
		errLName.style.display='none';
	}
	return true;
}

function checkEmail(){
	var email = document.getElementById('email');
	var emailRegex = /[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}/;
	var errEmail = document.getElementById('errEmail');
	if (email.value === '' || email.value === 'Enter your email address') {
		errEmail.innerHTML='Please enter your email address';
		errEmail.style.display='block';
		return false;
	} else if (!emailRegex.test(email.value)) {
		errEmail.innerHTML='Please enter a valid email address'
		errEmail.style.display='block';
		return false;
	} else {
		errEmail.style.display='none';
	}
	return true;
}

function checkDate(){
	var date = document.getElementById('date');
	var errDate = document.getElementById('errDate');
	if (date.value != '') {
		errDate.innerHTML='Please enter a valid date';
		errDate.style.display='block';
		return false;
	}
	else {
		errDate.style.display='none';
	}
	return true;
}

function checkUname(){
	var uname=document.getElementById("uname");
 	var errUname = document.getElementById("errUname");
 	var unameRegex = /[A-Za-z0-9].{6,}/;
	if (uname.value === '' || uname.value === 'Enter a user name') {
		errUname.innerHTML='Please enter a user name';
		errUname.style.display='block';
		return false;
	} else if (!unameRegex.test(uname.value)) {
		errUname.innerHTML='Please enter a valid user name'
		errUname.style.display='block';
		return false;
	} else {
		errUname.style.display='none';
	}
	return true;
}

function checkPassword(){
	var password=document.getElementById("password");
	var errPassword = document.getElementById("errPassword");
    var passwordRegex=/(?=[a-zA-Z0-9]).{6,}/;
    if (password.value === '' || password.value === 'Enter a password') {
		errPassword.innerHTML='Please enter a password';
		errPassword.style.display='block';
		return false;
	} else if (!passwordRegex.test(password.value)) {
		errPassword.innerHTML='Please enter a valid password'
		errPassword.style.display='block';
		return false;
	} else {
		errPassword.style.display='none';
	}
	return true;
}