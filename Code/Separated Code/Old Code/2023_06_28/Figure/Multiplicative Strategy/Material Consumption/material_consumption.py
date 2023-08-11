import matplotlib.pyplot as plt

# Data for PC graph
strategies_PC = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
PC = [2755, 2715, 2671, 2164, 1729, 1261, 893]

# Calculate reduction percentage for PC graph
reduction_percentage_PC = [100 * (PC[i] - PC[1]) / PC[1] for i in range(len(PC))]

# Define colors for PC graph
colors_PC = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Data for PC_AC graph
strategies_PC_AC = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
PC_AC = [2705, 2665, 2646, 2144, 1713, 1245, 1713]

# Calculate reduction percentage for PC_AC graph
reduction_percentage_PC_AC = [100 * (PC_AC[i] - PC_AC[1]) / PC_AC[1] for i in range(len(PC_AC))]

# Define colors for PC_AC graph
colors_PC_AC = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Data for Iron_Steel graph
strategies_Iron_Steel = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
Iron_Steel = [1134, 1118, 1100, 1100, 880, 581, 879]

# Calculate reduction percentage for Iron_Steel graph
reduction_percentage_Iron_Steel = [100 * (Iron_Steel[i] - Iron_Steel[1]) / Iron_Steel[1] for i in range(len(Iron_Steel))]

# Define colors for Iron_Steel graph
colors_Iron_Steel = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Data for Wood graph
strategies_Wood = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
Wood = [7242, 7136, 7022, 7022, 5614, 6481, 5611]

# Calculate reduction percentage for Wood graph
reduction_percentage_Wood = [100 * (Wood[i] - Wood[1]) / Wood[1] for i in range(len(Wood))]

# Define colors for Wood graph
colors_Wood = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot PC graph
axs[0, 0].bar(strategies_PC, PC, color=colors_PC)
#axs[0, 0].set_xlabel('Strategies')
axs[0, 0].set_ylabel('Portland Cement in tons')
axs[0, 0].set_title('Portland Cement')


# Add reduction percentage on top of each bar in PC graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(PC)):
    axs[0, 0].text(i, PC[i], f'{reduction_percentage_PC[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in PC graph
axs[0, 0].set_xticklabels(strategies_PC, rotation=45, ha='right')

# Plot PC_AC graph
axs[0, 1].bar(strategies_PC_AC, PC_AC, color=colors_PC_AC)
#axs[0, 1].set_xlabel('Strategies')
axs[0, 1].set_ylabel('PC & Alternative Cement in tons')
axs[0, 1].set_title('PC & Alternative Cement')

# Add reduction percentage on top of each bar in PC_AC graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(PC_AC)):
    axs[0, 1].text(i, PC_AC[i], f'{reduction_percentage_PC_AC[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in PC_AC graph
axs[0, 1].set_xticklabels(strategies_PC_AC, rotation=45, ha='right')

# Plot Iron_Steel graph
axs[1, 0].bar(strategies_Iron_Steel, Iron_Steel, color=colors_Iron_Steel)
#axs[1, 0].set_xlabel('Strategies')
axs[1, 0].set_ylabel('Iron Steel in tons')
axs[1, 0].set_title('Iron Steel')

# Add reduction percentage on top of each bar in Iron_Steel graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Iron_Steel)):
    axs[1, 0].text(i, Iron_Steel[i], f'{reduction_percentage_Iron_Steel[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in Iron_Steel graph
axs[1, 0].set_xticklabels(strategies_Iron_Steel, rotation=45, ha='right')

# Plot Wood graph
axs[1, 1].bar(strategies_Wood, Wood, color=colors_Wood)
#axs[1, 1].set_xlabel('Strategies')
axs[1, 1].set_ylabel('Wood in tons')
axs[1, 1].set_title('Wood')

# Add reduction percentage on top of each bar in Wood graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Wood)):
    axs[1, 1].text(i, Wood[i], f'{reduction_percentage_Wood[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in Wood graph
axs[1, 1].set_xticklabels(strategies_Wood, rotation=45, ha='right')

# Adjust spacing between subplots
plt.tight_layout()

# Display the graph
#plt.show()

plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Multiplicative Strategy/Material Consumption/Material Consumption 4.png')


############################################################################################################################
import matplotlib.pyplot as plt

# Data for PC graph
strategies_PC = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
PC = [2755, 2715, 2671, 2164, 1729, 1261, 893]

# Calculate reduction percentage for PC graph
reduction_percentage_PC = [100 * (PC[i] - PC[1]) / PC[1] for i in range(len(PC))]

# Define colors for PC graph
colors_PC = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Data for Iron_Steel graph
strategies_Iron_Steel = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
Iron_Steel = [1134, 1118, 1100, 1100, 880, 581, 879]

# Calculate reduction percentage for Iron_Steel graph
reduction_percentage_Iron_Steel = [100 * (Iron_Steel[i] - Iron_Steel[1]) / Iron_Steel[1] for i in range(len(Iron_Steel))]

# Define colors for Iron_Steel graph
colors_Iron_Steel = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Data for Wood graph
strategies_Wood = ['BTU 2020', 'BTU 2040', '+ Compact City', '+ Effective Design', '+ Intensive Use', '+ Mass-Timber', '+ Alternative Cement']
Wood = [7242, 7136, 7022, 7022, 5614, 6481, 5611]

# Calculate reduction percentage for Wood graph
reduction_percentage_Wood = [100 * (Wood[i] - Wood[1]) / Wood[1] for i in range(len(Wood))]

# Define colors for Wood graph
colors_Wood = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'grey']

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 8))

# Plot PC graph
axs[0].bar(strategies_PC, PC, color=colors_PC)
#axs[0, 0].set_xlabel('Strategies')
axs[0].set_ylabel('Portland Cement in tons')
axs[0].set_title('Portland Cement')


# Add reduction percentage on top of each bar in PC graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(PC)):
    axs[0].text(i, PC[i], f'{reduction_percentage_PC[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in PC graph
axs[0].set_xticklabels(strategies_PC, rotation=45, ha='right')

# Plot Iron_Steel graph
axs[1].bar(strategies_Iron_Steel, Iron_Steel, color=colors_Iron_Steel)
#axs[1].set_xlabel('Strategies')
axs[1].set_ylabel('Iron Steel in tons')
axs[1].set_title('Iron Steel')

# Add reduction percentage on top of each bar in Iron_Steel graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Iron_Steel)):
    axs[1].text(i, Iron_Steel[i], f'{reduction_percentage_Iron_Steel[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in Iron_Steel graph
axs[1].set_xticklabels(strategies_Iron_Steel, rotation=45, ha='right')

# Plot Wood graph
axs[2].bar(strategies_Wood, Wood, color=colors_Wood)
#axs[1, 1].set_xlabel('Strategies')
axs[2].set_ylabel('Wood in tons')
axs[2].set_title('Wood')

# Add reduction percentage on top of each bar in Wood graph (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Wood)):
    axs[2].text(i, Wood[i], f'{reduction_percentage_Wood[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels in Wood graph
axs[2].set_xticklabels(strategies_Wood, rotation=45, ha='right')

# Adjust spacing between subplots
plt.tight_layout()

# Display the graph
#plt.show()

plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Multiplicative Strategy/Material Consumption/Material Consumption 3.png')
