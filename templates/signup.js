import { ManageAccount } from './firebaseconect.js';

document.getElementById("signup-form").addEventListener("submit", (event) => {
  event.preventDefault();

  const email = document.getElementById("signup-email").value;
  const password = document.getElementById("signup-password").value;

  const account = new ManageAccount();
  account.register(email, password);

});

console.log('signup-form');