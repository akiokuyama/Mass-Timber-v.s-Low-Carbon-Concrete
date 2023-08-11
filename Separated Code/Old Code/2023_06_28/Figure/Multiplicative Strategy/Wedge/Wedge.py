import matplotlib.pyplot as plt

# Define the strategies and their corresponding CO2 reduction values
strategies = {0: 'BTU', 1: '+ Compact City', 2: '+ Effective Design', 3: '+ Intensive Use', 4: '+ Mass-Timber'}
emission_2020 = [5423, 5423, 5423, 5423, 5423]
emission_2040_MT = [5344, 5259, 4783, 3823, 3330]

reduction_percent = []

for i in range(len(emission_2020) - 1):
    reduction = (emission_2040_MT[i] - emission_2040_MT[i+1]) / emission_2040_MT[i]
    reduction_percent.append(reduction)

for i, reduction in enumerate(reduction_percent):
    strategy_label = strategies[i+1]
    print(f'{strategy_label}: {reduction}')

# Define the colors for each line and gap
line_colors = ['blue', 'green', 'orange', 'purple', 'brown']

# Create the first subplot for the first graph
fig, axs = plt.subplots(1, 3, figsize=(12, 6))

# Plot the first graph on the first subplot
light_brown = (0.71, 0.4, 0.11)
axs[0].fill_between([0, 1], [emission_2020[0], emission_2040_MT[0]], [emission_2020[1], emission_2040_MT[1]], color='green', alpha=0.3)
axs[0].fill_between([0, 1], [emission_2020[1], emission_2040_MT[1]], [emission_2020[2], emission_2040_MT[2]], color='peachpuff', alpha=0.3)
axs[0].fill_between([0, 1], [emission_2020[2], emission_2040_MT[2]], [emission_2020[3], emission_2040_MT[3]], color='lavender', alpha=0.3)
axs[0].fill_between([0, 1], [emission_2020[3], emission_2040_MT[3]], [emission_2020[4], emission_2040_MT[4]], color=light_brown, alpha=0.3)

for i in range(len(strategies)):
    axs[0].plot([0, 1], [emission_2020[i], emission_2040_MT[i]], color=line_colors[i], label=strategies[i])

for i in range(0, len(reduction_percent)):
    y_pos = (emission_2040_MT[i] + emission_2040_MT[i+1]) / 2
    axs[0].text(1.05, y_pos, f'{reduction_percent[i]:.2%}', va='center')

axs[0].set_xlabel('Year')
axs[0].set_ylabel('Annual Emission')
axs[0].set_xticks([0, 1])
axs[0].set_xticklabels(['2020', '2040'])
#axs[0].set_title('Reduction in CO2 Emission by Strategies')
axs[0].legend()

# Set the y-axis range and tick labels
axs[0].set_ylim(2000, 6100)
axs[0].set_yticks(range(2000, 6100, 1000))

# Define the strategies and their corresponding CO2 reduction values for the second graph
strategies = {0: 'BTU', 1: '+ Compact City', 2: '+ Effective Design', 3: '+ Intensive Use', 4: '+ CSA'}
emission_2020 = [5423, 5423, 5423, 5423, 5423]
emission_2040_CSA = [5344, 5259, 4783, 3823, 3528]

reduction_percent = []

for i in range(len(emission_2020) - 1):
    reduction = (emission_2040_CSA[i] - emission_2040_CSA[i+1]) / emission_2040_CSA[i]
    reduction_percent.append(reduction)

for i, reduction in enumerate(reduction_percent):
    strategy_label = strategies[i+1]
    print(f'{strategy_label}: {reduction}')

# Define the colors for each line and gap
line_colors = ['blue', 'green', 'orange', 'purple', 'lightblue']

