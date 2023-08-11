import matplotlib.pyplot as plt

# Data
strategies = ['BTU 2020', 'BTU 2040', 'Compact City', 'Effective Design', 'Intensive Use', 'Alternative Cement']
Emission_AC = [5376, 5297, 5235, 4822, 4237, 4405]

# Calculate reduction percentage
reduction_percentage = [100 * (Emission_AC[i] - Emission_AC[1]) / Emission_AC[1] for i in range(len(Emission_AC))]

# Define colors for each strategy
colors = ['blue', 'red', 'green', 'orange', 'purple', 'grey']

# Create the bar graph
plt.bar(strategies, Emission_AC, color=colors)
plt.xlabel('Single Strategies')
plt.ylabel('Annual Emission')
plt.title('Annual Emission with Single Strategy')

# Add reduction percentage on top of each bar (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Emission_AC)):
    plt.text(i, Emission_AC[i], f'{reduction_percentage[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Display the graph
#plt.tight_layout()
#plt.show()

plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Single Strategy/Wedge Single/Wedge_AC_Single/Wedge AC Single.png')