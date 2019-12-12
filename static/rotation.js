async function getRotation(){
    // console.log("test");
    var url = 'proxy/rotation';
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        return resp.json();
    })

    jr.then( 
        function(data){
            console.log(data);
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

    var link = document.createElement("a");
    link.href = article.url;
    link.id = "link"
    link.target = "_blank";

    var img = document.createElement("img");
    img.className = "card-img-bottom";
    img.src = article.urlToImage;
    img.alt = "Card image";
    img.style.width = "100%";
    img.style.height =  "50%";

    var cardBody = document.createElement("div");
    cardBody.className = "card-body";

    var title = document.createElement("h4");
    title.className = "card-title";
    title.innerHTML = article.title;

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