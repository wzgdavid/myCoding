from flask import Flask, request, session, g, make_response, redirect, url_for, abort, render_template, send_file, \
    flash, json, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('login post')
    else:
        print('login get')
    return ' login ?'


@app.route('/template/')
@app.route('/template/<name>')
def template(name=None):
    return render_template('hello.html', name=name)


@app.route('/returnjson')
def returnjson():
    return json.dumps({'name':'wzg', 'age':30})


@app.route('/test')
def test():
    '''
    template and dict
    '''
    data={'name':'wzg', 'age':30}
    return render_template('hello.html', data=data)


@app.route('/test2')
def test2():
    '''
    template and object
    '''
    class Person(object):
        """docstring for Person"""
        def __init__(self, name, age):
            super(Person, self).__init__()
            self.name = name
            self.age = age
            
    person = Person('jimi', 300)
    return render_template('hello.html', person=person)


@app.route('/test3')
def test3():
    '''
    list and object
    '''
    class Person(object):
        """docstring for Person"""
        def __init__(self, name, age):
            super(Person, self).__init__()
            self.name = name
            self.age = age
            
    persons = [Person('jimi', 300), Person('tom', 400)]
    return render_template('hello.html', persons=persons)


@app.route('/testaction', methods=['POST'])
def testaction():
    data = {}
    data['rjson'] = request.get_json()
    data['name'] = request.form['user']
    print(data)
    return json.dumps(data)
    #return render_template('temp/visitor_summary.html', data=data)

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/post_params', methods=['POST'])
def post_params():
    data = request.get_json()
    print(data)
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)