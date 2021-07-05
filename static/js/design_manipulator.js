

function loggedInDomManipulation(loggedInStatus) {
    console.log(loggedInStatus);
    if (loggedInStatus != 'not_logged_in') {
        let header = document.getElementById('header-auth');
        let welcome = document.createElement('p');
        welcome.innerHTML = 'You are logged in as: ';
        let userName = document.createElement('p');
        let br = document.createElement('br');
        userName.className = 'loggedInP';
        welcome.className = 'loggedInP';
        userName.innerText = loggedInStatus;
        header.append(br);
        header.append(welcome);
        header.append(userName);

    }
}


function isLoggedIn() {
    fetch("/logged-in-status")
        .then(response => response.json())
        .then(response => {
            loggedInDomManipulation(response)
        })
}


isLoggedIn();