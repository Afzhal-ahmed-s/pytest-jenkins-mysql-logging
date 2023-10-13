import datetime
import subprocess
import re
import pycharm_projects.utility.sql_utility as sql_utility

import graphical_representation.pie_chart_format_representation as pie
import graphical_representation.image_imbedder_into_html_file as img_imb
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

sql_gateway = sql_utility.Sql_utility("localhost", "root", "new_password", "db1")


# # Generate the timestamp
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#
# # Define the pytest command with dynamically generated arguments
# pytest_command = [
#     "pytest",
#     f"--html=reports/report_{timestamp}.html",
#     "test_suite.py"
# ]
#
# # subprocess.run(pytest_command)
# result = subprocess.run(pytest_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
#
# # Extract pass and fail counts from the output
# output = result.stdout
# pass_match = re.search(r"(\d+) passed", output)
# fail_match = re.search(r"(\d+) failed", output)
#
# # Check if there were pass and fail matches
# if pass_match:
#     pass_count = int(pass_match.group(1))
# else:
#     pass_count = 0
#
# if fail_match:
#     fail_count = int(fail_match.group(1))
# else:
#     fail_count = 0
#
# # Print the pass and fail counts
# print(f"Pass Count: {pass_count}")
# print(f"Fail Count: {fail_count}")
#
# p = pie.Pie_chart_format_representation(pass_count, fail_count)
#
# p.form_pie_chart(timestamp)
#
#
# # Check the return code
# if result.returncode == 0:
#     print("Test suite passed.")
# elif result.returncode == 1:
#     print("Test suite failed.")
# else:
#     print("Error: Test suite execution failed with return code", result.returncode)
#
#
#
# png_file_name = f"pie_chart of report at {timestamp}"
# html_file_name = f"report_{timestamp}"
#
# # pie chart imbedding into html report
#
# i = img_imb.Img_imbedder()
# i.img_imbed_into_html(html_file_name, png_file_name )
#
# # PERSISTING HTML FILE INTO DB
# sql_gateway.persist_html_report_into_db(html_file_name)
#
# # RETRIEVING HTML DATA FROM DB
sql_gateway.retrieve_html_data_from_db()

