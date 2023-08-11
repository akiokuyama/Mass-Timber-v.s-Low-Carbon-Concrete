import matplotlib.pyplot as plt

# Define the strategies and their corresponding CO2 reduction values
strategies = {0: 'BTU', 1: '+ Compact City', 2: '+ Effective Design', 3: '+ Intensive Use', 4: '+ Alternative Cement'}
emission_2020 = [5376, 5376, 5376, 5376, 5376]
emission_2040_AC = [5297, 5235, 4763, 3806, 3207]

reduction_percent = []

for i in range(len(emission_2020) - 1):
    reduction = (emission_2040_AC[i] - emission_2040_AC[i+1]) / emission_2040_AC[i]
    reduction_percent.append(reduction)

for i, reduction in enumerate(reduction_percent):
    strategy_label = strategies[i+1]

# Define the colors for each line and gap
line_colors = ['blue', 'green', 'red', 'orange', 'grey']

# Create a figure and axes
fig, ax = plt.subplots()

# Fill the gaps between specific strategies
ax.fill_between([0, 1], [emission_2020[0], emission_2040_AC[0]], [emission_2020[1], emission_2040_AC[1]], color='green', alpha=0.3)
ax.fill_between([0, 1], [emission_2020[1], emission_2040_AC[1]], [emission_2020[2], emission_2040_AC[2]], color='pink', alpha=0.3)
ax.fill_between([0, 1], [emission_2020[2], emission_2040_AC[2]], [emission_2020[3], emission_2040_AC[3]], color='peachpuff', alpha=0.3)
ax.fill_between([0, 1], [emission_2020[3], emission_2040_AC[3]], [emission_2020[4], emission_2040_AC[4]], color='lightgrey', alpha=0.3)

# Plot the line graph for each strategy
for i in range(len(strategies)):
    ax.plot([0, 1], [emission_2020[i], emission_2040_AC[i]], color=line_colors[i], label=strategies[i])
    
# Add reduction percentages as text
for i in range(0,len(reduction_percent)):
    y_pos = (emission_2040_AC[i] + emission_2040_AC[i+1]) / 2
    ax.text(1.05, y_pos, f'{reduction_percent[i]:.2%}', va='center')


# Set x-axis and y-axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Annual Emission')

# Set the x-axis tick labels
ax.set_xticks([0, 1])
ax.set_xticklabels(['2020', '2040'])

# Set the y-axis range and tick labels
ax.set_ylim(2000, 6100)
ax.set_yticks(range(2000, 6100, 1000))

# Set the title and legend
ax.set_title('Reduction in CO2 Emission by Strategies')
ax.legend()

# Display the plot
#plt.show()

plt.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Multiplicative Strategy/Wedge/Wedge_AC/Wedge_AC.png')

