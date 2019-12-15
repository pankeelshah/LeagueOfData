async function getPlayers(){
    var url = 'proxy/favoriteplayers';
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        return resp.json();
    })
    jr.then( 
        function(data){
            var champions_list = data[0]
            var dataLength = champions_list.length;
            var mainDiv = document.querySelector(".cardContainer");
            for(var i = 0; i < dataLength; i++){
                displayPlayers(mainDiv, champions_list[i], i + 1);
            }
        }
    )
}

function displayPlayers(mainDiv, champion_name, count){

    // var wrapper = document.querySelector("#wrapper");
    var cardDiv = document.createElement("div");
    cardDiv.id = "cardDiv";
    cardDiv.className = "cardDiv";

    var card = document.createElement("div");
    var br = document.createElement("br");
    card.className = "Card";
    card.style.width = "400px";
    card.style.height = "400px";

    var link = document.createElement("a");
    link.href = "https://na.op.gg/summoner/userName=" + champion_name;
    link.id = "link"
    link.target = "_blank";

    // get image from folder
    // var img = document.createElement("img");
    // img.className = "card-img-bottom";
    // img.src = img_link;
    // img.alt = "Card image";
    // img.style.width = "100%";
    // img.style.height =  "85%";

    var cardBody = document.createElement("div");
    cardBody.className = "card-body";

    // champion name
    var title = document.createElement("h4");
    title.className = "card-title";
    title.innerHTML = champion_name;

    // not sure
    // var discription = document.createElement("p");
    // discription.className = "card-text";
    // discription.innerHTML = d[id];

    mainDiv.appendChild(cardDiv);
    cardDiv.appendChild(card);
    card.appendChild(link);
    //link.appendChild(img);
    link.appendChild(cardBody);
    cardBody.appendChild(title);
    //cardBody.appendChild(discription);
}