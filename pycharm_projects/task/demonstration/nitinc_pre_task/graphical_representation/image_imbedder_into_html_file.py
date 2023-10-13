
class Img_imbedder:
    def __init__(self):
        print("Img_imb_intiated")


    def img_imbed_into_html(self, html_f_name, img_f_name):
        g_html_file_name = "/home/afzhal-ahmed-s/pytest-jenkins-mysql-logging/pycharm_projects/task/demonstration/nitinc_pre_task/reports/" + html_f_name + ".html"
        g_image_file_name = '"' + img_f_name + '.png"'

        # Define the <img> tag to add
        img_tag = '<img src=' + g_image_file_name + ' alt="Pie Chart">'

        # Read the HTML file content
        with open(g_html_file_name, 'r') as file:
            lines = file.readlines()

        # Find the last line of the body and insert the <img> tag before it
        for i, line in enumerate(reversed(lines)):
            if '</body>' in line:
                lines.insert(len(lines) - i, img_tag)
                break

        # Write the modified content back to the HTML file
        with open(g_html_file_name, 'w') as file:
            file.writelines(lines)

        print(f'Added the {img_tag} file into {html_f_name}')