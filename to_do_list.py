"""
Final Project

Gawa kayo ng medyo exciting na python program. Hanap kayo ng any existing python project sa youtube na interesting para sa inyo. Gawin nyo yung project tapos pag gumagana na gawan nyo ng demo.

Pag send nyo ng demo sakin, kindly add some details on chat kung saan nyo pweding iapply ung natutunan nyo sa project na sinundan nyo.
Please walang magda-download ng source code. Kaylangan nyong itype at mag git commit pa din every small milestone.
Push nyo yung code sa github. Lagay nyo sa README yung youtube link or icomment nyo sa code to give credit.
Send the demo/link to my messenger before Feb 3.
"""

#create a to do list located in a website using python and html

#create a function that could input a to do
#create a function that could delete inputed to do
#create a function that could edit a to do

#create a checker that is interactable with the user to checkoff the to do

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

todos = [{"task": "Sample Todo", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["post"])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)