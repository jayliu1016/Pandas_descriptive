import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestMain(unittest.TestCase):
    
    def setUp(self):
        # Load the actual CSV file
        self.df = pd.read_csv('usa_00004.csv')
    
    def test_filter_income(self):
        # Test filtering out rows with INCWAGE = 0, 999999, or 999998
        excluded_values = [0, 999999, 999998]
        filtered_df = self.df[~self.df['INCWAGE'].isin(excluded_values)]
        self.assertEqual(len(filtered_df), 1590418) 
    
    def test_filter_age(self):
        # Test keeping rows where AGE is between 18 and 65
        age_filtered_df = self.df[(self.df['AGE'] >= 18) & (self.df['AGE'] <= 65)]
        self.assertEqual(len(age_filtered_df), 1968849) 

    def test_recode_sex(self):
        # Test recoding 'SEX' to 'Male' and 'Female'
        sex_mapping = {1: 'Male', 2: 'Female'}
        self.df['SEX'] = self.df['SEX'].map(sex_mapping)
        self.assertEqual(self.df['SEX'].iloc[0], 'Male')
        self.assertEqual(self.df['SEX'].iloc[1], 'Female')

    def test_dummy_variables(self):
        # Test creating dummy variables for 'Male' and 'White'
        self.df['SEX'] = self.df['SEX'].map({1: 'Male', 2: 'Female'})
        self.df['Male'] = self.df['SEX'].apply(lambda x: 1 if x == 'Male' else 0)
        self.df['White'] = self.df['RACE'].apply(lambda x: 1 if x == 1 else 0)
        
        self.assertEqual(self.df['Male'].sum(), 1588332)
        self.assertEqual(self.df['White'].sum(), 2501187)

    def test_summary_statistics(self):
        # Test generation of summary statistics for columns
        self.df['Male'] = self.df['SEX'].apply(lambda x: 1 if x == 'Male' else 0)
        self.df['White'] = self.df['RACE'].apply(lambda x: 1 if x == 1 else 0)
        
        summary_table = self.df.agg({
            'Male': ['mean', 'median','std', 'min', 'max'],
            'White': ['mean', 'median','std', 'min', 'max'],
            'INCWAGE': ['mean','median', 'std', 'min', 'max'],
            'AGE': ['mean', 'median','std', 'min', 'max']
        }).round(2)
        
        # Test if summary statistics are correct
        self.assertAlmostEqual(summary_table['White']['mean'], 0.77, places=2)

    def test_plot_income_by_gender(self):
        # Test if the plot for income by gender works
        self.df['SEX'] = self.df['SEX'].map({1: 'Male', 2: 'Female'})
        mean_income_by_gender = self.df.groupby('SEX')['INCWAGE'].mean()
        
        # Ensure the plot doesn't raise any exceptions
        plt.figure()
        ax = mean_income_by_gender.plot(kind='bar')
        plt.close()
        self.assertIsNotNone(ax)

    def test_plot_income_by_gender_and_race(self):
        # Test if the plot for income by gender and race works
        self.df['SEX'] = self.df['SEX'].map({1: 'Male', 2: 'Female'})
        mean_income_by_gender_race = self.df.groupby(['RACE', 'SEX'])['INCWAGE'].mean().unstack()
        
        # Ensure the plot doesn't raise any exceptions
        plt.figure()
        ax = mean_income_by_gender_race.plot(kind='bar')
        plt.close()
        self.assertIsNotNone(ax)

if __name__ == '__main__':
    unittest.main()
