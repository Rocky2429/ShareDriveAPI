from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_robocopy():
    robocopy_cmd = ""
    if request.method == 'POST':
        source = request.form['source'].strip()
        destination = request.form['destination'].strip()
        ticket = request.form['ticket'].strip()

        # Add quotes around paths in case they have spaces
        robocopy_cmd = f'robocopy "{source}" "{destination}" /COPY:DATS /MIR /R:3 /W:5 /LOG:C:\\Logs\\{ticket}_robocopy.log'

    return render_template('form.html', robocopy_cmd=robocopy_cmd)

if __name__ == '__main__':
    app.run(debug=True)
