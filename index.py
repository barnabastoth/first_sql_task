from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import index
import queries2

app = Flask(__name__)


@app.route('/mentors')
def Mentors_and_Schools():
    title = 'Mentors and Schools'
    data_list = queries2.mentors_and_schools()
    return render_template('index.html', data_list=data_list, title=title)


@app.route('/all-school')
def Mentors_and_Schools_all():
    title = 'All Schools and Mentors'
    data_list = queries2.mentors_and_schools_all()
    return render_template('index.html', data_list=data_list, title=title)


@app.route('/mentors-by-country')
def Mentors_by_country():
    title = 'Mentors and Schools'
    data_list = queries2.mentors_by_country()
    return render_template('index.html', data_list=data_list, title=title)


@app.route('/contacts')
def contact_page():
    title = 'Contact Page'
    data_list = queries2.contacts()
    return render_template('index.html', data_list=data_list, title=title)


@app.route('/applicants')
def applicants_page():
    title = 'Applicants page'
    data_list = queries2.applicants()
    return render_template('index.html', data_list=data_list, title=title)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
