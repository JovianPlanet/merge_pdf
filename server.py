""" AI yr data

Server code for web application

    Executing this function initiates the application of stone price
    predictions to be executed over the Flask channel and deployed on
    localhost:5000.
"""
import os
from flask import Flask, request, render_template
from pypdf import PdfWriter

app = Flask("Stone price analyzer")

pdfs = []

# Define a route to render the index.html template
@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Renders index page
    '''
    global pdfs
    path = ""
    try:
        if request.method == 'POST':
            if request.form['data_btn'] == 'load_pdf':
                path = request.form.get('mfile')
                pdfs.append(os.path.join('./data/', path))
                print(f"Files: \n{pdfs}\n\n")
                txt ='File added to merge list'
            elif request.form['data_btn'] == 'merge':
                merger = PdfWriter()
                for pdf in pdfs:
                    merger.append(pdf)
                merger.write('./data/result.pdf')
                merger.close()
                txt ='Files merged'
            return render_template('index.html', msg=txt)
    except Exception as e:
        print(f"An error ocurred")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

