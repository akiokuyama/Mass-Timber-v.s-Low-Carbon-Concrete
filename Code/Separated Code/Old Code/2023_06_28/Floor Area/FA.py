### Load neccesary package
import pandas as pd
import numpy as np

### Import FA related variables ###
# Read the CSV file
FA_variable = pd.read_csv('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/1st Research/Code/Separated Code/Input/Input variables.csv', skiprows=1)

# Assign values to variables
SF_LF_2018 = FA_variable['SF_LF_2018'][0]
MF_LF_2018 = FA_variable['MF_LF_2018'][0]
SF_LF_2020 = FA_variable['SF_LF_2020'][0]
MF_LF_2020 = FA_variable['MF_LF_2020'][0]
SF_LF_2040 = FA_variable['SF_LF_2040'][0]
MF_LF_2040 = FA_variable['MF_LF_2040'][0]
MR_MF_LF = FA_variable['MR_MF_LF'][0]
HR_MF_RC = FA_variable['HR_MF_RC'][0]
BAU_MT = FA_variable['BAU_MT'][0]
SC_MT_new_RCSF_to_MT = FA_variable['SC_MT_new_RCSF_to_MT'][0]
SC_MT_new_RCMF_to_MT = FA_variable['SC_MT_new_RCMF_to_MT'][0]
SC_AC_new_RCSF_to_AC = FA_variable['SC_AC_new_RCSF_to_AC'][0]
SC_AC_new_RCMF_to_AC = FA_variable['SC_AC_new_RCMF_to_AC'][0]

### Import Floor Area Data in 2018 ###
# Read the CSV file
FA_data_2018 = pd.read_csv('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/1st Research/Code/Separated Code/Input/Input Floor Area 2018.csv', skiprows=1)

# Assign values to cells
FA_data_2018['Total_FA_SF'] = FA_data_2018['N_SF'] * FA_data_2018['Avg_FA_SF']
FA_data_2018['Total_FA_MF'] = FA_data_2018['N_MF'] * FA_data_2018['Avg_FA_MF']
FA_data_2018['Total_FA_MRMF'] = FA_data_2018['Total_FA_MF'] * MF_LF_2018
FA_data_2018['Total_FA_HRMF'] = FA_data_2018['Total_FA_MF'] * (1-MF_LF_2018)
FA_data_2018['Conv_Total_FA_LFSF'] = FA_data_2018['Total_FA_SF'] * SF_LF_2018
FA_data_2018['Conv_Total_FA_RCSF'] = FA_data_2018['Total_FA_SF'] * (1-SF_LF_2018)
FA_data_2018['Conv_Total_FA_SF'] = FA_data_2018['Conv_Total_FA_LFSF'] + FA_data_2018['Conv_Total_FA_RCSF']
FA_data_2018['Conv_Total_FA_MF'] = FA_data_2018['Total_FA_MF']
FA_data_2018['Conv_Total_FA_MRMF'] = FA_data_2018['Conv_Total_FA_MF'] * MF_LF_2018
FA_data_2018['Conv_Total_FA_HRMF'] = FA_data_2018['Conv_Total_FA_MF'] * (1-MF_LF_2018)

### BAU 2020 ###
# Read the CSV file
FA_data_2020 = pd.read_csv('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/1st Research/Code/Separated Code/Input/Input Floor Area 2020.csv', skiprows=1)

