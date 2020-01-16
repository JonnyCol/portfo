from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
# print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page>")
def html_page(page):
    return render_template(page)


def write_to_file(data):
    with open("database.txt", mode="a") as my_data:
        # my_data.write(data + "\n")
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        my_data.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", newline="", mode="a") as my_data2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(my_data2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect("/thank_you.html")
        except:
            return "Did not save to database"
    else:
        return "Something went wrong. Try again"


if __name__ == "__main__":
    app.run(debug=True)git
