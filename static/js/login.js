

function sendLogInData(logInEmail, logInPassword) {
    fetch("/login-data", {
        method: 'POST', body: JSON.stringify({
            logInEmail: logInEmail, logInPassword: logInPassword
                })})
                .then (response => response.json())
                .then(answer => {
                    alert(answer);
                })

}


function submitLogIn() {
    let logInSubmit = document.getElementById('log_submit');
    logInSubmit.addEventListener('click', getLogInData);
}


function getLogInData() {
    let logInEmail = document.getElementById('log_email').value;
    let logInPassword = document.getElementById('log_password').value;
    sendLogInData(logInEmail, logInPassword);
}


function sendLogOut() {
    fetch("/logout", {
        method: 'POST', body: JSON.stringify('true')})
        .then(response => response.json())
        .then(response => {
            alert('Bye');
            if (response == 'Logout') {
                alert('By Bye!')
                window.location.href = "http://127.0.0.1:5000/" ;
            }
        })
}


submitLogIn();


function logOutClick() {
    let logOutButton = document.getElementById('bt_logout');
    logOutButton.addEventListener('click', sendLogOut);
}


logOutClick();