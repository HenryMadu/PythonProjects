import matplotlib.pyplot as plt
#This line imports the pyplot module from the Matplotlib library. 
# pyplot provides a collection of functions that make it easy to create various types of plots and charts.

labels = ["Category A", "Category B", "Category C", "Category D"] 
#Here, you create a list called labels that contains the names of the categories you want to display in the pie chart. 
# Each label corresponds to a segment of the pie.
sizes = [15, 30, 45, 10]
#This line creates a list called sizes, which contains the numerical values that represent the size of each category in the pie chart. 
# The values correspond to the labels in the same order.

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# This line generates the pie chart using the plt.pie() function.
# sizes: This is the data that determines the size of each slice of the pie.
# labels: This assigns the category names to each slice.
# autopct='%1.1f%%': This formats the percentage display on each slice. It shows one decimal place followed by a percent sign (e.g., “30.0%”).
# startangle=140: This rotates the start of the pie chart to 140 degrees, which can help in positioning the slices more aesthetically.

plt.title("Henry's Pie Chart")
#This line sets the title of the pie chart to “Henry’s Pie Chart”. The title appears at the top of the chart.

plt.show()
#This line displays the pie chart in a window. The plt.show() function renders the chart so you can see it.