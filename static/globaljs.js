console.log("JS Connected!")

function validateSelectUser(){
  var username = document.forms["selectUser"]["selectedUser"].value;
  if (username == ""){
    alert("Please enter a username");
  }
}

function validateNewUser(){
  alert("function called");
  var newUsernameVar = document.forms["createNewUser"]["newUsername"].value;
  var newPasswordVar = document.forms["createNewUser"]["newPassword"].value;
  var valid = True;
  alert("function called");
  if (newUsernameVar == ""){
    valid = False;
    alert("Please enter a username");
  }
  alert("Test1");
  if (newPasswordVar == ""){
    alert("Please enter a password");
      valid = False;
  }
  alert("Test2");
  if (valid == False){
    //do not carry out creating new user SQL code
  }
  params = 'newUsernameCreate='+newUsernameVar+'&newPasswordCreate'+newPasswordVar;
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", true);
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
