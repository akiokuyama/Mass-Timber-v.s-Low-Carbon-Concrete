import matplotlib.pyplot as plt

# Data for multiplicative strategies
strategies = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ CSA', '+ ACC']
Total_AAC = [5397751, 5318685, 5233787, 5011886, 4006420, 4381932, 4223877, 4333477]


# Calculate reduction percentage
reduction_percentage = [100 * (Total_AAC[i] - Total_AAC[1]) / Total_AAC[1] for i in range(len(Total_AAC))]

# Define colors for each strategy
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown','lightblue', 'grey']

# Data for single strategies
single_strategies = ['BTU 2020', 'BTU 2040', 'Compact City', 'Effective Design', 'Intensive Use', 'Mass-Timber', 'CSA', 'ACC']
Total_ACC_single = [5397751, 5318685, 5233787, 5093185, 4254948, 5677133, 5651386, 5817736]

# Calculate reduction percentage for PC_CSA graph
reduction_percentage_single = [100 * (Total_ACC_single[i] - Total_ACC_single[1]) / Total_ACC_single[1] for i in range(len(Total_ACC_single))]

# Define colors for PC_CSA graph
colors_single = ['blue', 'red', 'green', 'orange', 'purple', 'brown','lightblue', 'grey']

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot PC graph
ax1.bar(strategies, Total_AAC, color=colors)
ax1.set_xlabel('Strategies')
ax1.set_ylabel('Material Production Cost')
# ax1.set_title('Total Material Cost of Reduction Strategies with multiplicative strategies')

# Add reduction percentage on top of each bar for PC graph
for i in range(2, len(Total_AAC)):
    ax1.text(i, Total_AAC[i], f'{reduction_percentage[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels for PC graph
ax1.set_xticklabels(strategies, rotation=45, ha='right')

# Plot PC_CSA graph
ax2.bar(single_strategies, Total_ACC_single, color=colors_single)
ax2.set_xlabel('Strategies')
# ax2.set_ylabel('Material Production Cost')
# ax2.set_title('Total Material Cost of Reduction Strategies with single strategy')

# Add reduction percentage on top of each bar for PC_CSA graph
for i in range(2, len(Total_ACC_single)):
    ax2.text(i, Total_ACC_single[i], f'{reduction_percentage_single[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels for PC_CSA graph
ax2.set_xticklabels(single_strategies, rotation=45, ha='right')

# Adjust spacing between subplots
plt.tight_layout()

# Display the subplots
# plt.show()



plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Cost Estimation/Cost Calculation.png')