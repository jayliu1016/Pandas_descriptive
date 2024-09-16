# Data
# Source:
# It is a survey conducted by Integrated Public Use Microdata Series (IPUMS), allifiated with University of Minnesota in 2019.

# Variables & Sample Restrictions:
# We have included four variables: SEX, AGE, RACE, and INCWAGE. We then deleted any entries with no income values. Notes: For sex, 1 represents male, 2 represents female. For age, the numerical value symbolizes the actual age of the surveyed individual(we have excluded people under 18 since they should not be llegaly hired. For example, an entry of 29 means the surveyed individual is 29 years of age, and and entry of 63 means the surveyed indivudal is 58 years of age. For race, 1 = White, 2=Black/African American, 3=American Indian or Alaska Native, 4=Chinese, 5=Japanese, 6=Other Asian or Pacific Islander, 7=Other race, nec, 8=Two major races, 9=Three or more major races. For income and wages, we have excluded 0 which means either retired or unemployed, 999999 means N/A, and 999998 means missing values.


import pandas as pd
import matplotlib.pyplot as plt

# Import the CSV to reset the DataFrame
data_cpi_combined_steps = pd.read_csv("usa_00004.csv")

# Remove the 'RACED' column
data_cpi_combined_steps.drop("RACED", axis=1, inplace=True)

# Filter out rows where 'INCWAGE' is 0, 999999, or 999998
excluded_values = [0, 999999, 999998]
data_cpi_filtered_combined = data_cpi_combined_steps[
    ~data_cpi_combined_steps["INCWAGE"].isin(excluded_values)
]

# Keep rows where 'AGE' is between 18 and 65
data_cpi_age_filtered = data_cpi_filtered_combined[
    (data_cpi_filtered_combined["AGE"] >= 18)
    & (data_cpi_filtered_combined["AGE"] <= 65)
]

# Recode 'SEX' to 'male' and 'female'
sex_mapping = {1: "Male", 2: "Female"}
data_cpi_age_filtered["SEX"] = data_cpi_age_filtered["SEX"].map(sex_mapping)

# Create dummy variables
data_cpi_age_filtered["Male"] = data_cpi_age_filtered["SEX"].apply(
    lambda x: 1 if x == "Male" else 0
)
data_cpi_age_filtered["White"] = data_cpi_age_filtered["RACE"].apply(
    lambda x: 1 if x == 1 else 0
)
data_cpi_age_filtered["Black"] = data_cpi_age_filtered["RACE"].apply(
    lambda x: 1 if x == 2 else 0
)
data_cpi_age_filtered["Other_Races"] = data_cpi_age_filtered["RACE"].apply(
    lambda x: 1 if x == 3 else 0
)

# Drop the original 'SEX' and 'RACE' columns as they're replaced by dummy variables.
data_cpi_age_filtered.drop(["SEX", "RACE"], axis=1, inplace=True)

# Using the aggregate function to create a summary table with multiple statistics
summary_table = data_cpi_age_filtered.agg(
    {
        "Male": ["mean", "median", "std", "min", "max"],
        "White": ["mean", "median", "std", "min", "max"],
        "Black": ["mean", "median", "std", "min", "max"],
        "Other_Races": ["mean", "median", "std", "min", "max"],
        "INCWAGE": ["mean", "median", "std", "min", "max"],
        "AGE": ["mean", "median", "std", "min", "max"],
    }
).round(2)

# Display the summary table
print(summary_table)

# Describe what you see in your summary statistics table in words and comment on any trend/pattern
# In our summary statistics table, we summarized six different variables by calculating the mean, standard deviation, minimum, and maximum values for “Male”, “White”, “Black”, “Other Races”, “INCWAGE”, “AGE”. For the purpose of this table, we summarized each of these variables only for men.

# MALE
# When viewing this table, it is important to note that of the data collected, 52% of the population is men. Therefore, 48% of the population analyzed in this project is women. This data is relatively equal for both groups and provides a balanced representation of the overall population. However, it's crucial to take a deeper dive to ensure comprehensive analysis and address any potential disparities that may exist.

# WHITE, BLACK, OTHER RACES
# According to this data, 77% of the male population is White, 9% are Black, and 1% are other races. The standard deviation for the proportion of White males in the population is 0.42, thus indicating that the data points are relatively close to the mean of 0.77. This suggests less variability in the proportion of White males in comparison to the mean.

# The standard deviation for the proportion of Black males in the population is 0.29. Similar to the White male population, this value suggests that the data points are relatively close to the mean of 0.09, demonstrating less variability in the proportion of Black males in comparison to the mean.

# The standard deviation for the proportion of males from other racial groups is 0.09. Similar to White and Black males, these values suggest that the data points are relatively close to the mean of 0.01, indicating less variability in the proportion of males from other racial groups in comparison to the mean.

# INCWAGE
# The mean wage for men was 55,650.02 USD and the standard deviation is 67,463.87 USD, indicating that the data distribution is very spread out but not normally distributed.

