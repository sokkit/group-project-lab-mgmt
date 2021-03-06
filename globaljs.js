console.log("JS Connected!")

function updateUserRole(){
  alert("Function called");
  var username = document.forms["changeRole"]["chosenUser"].value;
  alert(username);
  if (username == ""){
    valid = 1;
    alert("Please enter a username");
    return null; //exits function
  }
  var checkBox = document.getElementById("Admin");
  var role = "";
  if (checkBox.checked == true){
    role = "Admin";
    alert("User is now admin");
  } else {
    role = "Staff";
    alert("User is now staff");
  }
}

function updateUserPassword(){
  var username = document.forms["changePassword"]["selectedUser"].value;
  var password = document.forms["changePassword"]["newPassword2"].value;
  var checkBox = document.getElementById("confirmation");
  var valid = 0;
  alert("taken in variables");
  if (checkBox.checked == false){
    alert("Please confirm changes before submitting");
    return null;
  }
  if (username == ""){
    valid = 1;
    alert("Please enter a username");
  }
  if (password == ""){
    valid = 1;
    alert("Please enter a password");
  }
  if (valid == 0){
    params = 'username='+username+'&password='+password;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", '/Users/UpdatePassword', true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onload = function() {
      if (xhttp.readyState === 4 && xhttp.status === 200) {
        console.log(xhttp.responseText);
        document.getElementById("txt").innerHTML = xhttp.responseText;
      } else {
        console.error(xhttp.statusText);
      }
    }
    xhttp.send(params);
    return false;
  } else {
    alert("One or more fields were incorrectly entered");
  }
}

function validateNewUser(){
  var firstname = document.forms["createNewUser"]["newFirstname"].value; //taking values from form
  var surname = document.forms["createNewUser"]["newSurname"].value;
  var public = "No"; //we are not gonna bother with public field, it will be no by default
  var username = document.forms["createNewUser"]["newUsername"].value;
  var password = document.forms["createNewUser"]["newPassword"].value;
  var checkBox = document.getElementById("Admin");//this gets the 'RoleGiven' checkbox from create new user box
  var role = "";
  if (checkBox.checked == true){ //converts the true/false format into "Admin" and "Staff"
    role = "Admin";
  } else {
    role = "Staff";
  }
  var valid = 0; // 0 means its valid, 1 means its invalid
  if (firstname == ""){ //presence checking
    valid = 1;
    alert("Please enter a firstname");
  }
  if (surname == ""){
    valid = 1;
    alert("Please enter a surname");
  }
  if (username == ""){
    valid = 1;
    alert("Please enter a username");
  }
  if (newPasswordVar == ""){
    alert("Please enter a password");
      valid = 1;
  }
  if (valid == 0){ //if all boxes are valid xhttp request is made
    params = 'firstname='+firstname+'&surname='+surname+'&public='+public+'&username='+username+'&password'+password+'&role'+role;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", '/Customer/AddCustomer', true); // true is asynchronous
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.onload = function() {
      if (xhttp.readyState === 4 && xhttp.status === 200) {
        console.log(xhttp.responseText);
        document.getElementById("txt").innerHTML = xhttp.responseText;
      } else {
        console.error(xhttp.statusText);
      }
    };
    //sends params to server
    xhttp.send(params);
    return false;
  } else { //doesn't do xhttp request due to invalid data
    alert("Data was not sent to server due to not being valid")
  }
}

function addCustomer() {
  // collects data from form and turn them into params
  var customerName = document.forms["addCustomer"]["customerName"].value;
  var address = document.forms["addCustomer"]["address"].value;
  var deliveryAddress = document.forms["addCustomer"]["deliveryAddress"].value;
  params = 'customerName='+customerName+'&address='+address+'&deliveryAddress='+deliveryAddress;
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", '/Customer/AddCustomer', true); // true is asynchronous
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.onload = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      console.log(xhttp.responseText);
      document.getElementById("txt").innerHTML = xhttp.responseText;
    } else {
      console.error(xhttp.statusText);
    }
  };
  //sends params to server
  xhttp.send(params);
  return false;
}


function delCustomer() {
  var name = document.forms["delCustomer"]["name"].value;
  params = 'name='+name;
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", '/Customer/DelCustomer', true); // true is asynchronous
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.onload = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      console.log(xhttp.responseText);
      document.getElementById("txt").innerHTML = xhttp.responseText;
    } else {
      console.error(xhttp.statusText);
    }
  };
  xhttp.send(params);
  return false;
}
