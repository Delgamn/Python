import pathlib
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

#Путь папки для загрузки
UPLOAD_FOLDER = 'C:\\Users\\svyat\\OneDrive\\Рабочий стол\\'
#Разрешённые форматы
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
#Изменение параметра конфига
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Создание секретного ключа, для того чтобы работал flash
app.secret_key = 'many random bytes'

def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(pathlib.Path(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', name=filename))
    return render_template('Home.html')


if __name__ == '__main__':
    app.run(debug=True)
