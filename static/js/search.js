

function get_actors(){
    fetch('/api/actors')
    .then(response => response.json())
    .then(actors => {
        showActors(actors);
    })
};


let searchButton = document.getElementById("search_button");
searchButton.addEventListener('click', get_actors)


let submitSearch = document.getElementById('submit');
submit.addEventListener('click', getSearchInput);

function showActors(actors){
    let tableDiv = document.getElementById("searchDiv");

    let table = document.createElement('table');
    let headRow = document.createElement('tr');
    let headValue = document.createElement('td');
    headValue.innerHTML = 'Actors';

    headRow.appendChild(headValue);
    table.appendChild(headRow)

    for(let actor of actors){
        let tBodyRow = document.createElement('tr');
        let cell = document.createElement('td')
        cell.innerHTML= actor['name'];

        tBodyRow.appendChild(cell)
        table.appendChild(tBodyRow)
    }

    tableDiv.appendChild(table)
}
function getActorsByName(actor_name) {
    fetch('/search/actors',
        {method: "POST",
        body: JSON.stringify(actor_name)})
    .then(response => response.json())
    .then(actors => {
        showActors(actors);
    })
}


function getSearchInput() {
    let searchInput = document.getElementById('search_actor').value;
    getActorsByName(searchInput);
}