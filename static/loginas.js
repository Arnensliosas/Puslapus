document.getElementById("loginButton").addEventListener("click", function (event) {
    event.preventDefault(); // stops the form from actually submitting

    const loginName = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMessage = document.getElementById("error-message");

    if (loginName === "" || password === "") {
      errorMessage.textContent = "Nu susikaupk seni uzpildyk tas eilutes ir prisijunk";
  } else {
    errorMessage.textContent = "";
    alert("tu gejus");
  }

    console.log("Login button clicked!");
  });
