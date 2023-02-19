# Get Spotify Monthly Listeners from a list of Spotify IDs.
Simple script to return latest monthly listeners from any Spotify ID using the Soundcharts API.<br>

## Input: 
**__A **CSV file** with each SpotifyIDs you want to get the most recent monthly listeners from, one per line.<br>
The CSV file containing SpotifyIDs must be in the `input` folder for simplicity.__**

- Format of the .csv input file:<br>
<pre>
|spotify_id            |      
|----------------------|
|6qqNVTkY8uBg9cP3Jd7DAH|
|2NjfBq1NflQcKSeiDooVjY|
</pre>
With as many `spotify_id`'s you desire.

## Execution:
- Run the `main.py` file.
- It will prompt you with a window where you should select the aforementioned `spotify_id.csv` file. It should point you to the appropriate directory by default.
- The program will first show you how the file structure looks like.
- It will then show you how the resulting DataFrame will look like.
- After 2 seconds, it will print it to a new .csv file named `results-{YYYY-MM-DD}.csv` and show you a success message.
- All good! 🎉

Now, you should find the output file in the `output` folder. 
**Enjoy!**

## Bottom line:
- For any suggestions for improvement / optimization, I'm very welcome to any advice, so feel free to commit!- I'm a fairly new Python developer, trying to constantly learn and improve. 
- You can reach out to me on my <a href="https://github.com/JeremLeOuf/">GitHub profile</a> or through <a href="https://discordapp.com/users/207913674092969985">Discord<a> or <a href="https://twitter.com/jeremie_pk">Twitter<a>. Happy to connect to y'all! 
Cheers!
