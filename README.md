# Get Spotify Monthly Listeners from a list of Spotify IDs.
This is a simple script to return latest monthly listeners from any Spotify ID **list** using the Soundcharts API.<br><br>
**_NOTE: THIS WILL ONLY WORK WITH SOUNDCHARTS <code>SANDBOX</code> CREDENTIALS_**, that are included in the code.<br>
<p>To use it on the <code>PROD</code> SOUNDCHARTS environement, you must <strong>obtain Soundcharts Production credentials</strong> and update the code accordingly.<br>
  To do that, please refer to the <a href="https://doc.api.soundcharts.com/api/v2/doc">Soundcharts documentation.<a><br>
&nbsp;&nbsp;&nbsp;&nbsp;<i>Feel free to <a href="https://github.com/JeremLeOuf/GET-Spotify_monthlyListeners-FROM-SpotifyIDs/edit/main/README.md#bottom-line">reach out<a> if you need some help!</i><br>
</p>
<br>

## Input: 
- Input required:
  - **__A **CSV file** with each Spotify IDs you want to fetch the recent monthly listeners from, one per line.__**<br>
  - <strong>This CSV file containing Spotify IDs must be located in the <code>input</code> folder (for simplicity).<strong>
  
---
IMPORTANT NOTE:
- With the <code>SANDBOX</code> Soundcharts credentials, you are limited to the two rows in <code>\input\spotify_ids.csv</code>, that are respectively <i>'Billie Eilish'</i> and <i>'Tones & I'</i>.
- With the <code>PRODUCTION</code> Soundcharts credentials, you can add as many <code>spotify_id</code>'s as you want 
  - :warning: <strong>Be <i>VERY</i> careful as it will use credits from your paid Soundcharts API plan!</strong>
---
  
- <b>Format of the .csv input file:</b>
  <br>
<pre>
|spotify_id            |
|----------------------|
|6qqNVTkY8uBg9cP3Jd7DAH|
|2NjfBq1NflQcKSeiDooVjY|
</pre>
  This is the actual content of the default <code>spotify_ids.csv</code> file, located in the `input` folder that will be exported and used for the rest of the program.<br>
 
<strong>⛔ <i>HOWEVER, it could handle as many `spotify_id`'s you desire **AS LONG AS YOUR ARE USING PRODUCTION CREDENTIALS**</strong> (not included in this public repo, for obvious privacy reasons).</i></h4><br>
<i> With <strong>SANDBOX credentials</strong>, you'll be able only to use the two artists above (Billie Eilish and Tones & I, only artists included in the sandbox dataset.</i>
<br><br>
 
## Execution:
- Run the `main.py` file.
- It will prompt you with a window where you have to select the aforementioned `spotify_id.csv` file. <br>
  It should redirect you to the appropriate directory by default.
- The program will first print how the file structure looks like. (informative)
- It will then print how the resulting DataFrame will look like. (informative)
- After 2 seconds, it will print it to a new .csv file named `results-{YYYY-MM-DD}.csv` (with today's date), located in the `output` folder, and show you a success message (if successful).
- All done! 🎉
  
## Output:
  <strong>✅ Now, you should find the correctly named output file in the <code>output</code> folder.</strong><br>
  <strong>📈 Enjoy!</strong>
<br><br>

## Bottom line:
- For any suggestions for improvements / optimizations, I'm very welcome to any advice, so feel free to commit!- I'm a fairly new Python developer, trying to constantly learn and improve. All suggestions are welcome!
- You can reach out to me on my <a href="https://github.com/JeremLeOuf/">GitHub profile</a>, through <a href="https://discordapp.com/users/207913674092969985">Discord<a> or on my <a href="https://twitter.com/jeremie_pk">Twitter<a>. 
<br>Happy to connect to y'all! 
Cheers! 🤖
