

function sendRegData(regEmail, regPassword) {
    fetch(
        "/reg-data", {
            method: 'POST', body:
                JSON.stringify({regEmail: regEmail, regPassword: regPassword})})
        .then(response => response.json())
        .then(response => {
            alert('This email adress already registered! Give an other one!')
        })
}


function regSubmit() {
    let regSubmit = document.getElementById('reg_submit');
    regSubmit.addEventListener('click', getRegData);
}


function getRegData() {
    let regEmail = document.getElementById('reg_email').value;
    let regPassword = document.getElementById('reg_password').value;
    sendRegData(regEmail, regPassword);
}




regSubmit();