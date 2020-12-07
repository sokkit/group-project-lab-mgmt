console.log("JS Connected!")

function validateNewUser(){
  var newFirstnameVar = document.forms["createNewUser"]["newFirstname"].value; //taking values from form
  var newSurnameVar = document.forms["createNewUser"]["newSurname"].value;
  var public = "No"; //we are not gonna bother with public field, it will be no by default
  var newUsernameVar = document.forms["createNewUser"]["newUsername"].value;
  var newPasswordVar = document.forms["createNewUser"]["newPassword"].value;
  var checkBox = document.getElementById("confirmation");
  var admin = checkBox.checked;
  var valid = 0; // 0 means its valid, 1 means its invalid
  if (newFirstnameVar == ""){ //presence checking
    valid = 1;
    alert("Please enter a firstname");
  }
  if (newSurnameVar == ""){
    valid = 1;
    alert("Please enter a surname");
  }
  if (newUsernameVar == ""){
    valid = 1;
    alert("Please enter a username");
  }
  if (newPasswordVar == ""){
    alert("Please enter a password");
      valid = 1;
  }
  if (valid == 0){ //if all boxes are valid xhttp request is made
    params = 'newFirstname='+newFirstnameVar+'&newSurname='+newSurnameVar+'&newPublic='+public+'&newUsername='+newUsernameVar+'&newPassword'+newPasswordVar+'&Admin='+admin;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", '/Users/Add', true);
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

function UserRoleChange() {
  var username = document.forms["changeDetails"]["selectedUser"].value;
  var password = document.forms["changeDetails"]["newPassword2"].value;
  var checkBox = document.getElementById("confirmation");
  var confirmation = checkBox.checked;
  var valid = true
  if (username == "") {
    alert("please enter a username");
    valid = false;
  }
  if (password == "") {
    alert("please enter a password");
    valid = false;
  }
  if (confirmation == false) {
    alert("Please confirm the changes you want to make");
    valid = false;
  }
  if (valid == false) {
    alert("one or more elements in form were filled out incorrectly");
  } else {
    params = 'username='+username+'&password='+password';
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", '/Users/UpdatePassword', true); // true is asynchronous
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
