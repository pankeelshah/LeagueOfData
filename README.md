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
    test test test test test test test test test
    test test test test test test test test test
    test test test test test test test test test
    test test test test test test test test test
1. List of Controllers and their short description (No more than 50 words for each controller)
    * / : test
    * /index
    * /login
    * /logout
    * /signup
    * /news
    * /leaderboard
    * /rotation
    * /champions
    * /players
    * /proxy/<region>/<summoner_name>
    * /proxy/news/<type>
    * /proxy/challenger
    * /proxy/rotation
    * /proxy/favoritechampions
    * /proxy/favoriteplayers
1. List of Views and their short description (No more than 50 words for each view)
    * base.html - Base template which contains header and footer.
    * champions.html - Only available when a user is logged in. User can add and remove their favorite champions.
    * index.html - Default home page where League of Legend players stats can be searched.
    * leaderboard.html - Displays top 300 League of Legends players on the Summoners Rift Ranked 5v5 leaderboard.
    * login.html - Login page for users to log-in to website.
    * news.html - Shows the latest news articles associated with League of Legends.
    * players.html - Only available when a user is logged in. User can add and remove their favorite players.
    * rotation.html - Shows the current free rotation of champions that is available for the current week.
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