# Plot the second graph on the second subplot
axs[1].fill_between([0, 1], [emission_2020[0], emission_2040_CSA[0]], [emission_2020[1], emission_2040_CSA[1]], color='green', alpha=0.3)
axs[1].fill_between([0, 1], [emission_2020[1], emission_2040_CSA[1]], [emission_2020[2], emission_2040_CSA[2]], color='peachpuff', alpha=0.3)
axs[1].fill_between([0, 1], [emission_2020[2], emission_2040_CSA[2]], [emission_2020[3], emission_2040_CSA[3]], color='lavender', alpha=0.3)
axs[1].fill_between([0, 1], [emission_2020[3], emission_2040_CSA[3]], [emission_2020[4], emission_2040_CSA[4]], color='lightblue', alpha=0.3)

for i in range(len(strategies)):
    axs[1].plot([0, 1], [emission_2020[i], emission_2040_CSA[i]], color=line_colors[i], label=strategies[i])

# Plot the reduction percentage only between the last pair of emissions
y_pos = (emission_2040_CSA[-2] + emission_2040_CSA[-1]) / 2
axs[1].text(1.05, y_pos, f'{reduction_percent[-1]:.2%}', va='center')

axs[1].set_xlabel('Year')
#axs[1].set_ylabel('Annual Emission')
axs[1].set_xticks([0, 1])
axs[1].set_xticklabels(['2020', '2040'])
#axs[1].set_title('Reduction in CO2 Emission by Strategies')
axs[1].legend()

# Set the y-axis range and tick labels
axs[1].set_ylim(2000, 6100)
axs[1].set_yticks(range(2000, 6100, 1000))


# Define the strategies and their corresponding CO2 reduction values for the second graph
strategies = {0: 'BTU', 1: '+ Compact City', 2: '+ Effective Design', 3: '+ Intensive Use', 4: '+ ACC'}
emission_2020 = [5423, 5423, 5423, 5423, 5423]
emission_2040_ACC = [5344, 5259, 4783, 3823, 3215]

reduction_percent = []

for i in range(len(emission_2020) - 1):
    reduction = (emission_2040_ACC[i] - emission_2040_ACC[i+1]) / emission_2040_ACC[i]
    reduction_percent.append(reduction)

# Define the colors for each line and gap
line_colors = ['blue', 'green', 'orange', 'purple', 'grey']

# Plot the second graph on the second subplot
axs[2].fill_between([0, 1], [emission_2020[0], emission_2040_ACC[0]], [emission_2020[1], emission_2040_ACC[1]], color='green', alpha=0.3)
axs[2].fill_between([0, 1], [emission_2020[1], emission_2040_ACC[1]], [emission_2020[2], emission_2040_ACC[2]], color='peachpuff', alpha=0.3)
axs[2].fill_between([0, 1], [emission_2020[2], emission_2040_ACC[2]], [emission_2020[3], emission_2040_ACC[3]], color='lavender', alpha=0.3)
axs[2].fill_between([0, 1], [emission_2020[3], emission_2040_ACC[3]], [emission_2020[4], emission_2040_ACC[4]], color='lightgrey', alpha=0.3)

for i in range(len(strategies)):
    axs[2].plot([0, 1], [emission_2020[i], emission_2040_ACC[i]], color=line_colors[i], label=strategies[i])

# Plot the reduction percentage only between the last pair of emissions
y_pos = (emission_2040_ACC[-2] + emission_2040_ACC[-1]) / 2
axs[2].text(1.05, y_pos, f'{reduction_percent[-1]:.2%}', va='center')

axs[2].set_xlabel('Year')
# axs[2].set_ylabel('Annual Emission')
axs[2].set_xticks([0, 1])
axs[2].set_xticklabels(['2020', '2040'])
# axs[2].set_title('Reduction in CO2 Emission by Strategies')
axs[2].legend()

# Set the y-axis range and tick labels
axs[2].set_ylim(2000, 6100)
axs[2].set_yticks(range(2000, 6100, 1000))

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.4)

# Display the plot
#plt.show()


fig.savefig('/Users/akihi/Library/CloudStorage/OneDrive-PrincetonUniversity/Projects/Building Material in Cities/Top Down Approach/Code/Figure/Multiplicative Strategy/Wedge/Wedge.png')