# Assign values to cells
FA_data_2020['Total_FA_SF'] = FA_data_2020['N_SF'] * FA_data_2020['Avg_FA_SF']
FA_data_2020['Total_FA_MF'] = FA_data_2020['N_MF'] * FA_data_2020['Avg_FA_MF']
FA_data_2020['Total_FA_MRMF'] = FA_data_2020['Total_FA_MF'] * MF_LF_2018
FA_data_2020['Total_FA_HRMF'] = FA_data_2020['Total_FA_MF'] * (1-MF_LF_2018)
FA_data_2020['Conv_Total_FA_LFSF'] = FA_data_2018['Total_FA_SF'] * SF_LF_2018
FA_data_2020['Conv_Total_FA_RCSF'] = FA_data_2018['Total_FA_SF'] * (1-SF_LF_2018)
FA_data_2020['Conv_Total_FA_SF'] = FA_data_2020['Conv_Total_FA_LFSF'] + FA_data_2020['Conv_Total_FA_RCSF']
FA_data_2020['Conv_Total_FA_MF'] = FA_data_2018['Total_FA_MF']
FA_data_2020['Conv_Total_FA_MRMF'] = FA_data_2020['Conv_Total_FA_MF'] * MF_LF_2018
FA_data_2020['Conv_Total_FA_HRMF'] = FA_data_2020['Conv_Total_FA_MF'] * (1-MF_LF_2018)
FA_data_2020['Avg_FA_New_MF'] = ((FA_data_2020['N_MF'] * FA_data_2020['Avg_FA_MF']) - (FA_data_2018['N_MF'] * FA_data_2018['Avg_FA_MF'])) / (FA_data_2020['N_MF'] - FA_data_2018['N_MF'])
FA_data_2020['Total_FA_New_SF'] = (FA_data_2020['N_SF'] - FA_data_2018['N_SF']) * FA_data_2020['Avg_FA_New_SF']
FA_data_2020['Total_FA_New_SF_LF'] = FA_data_2020['Total_FA_New_SF'] * SF_LF_2020
FA_data_2020['Total_FA_New_SF_RC'] = FA_data_2020['Total_FA_New_SF'] * (1-SF_LF_2020)
FA_data_2020['Total_FA_New_MF'] = (FA_data_2020['N_MF'] - FA_data_2018['N_MF']) * FA_data_2020['Avg_FA_New_MF']
FA_data_2020['Total_FA_New_MF_LF'] = FA_data_2020['Total_FA_New_MF'] * MF_LF_2020
FA_data_2020['Total_FA_New_MF_RC'] = FA_data_2020['Total_FA_New_MF'] * (1-MF_LF_2020)
FA_data_2020['Conv_Total_FA_New_LFSF'] = FA_data_2020['Total_FA_New_SF'] * SF_LF_2018
FA_data_2020['Conv_Total_FA_New_RCSF'] = FA_data_2020['Total_FA_New_SF'] * (1-SF_LF_2018)
FA_data_2020['Conv_Total_FA_New_SF'] =FA_data_2020['Conv_Total_FA_New_LFSF'] + FA_data_2020['Conv_Total_FA_New_RCSF']
FA_data_2020['Conv_Total_FA_New_LFSF'] =FA_data_2020['Total_FA_New_SF_LF']
FA_data_2020['Conv_Total_FA_New_RCSF'] =FA_data_2020['Total_FA_New_SF_RC']
FA_data_2020['Conv_Total_FA_New_MF'] = FA_data_2020['Total_FA_New_MF']
FA_data_2020['Conv_Total_FA_New_LFMF'] = FA_data_2020['Total_FA_New_MF_LF']
FA_data_2020['Conv_Total_FA_New_RCMF'] = FA_data_2020['Total_FA_New_MF_RC']
FA_data_2020['Total_FA_extended_SF'] = FA_data_2020['Total_FA_SF'] - FA_data_2020['Conv_Total_FA_SF'] - FA_data_2020['Conv_Total_FA_New_SF']
FA_data_2020['Total_FA_extended_LFSF'] = FA_data_2020['Total_FA_extended_SF'] * SF_LF_2018
FA_data_2020['Total_FA_extended_RCSF'] = FA_data_2020['Total_FA_extended_SF'] * (1-SF_LF_2018)
FA_data_2020['FA_new_LF'] = FA_data_2020['Conv_Total_FA_New_LFSF'] + FA_data_2020['Total_FA_New_MF_LF'] + FA_data_2020['Total_FA_extended_LFSF']
FA_data_2020['FA_new_RC'] = FA_data_2020['Conv_Total_FA_New_RCSF'] + FA_data_2020['Total_FA_New_MF_RC'] + FA_data_2020['Total_FA_extended_RCSF']
FA_data_2020['FA_new_MT'] = FA_data_2020['MT_Total_FA_SF&MF']
FA_data_2020['FA_new_AC'] = FA_data_2020['AC_Total_FA_SF&MF']


merged_df = pd.concat([FA_data_2018, FA_data_2020])

### Import FA data in 2040 ###
# Read the CSV file
FA_data_2040 = pd.read_csv('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/1st Research/Code/Separated Code/Input/Input Floor Area 2040.csv', skiprows=1)

