from flask import Flask, request, render_template
import numpy as np
#import tensorflow as tf
#from tensorflow import keras

app1 = Flask(__name__)


def processing_params(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10):
    #     TODO: Добавить логику модели
    model = tf.keras.load_model("D:\diploma\my_model")
    pred = model.predict([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10])
    message = f"Соотношение матрица-наполнитель = {pred}"
    return message


@app1.route('/test/', methods=['post', 'get'])
def test():
    message = ''
    if request.method == 'POST':
        param1 = request.form.get('param1')
        param2 = request.form.get('param2')
        param3 = request.form.get('param3')
        param4 = request.form.get('param4')
        param5 = request.form.get('param5')
        param6 = request.form.get('param6')
        param7 = request.form.get('param7')
        param8 = request.form.get('param8')
        param9 = request.form.get('param9')
        param10 = request.form.get('param10')

        #param1 = float(param1)
        #param2 = float(param2)
        #param3 = float(param3)
        #param4 = float(param4)
        #param5 = float(param5)
        #param6 = float(param6)
        #param7 = float(param7)
        #param8 = float(param8)
        #param9 = float(param9)
        #param10 = float(param10)

        message = 0
        #processing_params(param1, param2, param3, param4, param5, param6, param7, param8, param9, param10)

    return render_template('test.html', message=message)

if __name__ == '__main__':
    app1.run()
