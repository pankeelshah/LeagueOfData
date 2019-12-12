async function getRotation(){
    // console.log("test");
    var url = 'proxy/rotation';
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        return resp.json();
    })
    jr.then( 
        function(data){
            var dataLength = data.freeChampionIds.length;
            var mainDiv = document.querySelector(".cardContainer");
            for(var i = 0; i < dataLength; i++){
                displayNews(mainDiv, data.freeChampionIds[i], i + 1);
            }
        }
    )
}

function displayNews(mainDiv, article, count){
    // var wrapper = document.querySelector("#wrapper");
    var cardDiv = document.createElement("div");
    cardDiv.id = "cardDiv";
    cardDiv.className = "cardDiv";

    var card = document.createElement("div");
    var br = document.createElement("br");
    card.className = "Card";
    card.style.width = "400px";
    card.style.height = "400px";

    // https://leagueoflegends.fandom.com/wiki/Jax
    var link = document.createElement("a");
    link.href = article.url;
    link.id = "link"
    link.target = "_blank";

    // get image from folder
    var img = document.createElement("img");
    img.className = "card-img-bottom";
    img.src = article.urlToImage;
    img.alt = "Card image";
    img.style.width = "100%";
    img.style.height =  "50%";

    var cardBody = document.createElement("div");
    cardBody.className = "card-body";

    // champion name
    var title = document.createElement("h4");
    title.className = "card-title";
    title.innerHTML = article.title;

    // not sure
    var discription = document.createElement("p");
    discription.className = "card-text";
    discription.innerHTML = article.description;

    mainDiv.appendChild(cardDiv);
    cardDiv.appendChild(card);
    card.appendChild(link);
    link.appendChild(img);
    link.appendChild(cardBody);
    cardBody.appendChild(title);
    cardBody.appendChild(discription);
}