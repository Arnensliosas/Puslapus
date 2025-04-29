document.getElementById("registerForm").addEventListener("submit", function (event) {
  event.preventDefault();

  const registerName = document.getElementById("reg-username").value.trim();
  const password = document.getElementById("reg-password").value.trim();
  const errorMessage = document.getElementById("reg-error-message");

  if (registerName === "" || password === "") {
    console.log("Tušti laukai aptikti");
    errorMessage.style.color = "red";
    errorMessage.textContent = "Nu susikaupk seni uzpildyk tas eilutes ir uzsiregistruok";
} else {
  errorMessage.textContent = "";
  const formData = new FormData();
  formData.append('reg-username', registerName);
  formData.append('reg-password', password);

  fetch('/register', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          errorMessage.style.color = "green";
          errorMessage.textContent = data.message;
          setTimeout(() => {
              window.location.href = '/';  
          }, 1000);  
      } else {
          errorMessage.style.color = "red";
          errorMessage.textContent = data.message;
      }
  })
  .catch(error => {
      console.error('Error:', error);
      errorMessage.style.color = "blue"
      errorMessage.textContent = "jo bbz seni gl";
    });
  }
});