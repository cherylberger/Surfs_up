# Surfs_up      Module 9

### Cheryl Berger

## 1.	Overview of the Surfs_Up Analysis
W. Avy is interested in the weather temperatures during the year in Ohau so that he knows when to open his ice cream shop.  He has asked XXX to compare temperatures in the summer to the winter temperatures to determine if it would be lucrative to reamain open all year long.  Using the the recent weather data found in file Hawaiii.sqlite https://github.com/cherylberger/Surfs_up/commit/56f426f175677560eba267b43b0a7858cbc551ce, the weather for the months of June and December will be queried and organized for comparison.  Three key differences in the weather results will be highlighted for W. Avy's consideration.  A summary of the results will be provided along with recommendations for additional analysis. 

## 2.	Surfs_Up Analysis and Results: 

### 2a. Connect to the Database and gather tools and methods to perfom the analysis
        
Using Python, Pandas functions and methods, and SQLAlchemy, filter the column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures           for the month of June. Load all dependencies and import the required functions as displayed in the code block from file https://github.com/cherylberger/Surfs_up/blob/main/SurfsUp_Challenge.ipynb. Create the base engine to connect Python to the database and reflect the Measurement table to ensure the connection has been made. 

![image](https://user-images.githubusercontent.com/94234511/151652230-b1577202-8252-457b-a806-072910b02c20.png)

### 2b. Determine the Summary Statistics for the month of June

#### Run the query that filters the Measurement table and collects the temperature values for the month of June
![image](https://user-images.githubusercontent.com/94234511/151652256-41935932-67c9-458a-bf64-c474fe491d08.png)

#### Make a list of the June temperatures
![image](https://user-images.githubusercontent.com/94234511/151652299-e988d0ea-1b1d-4dbb-8432-4d4a59a45d14.png)

#### Create a Pandas DataFrame to store the temperature data for June from 2010 to 2019
![image](https://user-images.githubusercontent.com/94234511/151688984-512ade21-983a-4cfb-bdbc-30bd06c6a449.png)

#### Calculate the summary statistics using the DataFrame created for the June query results. 
![image](https://user-images.githubusercontent.com/94234511/151652333-23eb4565-6cf0-453f-8c5b-5bbb1a45c705.png)

#### Plot the data to better visualize the outcome of the analysis
![image](https://user-images.githubusercontent.com/94234511/151652344-a9ce6448-a123-4b5e-b47b-3a0f513b23f0.png)


### 2c. Determine the Summary Statistics for the month of December

Using Python, Pandas functions and methods, and SQLAlchemy, you’ll filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the             temperatures for the month of December. The dependencies were loaded in Step 1 before analyzing the Juen results, the same dependencies and functions will be needed             again for the analysis of the December data.  The code detailed below was added to new code blocks in                         https://github.com/cherylberger/Surfs_up/blob/main/SurfsUp_Challenge.ipynb.

#### Run the query that that filters the Measurement table and collects the temperature values for the month of December
![image](https://user-images.githubusercontent.com/94234511/151652520-f5bfac51-0f3a-415c-b444-e3e613138f1c.png)
     
 #### Make a list of the December temperatures
![image](https://user-images.githubusercontent.com/94234511/151652534-a59b8813-39ac-49de-be4c-f7b8f075d910.png)

 #### Create a Pandas DataFrame to store the temperature data for December from 2010 to 2019
 ![image](https://user-images.githubusercontent.com/94234511/151652547-4736bc2d-3f5b-461b-8c7d-33250efbc9af.png)

 #### Calculate the Summary Statistics using the DataFrame create for the December temperature results
 ![image](https://user-images.githubusercontent.com/94234511/151652569-b8300c0c-3e98-41fd-a8c9-0f0da55571cd.png)

 #### Plot the data tp better visualize te outcome of the analysis
 ![image](https://user-images.githubusercontent.com/94234511/151652583-e58972dd-f7fb-4dd4-9433-85fbe28161ff.png)

### Summary of Key Differences 

####    #1:  Average Temperatures June vs December

The average temperatures measured 74.9F in June and 72.0F in December, with June temperatures averaging approximately 7% higher than December. The data appears normally distributed and largely centralized around the mean for both June and December.  A comparison of the results using a histogram shows that during both June and December, the mean and mode are near in both datasets. 

#####    Comparison of Summary Statistics
https://github.com/cherylberger/Surfs_up/blob/main/Avg_temps_June_Dec.png

####    #2:  Range of Temperatures June vs December
    
The lowest temperature observed in December was 56F compared to 64F in June. Interestingly, the maximum temperature in June was 85F compared to 83F in December, clearly there are still very warm days in December in Oahu, Hawaii!  

 
####    #3:  Sample size by Month
    
There were less data points in the December results, a total n=1517 compared to n=1700 for June. The reason for the missing data is not clear from the results but is not likey to impact the overall conclusions as the data is well behaved.    


## 3.	Summary of the Surfs_Up Analysis: 

### High Level Summary
Based on the temperature analysis, the average temperatures are above 70F in both June and December and the difference in average temperatures is less than 10%.  Although there may be some cooler days in December, observed temperatures would not be expected to dip below the statistical average +/- 3 st.dev or rougly 62F during the month of December based on historical data.  Based on the assumption that average daily temperatures for Juen and December are predictive of the weather year-round and that warm temperatures are better for the ice createm businees, the results of the analysis suggest that keeping the ice cream stand open year round would be profitable.   
   
### Additional Query 1  
Although temperatures may be pleasant for most or all of the calendar year in Oahu; it would be useful to gather precipitation results for each month of the year and determine if there are trends in precipitation amounts during year.  Although storms are not alwaya predicatable, most geographic regions have similar weather patterns from year to year.  Rainy months or series of months were high ampunts of precipition are observed may preclude visits to the beach and/or influence the typical beach-goers desire for ice cream.  It may be useful to conduct research on operating schedules for similar business on the Island before finalizing the annual operating plans for the new ice cream shop.   

### Additional Query 2  
Compare temperatures from each weather station to determine if location on the Island impacts either the temperature or the amount of precipitation.
Also look for trends across the entire dataset, were their storms or other events that impacted the weather in Oahu? 

