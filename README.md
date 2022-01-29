# Surfs_up      Module 9

## Cheryl Berger

### Deliverable 3: A written report for the statistical analysis (20 points)

### Deliverable 3 Instructions
#### For this part of the Challenge, write a report that describes the key differences in weather between June and December and two recommendations for further analysis.

##### The analysis should contain the following:
### 1.	Overview of the analysis: Explain the purpose of this analysis.
W. Avy is interested in the weather temperatures during the year in Ohau so that he knows when to open his ice cream shop.  He has asked XXX to compare temperatures in the summer to the winter temperatures.  Using the the recent weather data found in file Hawaiii.sqlite https://github.com/cherylberger/Surfs_up/commit/56f426f175677560eba267b43b0a7858cbc551ce, the weather for the months of June and December will be queried and organized for comparison.  The three key differences in the weather results will be highlighted for W. Avy's consideration.  A summary of the results will be provided along with recommendations for aditional analysis. 

### 2.	Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.

Using Python, Pandas functions and methods, and SQLAlchemy, filter the column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of June. Load all dependencies and import the required functions as displayed in the code block from file (Filename). 

![image](https://user-images.githubusercontent.com/94234511/151652230-b1577202-8252-457b-a806-072910b02c20.png)

### Determine the Summary Statistics for the month of June

#### Run the query
![image](https://user-images.githubusercontent.com/94234511/151652256-41935932-67c9-458a-bf64-c474fe491d08.png)

#### Make a list
![image](https://user-images.githubusercontent.com/94234511/151652299-e988d0ea-1b1d-4dbb-8432-4d4a59a45d14.png)

#### create the dataFrame
![image](https://user-images.githubusercontent.com/94234511/151652322-94f576af-b11a-4676-bef7-3cfc2ab29c8f.png


#### Calculate the summary statistics
![image](https://user-images.githubusercontent.com/94234511/151652333-23eb4565-6cf0-453f-8c5b-5bbb1a45c705.png)

#### Plot the data
![image](https://user-images.githubusercontent.com/94234511/151652344-a9ce6448-a123-4b5e-b47b-3a0f513b23f0.png)

### Determine the Summary Statistics for the month of December

Using Python, Pandas functions and methods, and SQLAlchemy, you’ll filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December. Load all dependencies and import the required functions as displayed in the code block from file (Filename).

#### Run the query
![image](https://user-images.githubusercontent.com/94234511/151652520-f5bfac51-0f3a-415c-b444-e3e613138f1c.png)

#### Make a list
![image](https://user-images.githubusercontent.com/94234511/151652534-a59b8813-39ac-49de-be4c-f7b8f075d910.png)

#### Create the DataFrame
![image](https://user-images.githubusercontent.com/94234511/151652547-4736bc2d-3f5b-461b-8c7d-33250efbc9af.png)

#### Calculate the Summary Statistics
![image](https://user-images.githubusercontent.com/94234511/151652569-b8300c0c-3e98-41fd-a8c9-0f0da55571cd.png)

#### Plot the data
![image](https://user-images.githubusercontent.com/94234511/151652583-e58972dd-f7fb-4dd4-9433-85fbe28161ff.png)

### Key Difference #1:  

The average temperatures are X in June and Y in December, with June temperatures averaging X% higher than December.


### Key Difference #2:  The lowest temperature observed in December was XF compared to XF in June, however the spread is X for June and Y for Dec indicating_________



### Key Differnece #3:  Less data points in the December results XXX compared to YYYY.  



### 3.	Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

##### High Level Summary

##### Additional Query 1  Gather precipitation results for each month

##### Additional Query 2  Compare temperatures from each weather station to determine if location on the Island impacts either the temperature or the amount of precipitation.



#### Deliverable 3 Requirements

##### Structure, Organization, and Formatting (6 points)

###### The written analysis has the following structure, organization, and formatting:
##### •	There is a title, and there are multiple sections. (2 pt)
##### •	Each section has a heading and subheading. (2 pt)
##### •	Links to images are working and displayed correctly. (2 pt)

#### Analysis (14 points)
###### The written analysis has the following:

##### 1.	Overview of the statistical analysis:
###### o	The purpose of the analysis is well defined. (3 pt)

#### 2.	Results:
##### o	There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)

#### 3.	Summary:
##### o	There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)
