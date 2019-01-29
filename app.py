from flask import Flask, render_template, flash, request
import pywikibot
from pywikibot import pagegenerators

# source venv/bin/activate
app = Flask(__name__)
app.debug = True

####################

@app.route("/", methods=['GET', 'POST'])
def entry():

    print("yolo")
    return render_template('template.html')

####################

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        path = request.form['PATH']
        print (path)
        blue = request.form['BLUE']
        print(blue)
        site = pywikibot.Site('fr', u'wiktionary')
        page = pywikibot.Page(site, path)
        message1 = ""
        if not page.exists():
            message1 = "La page indiquée n'existe pas : " + page.title()
            return render_template("result.html", MSG1=message1, MSG2="")
        else:
            message1 = page.title()
            links = page.linkedPages()
            message2 = ""
            for link in links:
                print (link.namespace())
                if link.namespace() == "":
                    if (blue == "on"):
                        if link.exists():
                            message2 += link.title() + "#"
                    else:
                        message2 += link.title()  + "#"
    return render_template("result.html", MSG1=message1, MSG2=message2)

####################

if __name__ == '__main__':
    app.run()