console.log("JS Connected!")

function validateSelectUser(){
  var username = document.forms["selectUser"]["selectedUser"].value;
  if (username == ""){
    alert("Please enter a username");
  }
}

function validateNewUser(){
  var newUsernameVar = document.forms["createNewUser"]["newUsername"].value;
  var newPasswordVar = document.forms["createNewUser"]["newPassword"].value;
  var valid = True;
  if (newUsernameVar == ""){
    valid = False;
    alert("Please enter a username");
  }
  alert("Test1");
  if (newPasswordVar.length < 1){
    alert("Please enter a password");
      valid = False;
  }
  alert("Test2");
  if (valid == False){
    //do not carry out creating new user SQL code
  }
}

function addCustomer() {
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
  xhttp.send(params);
  return false;
}
