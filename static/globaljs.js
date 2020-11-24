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