# Assign values to cells
FA_data_2040['Total_FA_SF'] = FA_data_2040['N_SF'] * FA_data_2040['Avg_FA_SF']
FA_data_2040['Total_FA_MF'] = FA_data_2040['N_MF'] * FA_data_2040['Avg_FA_MF']
FA_data_2040['Total_FA_MRMF'] = FA_data_2040['Total_FA_MF'] * MF_LF_2018
FA_data_2040['Total_FA_HRMF'] = FA_data_2040['Total_FA_MF'] * (1-MF_LF_2018)
FA_data_2040['Conv_Total_FA_LFSF'] = FA_data_2018['Total_FA_SF'] * SF_LF_2018
FA_data_2040['Conv_Total_FA_RCSF'] = FA_data_2018['Total_FA_SF'] * (1-SF_LF_2018)
FA_data_2040['Conv_Total_FA_SF'] = FA_data_2040['Conv_Total_FA_LFSF'] + FA_data_2040['Conv_Total_FA_RCSF']
FA_data_2040['Conv_Total_FA_MF'] = FA_data_2018['Total_FA_MF']
FA_data_2040['Conv_Total_FA_MRMF'] = FA_data_2040['Conv_Total_FA_MF'] * MF_LF_2018
FA_data_2040['Conv_Total_FA_HRMF'] = FA_data_2040['Conv_Total_FA_MF'] * (1-MF_LF_2018)
FA_data_2040['Avg_FA_New_MF'] = ((FA_data_2040['N_MF'] * FA_data_2040['Avg_FA_MF']) - (FA_data_2018['N_MF'] * FA_data_2018['Avg_FA_MF'])) / (FA_data_2040['N_MF'] - FA_data_2018['N_MF'])
FA_data_2040['Total_FA_New_SF'] = (FA_data_2040['N_SF'] - FA_data_2018['N_SF']) * FA_data_2040['Avg_FA_New_SF']
FA_data_2040['Total_FA_New_SF_LF'] = FA_data_2040['Total_FA_New_SF'] * SF_LF_2040
FA_data_2040['Total_FA_New_SF_RC'] = FA_data_2040['Total_FA_New_SF'] * (1-SF_LF_2040)
FA_data_2040['Total_FA_New_MF'] = (FA_data_2040['N_MF'] - FA_data_2018['N_MF']) * FA_data_2040['Avg_FA_New_MF']
FA_data_2040['Total_FA_New_MF_LF'] = FA_data_2040['Total_FA_New_MF'] * MF_LF_2040
FA_data_2040['Total_FA_New_MF_RC'] = FA_data_2040['Total_FA_New_MF'] * (1-MF_LF_2040)
FA_data_2040['Conv_Total_FA_New_LFSF'] = FA_data_2040['Total_FA_New_SF'] * SF_LF_2018
FA_data_2040['Conv_Total_FA_New_RCSF'] = FA_data_2040['Total_FA_New_SF'] * (1-SF_LF_2018)
FA_data_2040['Conv_Total_FA_New_SF'] =FA_data_2040['Conv_Total_FA_New_LFSF'] + FA_data_2040['Conv_Total_FA_New_RCSF']
FA_data_2040['Conv_Total_FA_New_LFSF'] =FA_data_2040['Total_FA_New_SF_LF']
FA_data_2040['Conv_Total_FA_New_RCSF'] =FA_data_2040['Total_FA_New_SF_RC']
FA_data_2040['Conv_Total_FA_New_MF'] = FA_data_2040['Total_FA_New_MF']
FA_data_2040['Conv_Total_FA_New_LFMF'] = FA_data_2040['Total_FA_New_MF_LF']
FA_data_2040['Conv_Total_FA_New_RCMF'] = FA_data_2040['Total_FA_New_MF_RC']
FA_data_2040['Total_FA_extended_SF'] = FA_data_2040['Total_FA_SF'] - FA_data_2040['Conv_Total_FA_SF'] - FA_data_2040['Conv_Total_FA_New_SF']
FA_data_2040['Total_FA_extended_LFSF'] = FA_data_2040['Total_FA_extended_SF'] * SF_LF_2018
FA_data_2040['Total_FA_extended_RCSF'] = FA_data_2040['Total_FA_extended_SF'] * (1-SF_LF_2018)
FA_data_2040['FA_new_LF'] = FA_data_2040['Conv_Total_FA_New_LFSF'] + FA_data_2040['Total_FA_New_MF_LF'] + FA_data_2040['Total_FA_extended_LFSF']
FA_data_2040['FA_new_RC'] = FA_data_2040['Conv_Total_FA_New_RCSF'] + FA_data_2040['Total_FA_New_MF_RC'] + FA_data_2040['Total_FA_extended_RCSF']
FA_data_2040['FA_new_MT'] = FA_data_2040['MT_Total_FA_SF&MF']
FA_data_2040['FA_new_AC'] = FA_data_2040['AC_Total_FA_SF&MF']

# Merge Files
merged_df = pd.concat([merged_df, FA_data_2040])

### Mass-Timber ###
Mass_Timber = FA_data_2040.copy()

