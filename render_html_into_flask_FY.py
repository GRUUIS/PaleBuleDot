from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def get_html():
    return render_template('jump_to_mypage.html')


@app.route('/index2', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('jump_to_mypage'))

    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
