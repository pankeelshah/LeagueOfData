async function getLeaderboard(){
    var url = '/proxy/challenger';
    let promise = fetch(encodeURI(url));

    let jr = promise.then(function(resp){
        return resp.json();
    })

    jr.then( 
        function(data){
            createLeaderboard(data);
        }
    ).catch(
        function(data){
            console.log(data);
        }
    )
}

function createLeaderboard(data){
  
    var leagueDataTable = document.querySelector("#leagueDataTable");

    //Reset Table
    leagueDataTable.innerHTML = "";

    var players = data.entries;
    players.sort((a, b) => (a.leaguePoints < b.leaguePoints) ? 1 : -1);
    var dataLength = players.length;

    // initalize thead and tbody
    thead = document.createElement("thead");
    tbody = document.createElement("tbody");
    
    // Creating table row for thead
    tr = document.createElement("tr");
    
    // Creating the table header data
    createTableHead("Rank", tr);
    createTableHead("Summoner Name", tr);
    createTableHead("Tier", tr);
    createTableHead("LP", tr);
    createTableHead("Wins", tr);
    createTableHead("Losses", tr);
    createTableHead("Win Ratio", tr);

    // setting header with th data
    thead.appendChild(tr);

    for(var i = 0; i < dataLength; i++){
        var ob = data.entries[i];

        // Create tr element
        tr = document.createElement("tr");

        // Player Data
        createTableData(i + 1, tr);
        createTableData(ob.summonerName, tr);
        createTableData("Challenger", tr);
        createTableData(ob.leaguePoints, tr);
        createTableData(ob.wins, tr);
        createTableData(ob.losses, tr);
        var winrate = parseInt((ob.wins / (ob.losses + ob.wins))*100) + "%"
        createTableData(winrate, tr);

        // Append each row to tbody
        tbody.appendChild(tr);   
    }
    // Setting table head and body
    leagueDataTable.appendChild(thead);
    leagueDataTable.appendChild(tbody);
}

function createTableHead(value, tr){
    th = document.createElement("th");
    p = document.createElement("p");
    p.id = "tableHeadText";
    p.innerHTML = value;
    th.append(p);
    tr.appendChild(th);
}

function createTableData(value, tr){
    td = document.createElement("td");
    p = document.createElement("p");
    p.id = "tableText";
    p.innerHTML = value;
    td.append(p);
    tr.appendChild(td);
}