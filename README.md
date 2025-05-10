# Boston Police Shooting Analysis
## Project Description
This project aims to analyze the death cases involved in police violence and shooting events in Boston, where the data is acquired from Fatal Force Database from Washington Post. More specifically, this project investigates the distribution of victims over different gender, age, and race groups. In addition, I studied the relationship between these demographic information and the likelyhood people got involved in police shooting events. The end product is a collection of bar charts that show the distribution of victims over different gender, age, and races, allowing analysis to be done to understand the characteristics of population that have higher chance of involving in police shooting events.

## Result Visualizations
- Figure 1

![DS 2001 final pic 1](https://github.com/user-attachments/assets/c9e7e1e7-c9e4-48f4-b4ed-8dccc04fe738)
- Figure 2

![DS 2001 final pic 2](https://github.com/user-attachments/assets/b53c6341-b3fa-4ff9-b411-5cf93b0f272c)
- Figure 3

![DS 2001 final pic 3](https://github.com/user-attachments/assets/b22f3781-4628-49e4-8465-5fd1ad88f512)

## How to Install and Run the Website
### Dependencies:
  - matplotlib >= 3.9.2
  - csv >= 3.12.3

### Instructions:
  1. Make sure all libraries in the above dependency list are installed to your current working environment
  2. Download the tsv and py files, which are the dataset and python file
  3. Run the Police_shooting_analysis.py file to process the data and generate the 3 bar charts

### Troubleshooting:
  - If there's error reading the tsv file, make sure its in the same directory as you py file, and its name isn't modified after downloaded
  - If there's error with the libraries used, make sure they're all properly installed to your current environment, and the version are the same or newer than the versions in the dependency list

## How to Use
### Using the py File:
The file reads and process the data in its first two functions, where a nested list is used to store data with each line/inner list being one victim's record. For data cleaning, records with missing or incomplete demographic information are removed. If you want to read and process the data in another approach, such as using pandas data frame to store the data and change the symbol of gender or race, then you're welcomed to modify the functions on your end to achieve these purposes. Functions 3 to 5 find the distribution of victims over different age, gender, and race by splitting the victims into different categories. For example, victims are splitted into two groups for gender since there are male and female. The same process is done for age and race groups as well. If you want to categorized victims in another way or based on other demographic information, feel free to adjust the code to do that. Finally, a class and function is used to generate plots using matplotlib, and if you want to use seaborn or plotly to make your plots, remember to install and import them on top of the file since these libraries aren't included in mine.

### Interpreting the Visualizations:
Figure 1 shows the percentage distribution of deaths from police shooting in five different age groups. The group with the highest death percentage is the age of 25 - 40 with 47.6%, and the second highest is the age of 40 - 65 with 32.8%. The groups with the lowest percentage is the age under 18 (1.8%) and above 65 (2.9%). Figure 1 implies that while younger adults are more often to get involved in police shootings, children and elders are much less likely for this danger perhaps due to their inconvinience or inability to move around without family's or other's supervision. Figure 2 shows the percentage dstribution of deaths in two different genders, where male accounts for 99.5% of deaths and female accounts for only 0.5%. This implies that men are more likely to be involved and killed in police shooting events compared to women, which agrees with many other studies and statistics online. Figure 3 shows the percentage distribution of deaths in five different age groups. The race with the highest death percentage is white with 49.5%, followed by black with 26.4% and hispanic with 18.4%. The two lowest groups are native Americans with 1.5% and Asians with 1.8%. The reason why white people account for almost half of the death cases is because white is the dominating race as 59.3% of the US population is white as of 2021. However, although black people only account for 13% of the US population as of 2021, they account for 26.4% of the death cases under police shooting, which is twice the percentage of their population. If we assume the distribution of races in the dataset is similar to that of the US population, then black people are actually twice as likely than white people to be shot and killed due to police shooting. Overall, these 3 bar charts allows user to visually see the distribution of victims under police shooting across different age, gender, and race groups, as well as analyzing the key characteristics of the population that has the highest death percentage from the dataset.

## Analysis You Can Do Using This Plots
- Which age group has the highest death rate?
- Which race group has the lowest death rate?
- Are male more likely than female to get involved in police shooting events, or is it the other way around?
- What's the population characteristics in terms of race, age, and gender that results in the highest death rate from police shooting events?

## Contributors
1. Kuan-Chun Chiu (Myself) - beagledirk1@gmail.com
