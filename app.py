
from flask import Flask , render_template, request, redirect, url_for, flash, jsonify
from forms import SearchForm
import yaml


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if request.method == 'POST' and form.validate():
        url = request.form['url']
        if getUrlFromYaml(url):
            flash('URL Is Safe', 'Success')
            return redirect(url_for('index'))
        else:
            flash('URL Is Not Safe', 'Error')
            return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


def getUrlFromYaml(url):
    with open('urls.yml', 'r') as file:
        for data in yaml.load_all(file, Loader=yaml.FullLoader):
            for index in range(len(data)):
                if  data[index]['url'] == url :
                    return True
            return False




if __name__ == '__main__':
    app.run(debug=True)