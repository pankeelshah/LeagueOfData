// var d = {'133': 'Quinn', '164': 'Camille', '131': 'Diana', '498': 'Xayah', '136': 'AurelionSol', '134': 'Syndra', '497': 'Rakan', '24': 'Jax', '25': 'Morgana', '26': 'Zilean', '27': 'Singed', '20': 'Nunu', '21': 'MissFortune', '22': 'Ashe', '23': 'Tryndamere', '28': 'Evelynn', '29': 'Twitch', '222': 'Jinx', '4': 'TwistedFate', '8': 'Vladimir', '163': 'Taliyah', '120': 'Hecarim', '121': 'Khazix', '122': 'Darius', '267': 'Nami', '266': 'Aatrox', '126': 'Jayce', '127': 'Lissandra', '268': 'Azir', '59': 'JarvanIV', '58': 'Renekton', '55': 'Katarina', '54': 'Malphite', '57': 'Maokai', '56': 'Nocturne', '51': 'Caitlyn', '50': 'Swain', '53': 'Blitzcrank', '412': 'Thresh', '115': 'Ziggs', '114': 'Fiora', '117': 'Lulu', '89': 'Leona', '111': 'Nautilus', '110': 'Varus', '113': 'Sejuani', '112': 'Viktor', '82': 'Mordekaiser', '83': 'Yorick', '80': 'Pantheon', '81': 'Ezreal', '86': 'Garen', '84': 'Akali', '85': 'Kennen', '429': 'Kalista', '3': 'Galio', '7': 'Leblanc', '523': 'Aphelios', '421': 'RekSai', '420': 'Illaoi', '427': 'Ivern', '245': 'Ekko', '246': 'Qiyana', '240': 'Kled', '102': 'Shyvana', '103': 'Ahri', '101': 'Xerath', '106': 'Volibear', '107': 'Rengar', '104': 'Graves', '105': 'Fizz', '39': 'Irelia', '38': 'Kassadin', '33': 'Rammus', '32': 'Amumu', '31': 'Chogath', '30': 'Karthus', '37': 'Sona', '36': 'DrMundo', '35': 'Shaco', '34': 'Anivia', '518': 'Neeko', '432': 'Bard', '517': 'Sylas', '516': 'Ornn', '60': 'Elise', '61': 'Orianna', '62': 'Wukong', '63': 'Brand', '64': 'LeeSin', '67': 'Vayne', '68': 'Rumble', '69': 'Cassiopeia', '254': 'Vi', '145': 'Kaisa', '2': 'Olaf', '6': 'Urgot', '99': 'Lux', '98': 'Shen', '91': 'Talon', '90': 'Malzahar', '92': 'Riven', '223': 'TahmKench', '161': 'Velkoz', '96': 'KogMaw', '11': 'MasterYi', '10': 'Kayle', '13': 'Ryze', '12': 'Alistar', '15': 'Sivir', '14': 'Sion', '17': 'Teemo', '16': 'Soraka', '19': 'Warwick', '18': 'Tristana', '150': 'Gnar', '154': 'Zac', '157': 'Yasuo', '555': 'Pyke', '238': 'Zed', '235': 'Senna', '236': 'Lucian', '48': 'Trundle', '119': 'Draven', '44': 'Taric', '45': 'Veigar', '42': 'Corki', '43': 'Karma', '40': 'Janna', '41': 'Gangplank', '1': 'Annie', '5': 'XinZhao', '9': 'Fiddlesticks', '201': 'Braum', '203': 'Kindred', '202': 'Jhin', '142': 'Zoe', '143': 'Zyra', '141': 'Kayn', '77': 'Udyr', '76': 'Nidalee', '75': 'Nasus', '74': 'Heimerdinger', '72': 'Skarner', '79': 'Gragas', '78': 'Poppy', '350': 'Yuumi'};

async function getChampions(){
    // var url = 'proxy/favoritechampions';
    // let promise = fetch(encodeURI(url));
    // let jr = promise.then(function(resp){
    //     return resp.json();
    // })
    // jr.then( 
    //     function(data){
    //         var champions_list = data[0]
    //         var dataLength = champions_list.length;
    //         var mainDiv = document.querySelector(".cardContainer");
    //         mainDiv.innerHTML = "";
    //         for(var i = 0; i < dataLength; i++){
    //             displayChampions(mainDiv, champions_list[i], i + 1);
    //         }
    //     }
    // )
}

function displayChampions(mainDiv, champion_name, count){

    var img_link = "http://ddragon.leagueoflegends.com/cdn/img/" + "champion/splash/" + champion_name + "_0.jpg";
    //var img_link = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_0.jpg";
    console.log(img_link);

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
    link.href = "https://leagueoflegends.fandom.com/wiki/" + champion_name;
    link.id = "link"
    link.target = "_blank";

    // get image from folder
    var img = document.createElement("img");
    img.className = "card-img-bottom";
    img.src = img_link;
    img.alt = "Card image";
    img.style.width = "100%";
    img.style.height =  "85%";

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
    link.appendChild(img);
    link.appendChild(cardBody);
    cardBody.appendChild(title);
    //cardBody.appendChild(discription);
}