# LeagueWebsite

1. Project Type: Plan A
1. Link to live Application: https://league-of-legends-data.herokuapp.com/
1. Link to Github Code Repository: https://github.com/pankeelshah/LeagueofData
1. List of Technologies/API's Used
   * BootStrap
   * Flask
   * Riot Games API
   * Google News API
1. Detailed Description of the project (No more than 500 words) <br />

League of Legend's web application created using the Flask framework which allows users to get many different types of League of Legends information, and also store their own information. 

On the Home page, users can search for information on specific League of Legend's players and get statistics on the different game modes that they play, and their tier, rank, wins, losses and win rate in those game modes. 

On the Leaderboard page, users can view the current top of the ranked leaderboard and see the top 300 players on the ladder at the current moment.

On the Free Rotation page, users can view the current free champion rotation. This page shows a list of the champions that are available and free to play for the current week. These champions can be clicked on which will lead to a wiki page with more information on those champions. 

On the News page, users can view cards displaying the latest League of Legends articles. There is also a search bar which allows users to search for specific articles. These articles can be clicked to visit the full link.

On the Login page, users can sign in to their account. If the user does that have an account, they can click the create an account link. On the Create An Account page, users can create a new account. All created users have a unique email and summoner name. Once a user has logged in, two new tabs are available: Champions and Players.

On the Champions page, users can keep track of their favorite champions. They can add or remove champions to update their current favorite champions. This list of favorite champions is saved in the database. 

On the Players page, users can keep track of their favorite players. They can add or remove players to update their current favorite players. This list of favorite players is saved in the database. 

To aid with testing purposes we have provided additional information which may be used to verify website functionality. 

Already Created Accounts(username, password): 
* [admin1@example.com](admin1@example.com), admin1
* [admin2@example.com](admin2@example.com), admin2

Feel free to create your own accounts. To create an account you must provide a valid summoner name. You can find a list of summoner names in the Leaderboard tab.

When champions to your favorite champions list, you must provide real champions. Here is a [list](https://na.leagueoflegends.com/en/game-info/champions/) containing all 147 League of Legend champions.

1. List of Controllers and their short description (No more than 50 words for each controller)
    * / - Default which redirects to /index.
    * /index - Default home page, which uses JavaScript to search and display results.
    * /login - Handle's login form validation and checks database for user.
    * /logout - Logs out user and makes changes in database.
    * /signup - Handle's signup form validation and adds user to database.
    * /news - Uses onLoad() function to call JavaScript and display news.
    * /leaderboard - Uses onLoad() function to call JavaScript and display leaderboard.
    * /rotation - Uses onLoad() function to call JavaScript and display current free rotation.
    * /champions - Uses form validation to check for input, make sure that champion exists, and check weather the champion is in the database already. Depending on if user has clicked add or remove, adds or removes the champion from the database.
    * /players - Uses form validation to check for input, and make sure that the champion is in the database already. Depending on if user has clicked add or remove, adds or removes the player from the database.
    * /proxy/&lt;region&gt;/&lt;summoner_name&gt; - Makes an API call to Riot's API to get statistics on a specific player. 
    * /proxy/news/&lt;type&gt; - Makes an API call to Google News API to get the latest League of Legends articles.
    * /proxy/challenger - Makes an API call to Riot's API to get the top 300 players on the leaderboard.
    * /proxy/rotation - Makes an API call to Riot's API to get the current week's free champion rotation. 
    * /proxy/favoritechampions - Gets the current users favorite champions from the database. 
    * /proxy/favoriteplayers - Gets the current users favorite players from the database. 
1. List of Views and their short description (No more than 50 words for each view)
    * base.html - Base template which contains header and footer.
    * champions.html - Only available when a user is logged in. User can add and remove their favorite champions. This will display their favorite champions which can be clicked to visit a website with more information on them.
    * index.html - Default home page where League of Legend players stats can be searched.
    * leaderboard.html - Displays top 300 League of Legends players on the Summoners Rift Ranked 5v5 leaderboard.
    * login.html - Login page for users to log-in to website.
    * news.html - Shows the latest news articles associated with League of Legends.
    * players.html - Only available when a user is logged in. User can add and remove their favorite players. This will display their favorite players which can be clicked to visit a website with more information on them.
    * rotation.html - Shows the current free rotation of champions that is available for the current week. The champions can be clicked to visit a website with more information on them.
    * signup.html - Signup page to create a new account.
1. List of Tables, their Structure and short description
    * champion - Holds all user's favorite champions along with which user they belong to.
    * player - Holds all user's favorite players along with which user they belong to.
    * user - Holds all registered users and keeps track of currently logged in user.
1. References/Resources:
    * https://getbootstrap.com/
    * https://www.w3schools.com/
    * https://developer.riotgames.com/
    * https://newsapi.org/s/google-news-api
    * https://github.umn.edu/mill0242/CS4131Fall2019
