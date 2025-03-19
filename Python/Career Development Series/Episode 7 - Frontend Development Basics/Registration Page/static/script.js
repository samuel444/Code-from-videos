function buttonClicked() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        let message = document.getElementById('message');
        if (data.status === 'success') {
            message.style.color = 'green';
        } else {
            message.style.color = 'red';
        }
        message.textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
}

function buttonClick() {
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let confpassword = document.getElementById('confpassword').value;

    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password, confpassword: confpassword })
    })
    .then(response => response.json())
    .then(data => {
        let message = document.getElementById('message');
        if (data.status === 'success') {
            message.style.color = 'green';
            setTimeout("window.location.href = '/login'", 2000)
        } else {
            message.style.color = 'red';
        }
        message.textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
}
function LpasswordShow() {
    let password = document.getElementById('password');
    if (password.type === "password") {
        password.type = "text";
      } else {
        password.type = "password";
      }
}

function SpasswordShow() {
    let password = document.getElementById('password');
    let confpassword = document.getElementById('confpassword');
    if (password.type === "password") {
        password.type = "text";
        confpassword.type = 'text';
      } else {
        password.type = "password";
        confpassword.type = 'password';
      }
}
