from flask import Flask, jsonify
import pycharm_projects.utility.sql_utility as sql_utility

sql_utility = sql_utility.Sql_utility("localhost", "root", "new_password", "db1")

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
