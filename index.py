from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import index
import queries2

app = Flask(__name__)


@app.route('/')
def index_page():
    title = 'Application Process - Part 2'
    column_titles = ('Choose from the options below',)
    data_list = [
        ('<a href="/mentors">1: mentors and schools<a>',),
        ('<a href="/all-school">2: all mentors and school<a>',),
        ('<a href="/mentors-by-country">3: mentors by country<a>',),
        ('<a href="/contacts">4: conctacts<a>',),
        ('<a href="/applicants">5: applicants_page<a>',),
        ('<a href="/applicants-and-mentors">6: applicants and mentors page<a>',)
    ]
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


@app.route('/mentors')
def mentors_and_schools_page():
    title = 'Mentors and Schools'
    column_titles = ['Full name', 'School', 'Country']
    data_list = queries2.mentors_and_schools()
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


@app.route('/all-school')
def mentors_and_schools_all_page():
    title = 'All Schools and Mentors'
    column_titles = ['Full name', 'School', 'Country']
    data_list = queries2.mentors_and_schools_all()
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


@app.route('/mentors-by-country')
def mentors_by_country_page():
    title = 'Mentors and Schools'
    column_titles = ['School', 'Number of Mentors']
    data_list = queries2.mentors_by_country()
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


@app.route('/contacts')
def contact_page():
    title = 'Contact Page'
    column_titles = ['School', 'Contact Person']
    data_list = queries2.contacts()
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


@app.route('/applicants')
def applicants_page():
    title = 'Applicants page'
    column_titles = ['Applicant Name', 'Applicant Code', 'Creation Date']
    data_list = queries2.applicants()
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


@app.route('/applicants-and-mentors')
def applicants_and_mentors_page():
    title = 'Applicants and mentors'
    column_titles = ['Applicant name', 'Application Code', 'Assigned Mentor']
    data_list = queries2.applicants_and_mentors()
    return render_template('index.html', data_list=data_list, title=title, column_titles=column_titles)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
