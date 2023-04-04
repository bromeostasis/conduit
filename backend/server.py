# Import flask and datetime module for showing date and time
import datetime
from flask import Flask, request, jsonify
from csv_reader.reader import *
  
now = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route('/data')
def get_time():
    return [{
        "String":"Celing type",
        "Date":now,
    }]

@app.route('/get_next_selectors', methods=['POST'])
def get_next_selectors():
    body = request.get_json()
    print(body)
    return get_next_results(body)

  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)