# Get Spotify Monthly Listeners from a list of Spotify IDs.
Simple script to return latest monthly listeners from any Spotify ID using the Soundcharts API.<br><br>
**_NOTE: THIS WILL ONLY WORK WITH SOUNDCHARTS SANDBOX CREDENTIALS.<br>
To use it on the PROD SOUNDCHARTS environemnt, you must **obtain Soundcharts Production credentials**_**.
  - To do that, please refer to the <a href="https://doc.api.soundcharts.com/api/v2/doc">Soundcharts documentation.<a>
<br>

## Input: 
- Input required:
  - **__A **CSV file** with each Spotify IDs you want to get the most recent monthly listeners from, one per line.<br>
This CSV file containing Spotify IDs must be located in the `input` folder (for simplicity).__**
    - With the SANDBOX Soundcharts credentials, you are limited to the two inputs in `\input\spotify_ids.csv`
    - With the PRODUCTION Soundcharts credentials, you can add as many `spotify_id`s as you want 
      - :warning: **Be VERY careful as it will use credits from your paid Soundcharts API plan!**

 <br>
• <b>Format of the .csv input file:</b>
  <br>
<pre>
|spotify_id            |
|----------------------|
|6qqNVTkY8uBg9cP3Jd7DAH|
|2NjfBq1NflQcKSeiDooVjY|
</pre>
This is the actual content of the default `spotify_ids.csv` file, located in the `input` folder that will be exported.<br>
 
<strong>⛔ <i>HOWEVER, it could handle as many `spotify_id`'s you desire **AS LONG AS YOUR ARE USING PRODUCTION CREDENTIALS**</strong> (not included in this public repo, for obvious privacy reasons).</i></h4>
<br><br>
 
## Execution:
- Run the `main.py` file.
- It will prompt you with a window where you should select the aforementioned `spotify_id.csv` file. It should point you to the appropriate directory by default.
- The program will first print how the file structure looks like.
- It will then print how the resulting DataFrame will look like.
- After 2 seconds, it will print it to a new .csv file named `results-{YYYY-MM-DD}.csv`, located in the `output` folder, and show you a success message.
<h4>All good! 🎉</h4>
<strong>Now, you should find the correctly named output file in the `output` folder.</strong><br>
**_Enjoy!_**
<br><br>

## Bottom line:
- For any suggestions for improvement / optimization, I'm very welcome to any advice, so feel free to commit!- I'm a fairly new Python developer, trying to constantly learn and improve. All suggestions are welcome!
- You can reach out to me on my <a href="https://github.com/JeremLeOuf/">GitHub profile</a> or through <a href="https://discordapp.com/users/207913674092969985">Discord<a> or <a href="https://twitter.com/jeremie_pk">Twitter<a>. Happy to connect to y'all! 
Cheers!
