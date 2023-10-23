from flask import Flask, jsonify, render_template
import pycharm_projects.utility.sql_utility as sql_utility

sql_utility = sql_utility.Sql_utility("localhost", "root", "new_password", "db1")

# app = Flask(__name__)
app = Flask(__name__, template_folder='/home/afzhal-ahmed-s/pytest-jenkins-mysql-logging/pycharm_projects/task/demonstration/nitinc_pre_task/full_stack/template')
app.static_folder = 'static'  # Set the static folder to the 'static' directory


@app.route('/api/get_records', methods=['GET'])
def get_records():
    # Fetch all the records as a list of tuples
    records = sql_utility.retrieve_html_data_from_db()

    # Convert the list of tuples to a list of dictionaries for JSON serialization
    record_list = []
    for record in records:
        record_dict = {
            'file_name': record[0],
            'file_content': record[1],
        }
        record_list.append(record_dict)

    return jsonify(record_list)

@app.route('/')
def index():
    return render_template('index.html')

# Define a route to get file content
@app.route('/api/get_file_content/<filename>', methods=['GET'])
def get_file_content(filename):
    # Use the SQL utility method to retrieve file content by file name
    file_content = sql_utility.retrieve_html_file_content_from_db_with_file_name(filename)

    if file_content is not None:
        # Return the file content as a response
        return file_content
    else:
        # Handle the case where no matching record is found
        return "File not found", 404



if __name__ == '__main__':
    app.run(debug=True)