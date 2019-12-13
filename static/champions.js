async function getChampions(){
    var url = '/proxy/champions';
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