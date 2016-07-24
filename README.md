# OSM-EventGrade
To analyze popularity of events near user specified location based on number of likes, number of comments, number of images , weather at time of event, etc. Also, user can select category of events on basis of his choice like education, social, etc. Eventley help users to find popular and relevant(weather on day is fine) events near him on basis of his choice of category.
<br/>
Languages used: Python, Django, Html, Css, JS

##Setup (Commands are for linux)
Install python <br/>
Install pip ( sudo apt-get install python-pip python-dev build-essential) <br/>
Install djnago (sudo pip install Django==1.9.7) <br/>
Install MySQLDB (sudo apt-get install python-mysqldb) <br/>
Install python unicodecsv module (sudo pip install unicodecsv) <br/>
Install python library of JSON (sudo pip install simplejson) <br/>
Go to link: http://api.eventful.com/libs/python/ and install python library of eventful as per mentioned in link. <br/>
Install plotly python library (sudo pip install plotly) <br/>
Clone the repository: git clone https://github.com/megha-code/OSM-EventGrade.git <br/>
Move to your clone repo folder: ~/OSM-EventGrade/Eventgrade/ <br/>
Open in terminal and type "python manage.py runserver" <br/>
Hey you are good to go and your server is rnning. Now you can visit : 127.0.0.1:8000/


####Data Collection & Analysis
* Python
* Eventful API 
* Google Maps API 
* Open Weather API 

####Front End and Visualisations
* HTML,CSS, JavaScript 
* Plotly.js 
* Google Maps API 

####FrameWork used
* Django  (DB - Sqlite3) 

###DATA ANALYSIS
Score = (0.25 * distanceScore + 0.75 * #likes + #comments + 2 * #images + 1.5 * #links) * (weatherScore / 2) <br/>
WeatherScore:  if ((maxtmp > 35) or (mintmp < 25) ) then return "1"   else return “2” <br/>
distanceScore : (distance_in_km – distance_loc)* 100 / distance_in_km <br/>
