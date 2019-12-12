async function getPlayerStats(){
    var name = document.querySelector("#username").value;
    var region_dropdown = document.querySelector("#region");
    var region = region_dropdown.options[region_dropdown.selectedIndex].value;
    var url = '/proxy/' + region + '/' + name;
    let promise = fetch(encodeURI(url));

    let jr = promise.then(function(resp){
        return resp.json();
    })

    if(name == ""){
      alert("Please enter a summoner name.");
      return;
    }
    
    jr.then( 
        function(data){
          if (data.length == 0){
            alert("Summoner does not exist.");
          }
          else {
            createTableStats(data);
          }
        }
    ).catch(
        function(data){
            console.log(data);
        }
    )
}

function createTableStats(data){
  
  var leagueDataTable = document.querySelector("#leagueDataTable");

  //Reset Table
  leagueDataTable.innerHTML = "";

  //Initialize table headers
  if(data.error == "Player Not Found"){
    // console.log("Player does not exist, or no data available.")
    alert("Player does not exist, or no data available.");
  }else{

    console.log(data);
    var dataLength = data.length;
    for(var i = 0; i < dataLength; i++){

      // initalize tbody
      tbody = document.createElement("tbody");
      
      var ob = data[i];

      // adding table rows
      createTableRow("Queue Type", ob.queueType, tbody);
      createTableRow("Tier", ob.tier, tbody);
      createTableRow("Rank", ob.rank, tbody);
      createTableRow("Wins", ob.wins, tbody);
      createTableRow("Losses", ob.losses, tbody);
      var winrate = parseInt((ob.wins / (ob.losses + ob.wins))*100) + "%"
      createTableRow("Win Rate", winrate, tbody);
      createTableRow("", "", tbody);

      // Setting table body
      leagueDataTable.appendChild(tbody);
    }

  }
 }

function createTableRow(key, value, tbody){
  // Create tr element
  tr = document.createElement("tr");
    
  // Key column Data
  td = document.createElement("td");
  p = document.createElement("p");
  p.id = "tableText";
  p.innerHTML = key;
  td.append(p);
  tr.appendChild(td);

  // Value column Data
  td = document.createElement("td");
  p = document.createElement("p");
  p.id = "tableText";
  p.innerHTML = value;
  td.append(p);
  tr.appendChild(td);

  // Append each row to tbody
  tbody.appendChild(tr);
}
  
window.onload = function(){ 
  document.getElementById("username").onkeypress=function(e){
    if(e.keyCode==13){
      document.getElementById('playerStatsBtn').click();
    }
  }
};
  