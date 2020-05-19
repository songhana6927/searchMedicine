from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/student')
def student():
    return render_template('/student.html')


@app.route('/student_result', methods=['POST', 'GET'])
def student_result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)