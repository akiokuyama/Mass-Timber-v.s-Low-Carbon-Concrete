import matplotlib.pyplot as plt

# Data
strategies = ['BTU 2020', 'BTU 2040', 'Compact City', 'Effective Design', 'Intensive Use', 'Mass-Timber']
Emission_MT = [5376, 5297, 5235, 4822, 4237, 4467]

# Calculate reduction percentage
reduction_percentage = [100 * (Emission_MT[i] - Emission_MT[1]) / Emission_MT[1] for i in range(len(Emission_MT))]

# Define colors for each strategy
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']

# Create the bar graph
plt.bar(strategies, Emission_MT, color=colors)
plt.xlabel('Single Strategies')
plt.ylabel('Annual Emission')
plt.title('Annual Emission with Single Strategy')

# Add reduction percentage on top of each bar (excluding BTU 2020 and BTU 2040)
for i in range(2, len(Emission_MT)):
    plt.text(i, Emission_MT[i], f'{reduction_percentage[i]:.2f}%', ha='center', va='bottom')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Display the graph
#plt.tight_layout()
#plt.show()

plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Single Strategy/Wedge Single/Wedge_MT_Single/Wedge MT Single.png')