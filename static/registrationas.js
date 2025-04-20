document.getElementById("registerButton").addEventListener("click", function (event) {

    const registerName = document.getElementById("reg-username").value.trim();
    const password = document.getElementById("reg-password").value.trim();
    const errorMessage = document.getElementById("error-message");

    if (registerName === "" || password === "") {
      errorMessage.textContent = "Nu susikaupk seni uzpildyk tas eilutes ir uzsiregistruok";
  } else {
    errorMessage.textContent = "";
    alert("tu gejus");
    document.querySelector("form").submit();
    
  }
    console.log("register button clicked!");
  });