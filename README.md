# g100-restaurants-during-covid
This analysis studies the impact of COVID on restaurants. Using Small Businesses Adminsitration data about Payroll Protection Program Freedom of Information Act data, I visualized and graphed it for restaurants -- one of the industries hardest hit by the COVID-19 pandemic--across multiple dimensions.

The Paycheck Protection Program (PPP) is a forgivable loan which is designed to support sole proprietors, independent contractors and self-employed, private non-profits and 501(c)(19) veterans organizations. It functions as an incentive to maintain workers on the payroll during the pandemic. The program is ongoing until May 31, 2021.

The scripts should be run in order of 1create.py , 2polish.py , 3analyze_resto_loans.py , 4resto_viz_corr.py, 5loanspercapita.py, and 6heatmap.

I used the North American Industry Classification System (NAICS) Codes to filter the data for restaurants. Their classifications can be found below. Greater detail about what makes up each sector can be found here: https://www.census.gov/naics/?input=72&year=2017&details=722. 
             
             722110: Full-Service Restaurants
             722211: Limited-Service Restaurants
             722212: Cafeterias
             722213: Non-alcoholic Bars
             722310: Food Service Contractors
             722320: Caterers
             722330: Mobile Food Services
             722410: Bars

Inputs include: 
1) 12 CSV files from the Small Businesses Administration. Details for accessing them can be found below.
2) 2020 TIGER/Line® Shapefiles for State and equivalents. It is located here: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=States+%28and+equivalent%29
3) 2020 TIGER/Line® Shapefiles for ZIP Code Tabulation Areas. It is located here: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2020&layergroup=ZIP+Code+Tabulation+Areas

Outputs include: 
1) a graph which demonstrates the current approval amount of PPP loans for a restaurants;
2) a hex diagram that compares jobs reported and loan approval amount;
3) a detailed graphs about number of jobs reported by restaurants recieving loans;
4) a boxplot of money recieved by NAICS code;
5) a box plot of loan size and across gender of the loan recipients;
6) a graph across race of the loan recipients;
7) a bar graph for the top 10 and bottom 10 states;
8) a bar graph for the top 10 cities;
9) a bar graph of the top 20 states per capita for loan amount;
10) a bar graph of the top 10 cities per capita for loan amount;
11) a heatmap graph for NAICS code industry classification across the top 10 states for the Current Loan Amounts;
12) a heatmap graph for NAICS code industry classification across the top 10 cities for the Current Loan Amounts;
13) a map of loan amounts per state;
14) a map of loan amounts across New York State at the county level;
15) and a map of loan amounts across the zips.

In the map of loan amounts per state darker greeners recieved more money.

In the maps of the loan amounts across New York State at the county level and across all the zips the scale is dark green most to dark red least amount of PPP restaurant funding.

#The SBA data for this analysis is from May 2, 2021, 9:30 PM (UTC-04:00)
#It can be downloaded at https://data.sba.gov/dataset/ppp-foia.
#All 12 avaiable CSV files will be used.

As a researcher, my key takeaways and remaining questions are:
1) there is a huge range of loan size—who received the big money?
2) At first glance demographic data seems equitable but further analysis is necessary to confirm this. It could be overlaid with detailed ownership data.
3) NAICS Codes may not be the best classification system to understand the complexity of food. Cafeterias are an example; it is my belief that buffets and COVID-19 intense impact on them likely drove this number up.
4) I found per capita restaurant PPP funding to be surprising. Chicago was a big recipient.
5) Remaining questions for me include: How will rural restaurants fare? Did this protect jobs on payroll? Are there richer ways to analyze restaurants? How did geographically specific COVID restrictions impact the performance, profitability, and outcomes of these restaurants? How did local vs. non-local businesses fare?

Thanks for checking out my project! Eat local & cheers!
