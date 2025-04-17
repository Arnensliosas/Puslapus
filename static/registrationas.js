document.getElementById("registerButton").addEventListener("click", function (event) {
    event.preventDefault(); // stops the form from actually submitting

    const registerName = document.getElementById("reg-username").value.trim();
    const password = document.getElementById("reg-password").value.trim();
    const errorMessage = document.getElementById("error-message");

    if (registerName === "" || password === "") {
      errorMessage.textContent = "Nu susikaupk seni uzpildyk tas eilutes ir uzsiregistruok";
  } else {
    errorMessage.textContent = "";
    alert("tu gejus");
    
  }
    console.log("register button clicked!");
  });