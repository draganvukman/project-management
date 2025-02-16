// Real-time password validation
document.getElementById("id_password1").addEventListener("input", function () {
  const password = this.value;
  const feedback = document.getElementById("password-strength");
  if (password.length < 8) {
    feedback.textContent = "Password must be at least 8 characters.";
    feedback.className = "text-danger";
  } else {
    feedback.textContent = "Password is strong!";
    feedback.className = "text-success";
  }
});

// Email format validation
document.getElementById("id_email").addEventListener("input", function () {
  const email = this.value;
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const feedback = document.getElementById("email-feedback");
  if (!regex.test(email)) {
    feedback.textContent = "Please enter a valid email address.";
    feedback.className = "text-danger";
  } else {
    feedback.textContent = "";
  }
});
