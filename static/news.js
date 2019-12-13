async function getNews(){
    // console.log("test");
    var url = 'proxy/news/league-of-legends';
    let promise = fetch(encodeURI(url));
    let jr = promise.then(function(resp){
        return resp.json();
    })

    jr.then( 
        function(data){
            var articles = data.articles;
            var aLen = articles.length;
            var mainDiv = document.querySelector(".cardContainer");
            for(var i = 0; i < aLen; i++){
                displayNews(mainDiv, articles[i], i + 1);
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
    card.style.width = "50%";
    card.style.height = "20%";

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

function test(){
    var searchText = document.querySelector("#search").value;
    let divs = document.getElementsByClassName("cardDiv");
    // console.log(searchText);
    if(searchText != ""){
        
        // console.log(divs);
        for (let x = 0; x < divs.length; x++) {
            var innerText = divs[x].innerText;
            let div = divs[x];
            if(innerText.toLowerCase().includes(searchText.toLowerCase())){
                div.style.display = 'block';
            }
            else{
                div.style.display = 'none';
            }
        }
    }
    else{
        for (let x = 0; x < divs.length; x++) {
            let div = divs[x];
            div.style.display = 'block';
        }
    }
}