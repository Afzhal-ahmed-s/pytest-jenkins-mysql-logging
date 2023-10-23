import matplotlib.pyplot as plt
import os


class Pie_chart_format_representation:

    def __init__(self, passed_count, failed_count):
        global passed
        global failed
        passed = passed_count
        failed = failed_count

    def form_pie_chart(self, timestamp):
        # Data for the pie chart
        labels = ['Passed', 'Failed']
        sizes = [passed, failed]  # Sizes or proportions for each category

        # Create a pie chart
        plt.figure(figsize=(5, 5))  # Set the figure size (optional)
        plt.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=140)

        # Optional customization
        plt.title(f'Tests result of {timestamp} in pie chart format')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        reports_folder = "reports"
        os.makedirs(reports_folder, exist_ok=True)
        chart_filename = os.path.join(reports_folder, f'pie_chart of report at {timestamp}.png')

        # Save the pie chart to a file (e.g., PNG, JPEG, PDF)
        plt.savefig(chart_filename)  # Specify the desired file format and name

        # Show the pie chart
        # plt.show()

        return f'pie_chart of report at {timestamp}.png'
