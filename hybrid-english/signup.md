---
layout: default
title: Sign Up
permalink: /signup/
---

<form id="leadForm">
  <input type="text" name="fullName" placeholder="Full Name" required>
  <input type="email" name="email" placeholder="Email" required>
  <input type="text" name="role" placeholder="Role / Position">
  <input type="tel" name="phone" placeholder="Phone Number">
  <textarea name="challenge" placeholder="Main Communication Challenge"></textarea>
  <button type="submit">Submit</button>
</form>

<script>
document.getElementById("leadForm").addEventListener("submit", function(e) {
  e.preventDefault();

  var formData = new FormData(this);

  fetch("https://script.google.com/macros/library/d/1sykrC0lfuFi2zAa02fiBGm7e99xKZwJgb1paDcM-ZhAAWi5NmYm3An_D/2", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    alert("Thank you. We will review your submission.");
    document.getElementById("leadForm").reset();
  })
  .catch(error => {
    alert("Submission failed. Please try again.");
  });
});
</script>
