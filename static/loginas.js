document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault();

    const loginName = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMessage = document.getElementById("error-message");

  errorMessage.textContent = "";
  const formData = new FormData();
  formData.append('username', loginName);
  formData.append('password', password);

  fetch('/login', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
        errorMessage.style.color = "green";
        errorMessage.textContent = "mldc sekmingai prisijungei"
        setTimeout(() => {
          window.location.href = '/namuDarbai';
        }, 1000)  
      } else {
          errorMessage.textContent = data.message;
      }
  })
  .catch(error => {
      console.error('Error:', error);
      errorMessage.style.color = "blue"
      errorMessage.textContent = "nu bbz seni liudna, bandyk dar:D";
  });
});