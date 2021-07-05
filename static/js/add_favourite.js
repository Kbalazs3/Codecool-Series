

function sendFavourite(favouriteId) {
    fetch("/send-favourite", {
        method: 'POST', body:JSON.stringify({favouriteId})})
        .then(response => response.json())
        .then(response => {
            alert(response)
        })
}


function addFavouriteButton() {
    let favButton = document.getElementsByTagName('favourite');


}


function putIdToButton (clickId) {
     sendFavourite(clickId)
}

