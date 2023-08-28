from flask import Flask,render_template
app=Flask(__name__)

post =[
    {
        "name":"Masresha",
        "age":"22",
        "data":"2021"
    },
      {
        "name":"Masresha",
        "age":"22",
        "data":"2021"
    },
      {
        "name":"Masresha",
        "age":"22",
        "data":"2021"
    },
]

@app.route('/')
def Hello():
    return render_template('home.html',post=post,title="home")


@app.route('/about')
def About():
    return render_template('about.html',title="about")

if __name__=='__main__':
    app.run(debug=True)