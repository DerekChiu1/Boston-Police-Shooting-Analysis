# Course: DS 2001 Programming Practicum
# Name: Derek Chiu
# Due date: 12/01/2023

"""
Program: Finding the correlation between victims' gender/age/race and their 
likelyhood to die from police shooting

"""

"""
Project title: Police violence & shooting dataset analysis
    
File used: fatal-police-shootings.tsv

Death factors to look into: Gender, age, race of the victim
    
Research question: What's the correlation between victims' gender/age/race
and their likelihood to die from police shooting
    
Analysis:
- Among the races of white, black, native american, asian, and hispanic,
  which race group is more often killed from police shooting?
  
- Whether men or women are more often killed from police shooting?

- Among age groups of teen, young adult, middle age, and elderly, 
  which age group is more often killed from police shooting? 

Real world application:
- Is there one race, gender, or age group being more likely to be killed from
  police shooting?

- Does the result above agreee or conflict with the trend found in graphs based
  on data in the fatal-police-shootings.tsv file?

"""

import csv
import matplotlib.pyplot as plt

def read_file():
    file_name = "fatal-police-shootings.tsv"
    with open(file_name, "r", encoding = "utf-8") as police_file:
        all_victims = []
        police_reader = csv.reader(police_file, delimiter = "\t")
        for line_num, line in enumerate(police_reader):
            if line_num == 0:
                continue
            line = line[1:]
            for item in line:
                item = item.strip()
            all_victims.append(line)
    return all_victims

def cleaning_data(all_victims):
    race_symbol = ["W", "B", "N", "A", "H"]
    gender_symbol = ["M", "W"]
    age_list = []
    for victim in all_victims:
        age = int(victim[4])
        age_list.append(age)
    max_age = max(age_list)
    min_age = min(age_list)
    for victim in all_victims:
        age = int(victim[4])
        gender = victim[5]
        race = victim[6]
        if gender in gender_symbol and race in race_symbol and \
            age in range(min_age, max_age + 1):
            continue
        else:
            all_victims.remove(victim)
    return all_victims
         
def find_age_dist(all_victims):
    teens, young_adults, older_adults, middle_age, elderlies = [], [], [], [], []
    for victim in all_victims:
        age = int(victim[4])
        if age < 18:
            teens.append(victim)
        elif 18 <= age < 25:
            young_adults.append(victim)
        elif 25 <= age < 40:
            older_adults.append(victim)
        elif 40 <= age < 65:
            middle_age.append(victim)
        elif age >= 65:
            elderlies.append(victim)
    all_ages = {}
    all_values = [teens, young_adults, older_adults, middle_age, elderlies]
    all_keys = ["Under 18", "18-25", "25-40", "40-65", "above 65"]
    for key in range(len(all_keys)):
        all_ages[all_keys[key]] = all_values[key]
    return all_ages

def find_gender_dist(all_victims):
    men, women = [],[]
    for victim in all_victims:
        gender = victim[5]
        if gender == "M":
            men.append(victim)
        else:
            women.append(victim)
    all_genders = {}
    all_values = [men, women]
    all_keys = ["men", "women"]
    for key in range(len(all_keys)):
        all_genders[all_keys[key]] = all_values[key]
    return all_genders
        
def find_race_dist(all_victims):
    white, black, native_american, asian, hispanic = [], [], [], [], []
    for victim in all_victims:
        race = victim[6]
        if race == "W":
            white.append(victim)
        elif race == "B":
            black.append(victim)
        elif race == "N":
            native_american.append(victim)
        elif race == "A":
            asian.append(victim)
        elif race == "H":
            hispanic.append(victim)
    all_races = {}
    all_values = [white, black, native_american, asian, hispanic]
    all_keys = ["white", "black", "native american", "asian", "hispanic"]
    for key in range(len(all_keys)):
        all_races[all_keys[key]] = all_values[key]
    return all_races

class Victims():
    def __init__(self, all_victims, factor):
        self.total_num = len(all_victims)
        self.factor_values = list(factor.values())
        self.factor_keys = list(factor.keys())

    def find_percentages(self):
        percentage_list = []
        for value in self.factor_values:
            percentage = round((len(value) / self.total_num) * 100, 1)
            percentage_list.append(percentage)
        return percentage_list

    def plot_3_factors(self, percentage_list, factor_name):
        x_axis = self.factor_keys
        plt.title("""Percentage distribution of death resulted from police
shooting of different {}\n""".format(factor_name))
        plt.xlabel(factor_name)
        plt.ylabel("Percentage")
        plt.ylim(0, 100)
        plt.bar(x_axis, percentage_list, color = "brown")
        return None

def making_plots(all_victims, all_ages, all_genders, all_races):
    age_plot = Victims(all_victims, all_ages)
    gender_plot = Victims(all_victims, all_genders)
    race_plot = Victims(all_victims, all_races)
    plots = [age_plot, gender_plot, race_plot]
    all_names = ["ages", "genders", "races"]
    for plot in plots:
        if plot == age_plot:
            name = all_names[0]
        elif plot == gender_plot:
            name = all_names[1]
        elif plot == race_plot:
            name = all_names[2]
        percentage_list = plot.find_percentages()
        plot.plot_3_factors(percentage_list, name)
        plt.show()
    return_statement = "The bar graphs, of the correlation between victim's age/gender/race and \
their likelyhood to die from police shooting, are plotted above."
    return return_statement

def main():
    all_victims = read_file()
    all_victims = cleaning_data(all_victims)
    all_ages, all_genders, all_races = find_age_dist(all_victims), \
        find_gender_dist(all_victims), find_race_dist(all_victims)
    plots = making_plots(all_victims, all_ages, all_genders, all_races)
    return plots
    
if __name__ == "__main__":
    print (main())