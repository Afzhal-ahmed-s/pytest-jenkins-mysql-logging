import run
print(run.timestamp)

def img_imbed_into_html(html_f_name, img_f_name):
    g_html_file_name = "/home/afzhal-ahmed-s/pytest-jenkins-mysql-logging/pycharm_projects/task/demonstration/nitinc_pre_task/reports/" + html_f_name + ".html"
    g_image_file_name = img_f_name + ".png"


    html_file_path = g_html_file_name  # Replace with the actual file path


    img_tag = f'<img src="{g_image_file_name}" alt="Pie Chart">'

    # Read the HTML file content
    with open(html_file_path, 'r') as file:
        lines = file.readlines()

    # Find the last line of the body and insert the <img> tag before it
    for i, line in enumerate(reversed(lines)):
        if '</body>' in line:
            lines.insert(len(lines) - i, img_tag)
            break

    # Write the modified content back to the HTML file
    with open(html_file_path, 'w') as file:
        file.writelines(lines)

    print(f'Added the {img_tag} file into {html_file_path}')



# img_imbed_into_html("report_2023-10-11_17-24-09", "pie_chart of report at 2023-10-11_19-07-17")