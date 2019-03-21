from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/books')
def books():
    return render_template('index.html')


@app.route('/artbooks')
def artbooks():
    return render_template('artbooks.html')

@app.route('/artdesc1')
def artdesc1():
    return render_template('artdesc1.html')

@app.route('/artdesc2')
def artdesc2():
    return render_template('artdesc2.html')

@app.route('/artdesc3')
def artdesc3():
    return render_template('artdesc3.html')


@app.route('/comics')
def comics():
    return render_template('comics.html')

@app.route('/comicsdesc1')
def comicdesc1():
    return render_template('comicsdesc1.html')

@app.route('/comicsdesc2')
def comicdesc2():
    return render_template('comicsdesc2.html')

@app.route('/comicsdesc3')
def comicdesc3():
    return render_template('comicsdesc3.html')



@app.route('/fantasy')
def fantasy():
    return render_template('fantasy.html')

@app.route('/fantasydesc1')
def fantasydesc1():
    return render_template('fantasydesc1.html')

@app.route('/fantasydesc2')
def fantasydesc2():
    return render_template('fantasydesc2.html')

@app.route('/fantasydesc3')
def fantasydesc3():
    return render_template('fantasydesc3.html')

if __name__ == '__main__':
    app.run(debug=True)
