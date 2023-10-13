import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Passed', 'Failed']
sizes = [11,1]  # Sizes or proportions for each category

# Create a pie chart
plt.figure(figsize=(4, 4))  # Set the figure size (optional)
plt.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=140)

# Optional customization
plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Show the pie chart
plt.show()
