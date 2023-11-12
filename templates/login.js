import { ManageAccount } from './firebaseconect.js';

document.getElementById("login-form").addEventListener("submit", (event) => {
  event.preventDefault();

  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  const account = new ManageAccount();
  account.authenticate(email, password);

});

console.log('login-form');