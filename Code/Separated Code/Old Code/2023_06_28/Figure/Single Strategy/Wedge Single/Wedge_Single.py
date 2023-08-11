import matplotlib.pyplot as plt

# Data
strategies = ['BTU 2020', 'BTU 2040', 'Compact City', 'Effective Design', 'Intensive Use', 'Mass-Timber', 'CSA', 'ACC']
Emission_Single = [5423, 5344, 5259, 4860, 4275, 4514, 4928, 4452]

# Calculate reduction percentage
reduction_percentage = [100 * (Emission_Single[i] - Emission_Single[1]) / Emission_Single[1] for i in range(len(Emission_Single))]

# Define colors for each strategy
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'lightblue', 'grey']

# Create the bar graph
plt.bar(strategies, Emission_Single, color=colors)
plt.xlabel('Strategies')
plt.ylabel('Annual Emissions')
# plt.title('Annual Emission with Single Strategy')

# Add reduction percentage on top of each bar (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Emission_Single)):
    plt.text(i, Emission_Single[i], f'{reduction_percentage[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Display the graph
plt.tight_layout()
#plt.show()


plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Single Strategy/Wedge Single/Wedge Single.png')