# AGE
# The mean age in this sample of males is 41.42 years. The standard deviation for age shows how much individual ages in this population deviate from the mean age. In the case of this data, the standard deviation for age is 13.60 years, showing that, on average, individual ages in the data set deviate from the mean age by 13.60 years.
## The summary statistics table above provides an overview of the variables:
data_cpi_combined_steps.info()

# Load the CSV file
data_cpi_combined_steps = pd.read_csv(
    "/Users/liuliangcheng/Desktop/Duke/DE/usa_00004.csv"
)

# Remove the 'RACED' column
data_cpi_combined_steps.drop("RACED", axis=1, inplace=True)

# Filter out rows where 'INCWAGE' is 0, 999999, or 999998
excluded_values = [0, 999999, 999998]
data_cpi_filtered_combined = data_cpi_combined_steps[
    ~data_cpi_combined_steps["INCWAGE"].isin(excluded_values)
]

# Keep rows where 'AGE' is between 18 and 65
data_cpi_age_filtered = data_cpi_filtered_combined[
    (data_cpi_filtered_combined["AGE"] >= 18)
    & (data_cpi_filtered_combined["AGE"] <= 65)
]

# Map the 'RACE' to new groupings
race_mapping = {1: 1, 2: 2, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3}
data_cpi_age_filtered["RACE"] = data_cpi_age_filtered["RACE"].map(race_mapping)

# Calculate the proportion of each sex
sex_counts = data_cpi_age_filtered["SEX"].value_counts(normalize=True)

# Recode 'SEX' to 'male' and 'female'
sex_mapping = {1: "Male", 2: "Female"}
data_cpi_age_filtered["SEX"] = data_cpi_age_filtered["SEX"].map(sex_mapping)


mean_income_by_gender = data_cpi_age_filtered.groupby("SEX")["INCWAGE"].mean().round(2)
# Calculate mean income by gender and race
mean_income_by_gender_race = (
    data_cpi_age_filtered.groupby(["RACE", "SEX"])["INCWAGE"].mean().round(2).unstack()
)

# Recode 'RACE' to readable categories, assuming 'race_mapping' is defined as before
race_names = {1: "White", 2: "Black/African American", 3: "Other"}
mean_income_by_gender_race.rename(index=race_names, inplace=True)


# Re-plotting the first graph with the mean income values annotated on top of the bars
plt.figure(figsize=(10, 6))
ax1 = mean_income_by_gender.plot(kind="bar", color=["pink", "blue"])
plt.title("Mean Income by Gender")
plt.xlabel("Gender")
plt.ylabel("Mean Income")
plt.xticks(rotation=0)

# Annotate with the mean income values
for p in ax1.patches:
    ax1.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.tight_layout()
plt.show()

# Re-plotting the second graph with the mean income values annotated on top of the bars
plt.figure(figsize=(10, 6))
ax2 = mean_income_by_gender_race.plot(kind="bar", color=["pink", "blue"])
plt.title("Mean Income by Gender and Race")
plt.xlabel("Race")
plt.ylabel("Mean Income")
plt.xticks(rotation=0)
plt.legend(title="Gender")

# Annotate with the mean income values
for p in ax2.patches:
    ax2.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.tight_layout()
plt.show()

# Describe your two plots in words and comment on the trend/pattern
# We first started by comparing mean income by gender in the United States of America in 2019. We plotted the mean income on the y-axis and gender on the x-axis. When looking at this graph, there is a clear difference between the mean income for women versus the mean income for men. For women, the mean income in 2019 was 44,742.77 USD whereas for men, it was 65,943.74 USD. This data displays over a 20,000 dollar difference between the two genders listed.

# In our second graph, we analyzed mean income by race and gender, plotting mean income on the y-axis and race on the x-axis, and using pink and blue to denote the two genders in question on the legend. We grouped our data by “White”, “Black/African American”, and “Other”. For each of the three race groups listed above, the median income was higher for men than women. In some cases, there was a significant difference. For example, there was a 23,689.93 dollar difference between and white men and women, whereas for Black men and women, there was a $4,509.81 difference. The group “Other” includes “American Indian or Alaska Native”, “Chinese”, “Japanese”, “Other Asian or Pacific Islander”, “Other race”, “Three or more major races”, and “Two major races”. This group displayed a 15,821.73 dollar difference in the wages between males and females.

# Overall, our data analysis matched our prediction that the higher median income would be higher for males than females. Given prevailing socio-economic norms and historical disparities, the highest mean income tends to skew towards males due to systemic factors such as gender wage gaps and cultural biases favoring male earning potential. This expectation is rooted in empirical evidence reflecting a pattern of males occupying higher-paying positions and enjoying greater advancement opportunities within various professional atmospheres. Consequently, disparities in median income between genders persist, with males typically commanding higher earnings at the upper levels of the income distribution.

# Additionally, it’s important to acknowledge that the disparities in income extend beyond economic data. It reflects systemic injustices that are deeply ingrained in our society, further exacerbating cycles of inequality and limiting the ability of marginalized communities to advance socioeconomically. Other factors such as education level and access to healthcare further exacerbate these disparities, further compounding these systemic issues.
