async function getPlayerStats(){
    var name = document.querySelector("#username").value;

    var region_dropdown = document.querySelector("#region");
    var region = region_dropdown.options[region_dropdown.selectedIndex].value;

    console.log(name);
    console.log(region_dropdown);
    console.log(region);

    var url = '/proxy/' + region + '/' + name;
    let promise = fetch(encodeURI(url));

    let jr = promise.then(function(resp){
        return resp.json();
    })

    jr.then( 
        function(data){
            console.log(data);
        }
    ).catch(
        function(data){
            console.log(data);
        }
    )
}

function createTableStats(data){
  
    var fortDataTable = document.querySelector("#fortDataTable");
  
    //Reset Table
    fortDataTable.innerHTML = "";
  
    //Initialize table headers
    if(data.error == "Player Not Found"){
      // console.log("Player does not exist, or no data available.")
      alert("Player does not exist, or no data available.");
    }else{
  
      var dataLength = data.lifeTimeStats.length;
      
      // initalize thead and tbody
      thead = document.createElement("thead");
      tbody = document.createElement("tbody");
      
      // Creating table row for thead
      tr = document.createElement("tr");
      
      // Creating the table header data
      // th = document.createElement("th");
      // th.innerHTML = "index";
      // tr.appendChild(th);
      // th = document.createElement("th");
      // th.innerHTML = "key";
      // tr.appendChild(th);
      // th = document.createElement("th");
      // th.innerHTML = "value";
      // tr.appendChild(th);
  
      // setting header with th data
      // thead.appendChild(tr);
  
      for(var i = 0; i < dataLength; i++){
        var ob = data.lifeTimeStats[i];
  
        // Create tr element
        tr = document.createElement("tr");
        
        // Index column Data
        // td = document.createElement("td");
        // p = document.createElement("p");
        // p.innerHTML = i+1;
        // td.append(p)
        // tr.appendChild(td);
  
        // Key column Data
        td = document.createElement("td");
        p = document.createElement("p");
        p.id = "tableText";
        p.innerHTML = ob.key;
        td.append(p);
        tr.appendChild(td);
  
        // Value column Data
        td = document.createElement("td");
        p = document.createElement("p");
        p.id = "tableText";
        p.innerHTML = ob.value;
        td.append(p);
        tr.appendChild(td);
  
        // Append each row to tbody
        tbody.appendChild(tr);
      }
  
      // Setting table head and body
      fortDataTable.appendChild(thead);
      fortDataTable.appendChild(tbody);
      // console.log(data.accountId);
    }
    document.querySelector("#username").disabled = false;
    document.querySelector("#gaming_console").disabled = false;
    document.querySelector("#playerStatsBtn").disabled = false;
    document.querySelector("#playerStatsBtn").value = "Search";
  }
  
  window.onload = function(){ 
    document.getElementById("username").onkeypress=function(e){
      if(e.keyCode==13){
        document.getElementById('playerStatsBtn').click();
      }
    }
  };
  