# Assign values to cells
Mass_Timber['Scenario'] = 'Mass-Timber'
Mass_Timber['N_HH'] = np.nan
Mass_Timber['Conv_Total_FA_New_LFSF'] = Mass_Timber['Total_FA_New_SF_LF'] * SC_MT_new_RCSF_to_MT
Mass_Timber['Conv_Total_FA_New_RCSF'] = Mass_Timber['Total_FA_New_SF_RC'] * (1-SC_MT_new_RCSF_to_MT)
Mass_Timber['Conv_Total_FA_New_SF'] = Mass_Timber['Conv_Total_FA_New_LFSF'] + Mass_Timber['Conv_Total_FA_New_RCSF']
Mass_Timber['Conv_Total_FA_New_LFMF'] = Mass_Timber['Total_FA_New_MF_LF'] * SC_MT_new_RCMF_to_MT
Mass_Timber['Conv_Total_FA_New_RCMF'] = Mass_Timber['Total_FA_New_MF_RC'] * (1-SC_MT_new_RCMF_to_MT)
Mass_Timber['Conv_Total_FA_New_MF'] = Mass_Timber['Conv_Total_FA_New_LFMF'] + Mass_Timber['Conv_Total_FA_New_RCMF']
Mass_Timber['Total_FA_extended_RCSF'] = (Mass_Timber['Total_FA_extended_SF']*(1-SF_LF_2018))*(1-SC_MT_new_RCSF_to_MT)
Mass_Timber['Total_FA_extended_RC_MTorAC'] = (Mass_Timber['Total_FA_extended_SF']*(1-SF_LF_2018))*SC_MT_new_RCSF_to_MT
Mass_Timber['MT_Total_FA_RCSF'] = Mass_Timber['Total_FA_New_SF_RC'] * SC_MT_new_RCSF_to_MT
Mass_Timber['MT_Total_FA_RCMF'] = Mass_Timber['Total_FA_New_MF_RC'] * SC_MT_new_RCMF_to_MT
Mass_Timber['MT_extended'] = Mass_Timber['Total_FA_extended_RC_MTorAC']
Mass_Timber['MT_Total_FA_SF&MF'] = Mass_Timber['MT_Total_FA_RCSF'] + Mass_Timber['MT_Total_FA_RCMF'] + Mass_Timber['MT_extended']
Mass_Timber['FA_new_LF'] = Mass_Timber['Conv_Total_FA_New_LFSF'] + Mass_Timber['Total_FA_New_MF_LF'] + Mass_Timber['Total_FA_extended_LFSF']
Mass_Timber['FA_new_RC'] = Mass_Timber['Conv_Total_FA_New_RCSF'] + Mass_Timber['Conv_Total_FA_New_RCMF'] + Mass_Timber['Total_FA_extended_RCSF']
Mass_Timber['FA_new_MT'] = Mass_Timber['MT_Total_FA_SF&MF']
Mass_Timber['FA_new_AC'] = Mass_Timber['AC_Total_FA_SF&MF']

# merge data
merged_df = merged_df.append(Mass_Timber, ignore_index=True)


### Alternative Cement ###
Alternative_Cement = Mass_Timber.copy()

# Assign values to cells
Alternative_Cement['Scenario'] = 'Alternative Cement'
Alternative_Cement['N_HH'] = np.nan
Alternative_Cement['MT_Total_FA_SF&MF'] = np.nan
Alternative_Cement['MT_Total_FA_RCSF'] = np.nan
Alternative_Cement['MT_Total_FA_RCMF'] = np.nan
Alternative_Cement['MT_extended'] = np.nan
Alternative_Cement['AC_Total_FA_RCSF'] = Alternative_Cement['Total_FA_New_SF_RC'] * SC_AC_new_RCSF_to_AC
Alternative_Cement['AC_Total_FA_RCMF'] = Alternative_Cement['Total_FA_New_MF_RC'] * SC_AC_new_RCMF_to_AC
Alternative_Cement['AC_extended'] = Alternative_Cement['Total_FA_extended_RC_MTorAC']
Alternative_Cement['AC_Total_FA_SF&MF'] = Alternative_Cement['AC_Total_FA_RCSF'] + Alternative_Cement['AC_Total_FA_RCMF'] + Alternative_Cement['AC_extended']
Alternative_Cement['FA_new_LF'] = Alternative_Cement['Conv_Total_FA_New_LFSF'] + Alternative_Cement['Total_FA_New_MF_LF'] + Alternative_Cement['Total_FA_extended_LFSF']
Alternative_Cement['FA_new_RC'] = Alternative_Cement['Conv_Total_FA_New_RCSF'] + Alternative_Cement['Conv_Total_FA_New_RCMF'] + Alternative_Cement['Total_FA_extended_RCSF']
Alternative_Cement['FA_new_MT'] = Alternative_Cement['MT_Total_FA_SF&MF']
Alternative_Cement['FA_new_AC'] = Alternative_Cement['AC_Total_FA_SF&MF']

# merge
merged_df = merged_df.append(Alternative_Cement, ignore_index=True)

print(merged_df)

# Export to csv file
merged_df.to_csv('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/1st Research/Code/Separated Code/Floor Area/Merged.csv', index=False)