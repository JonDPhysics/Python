from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def play_color(num=3,color="dodgerblue"):
    return render_template('indexPlayColor.html', box_num = num, box_color = color)

if __name__=="__main__":
    app.run(debug=True)