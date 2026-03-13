---
title: TensorFlow Keras observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/tensorflow-keras-observability
scraped: 2026-03-06T21:33:34.751016
---

# Наблюдаемость TensorFlow Keras

# Наблюдаемость TensorFlow Keras

* Latest Dynatrace
* Руководство
* Чтение: 4 мин
* Опубликовано 6 июня 2023 г.

**TensorFlow** и его удобный **последовательный интерфейс Keras** представляют собой передовую технологию для обучения и запуска моделей глубокого обучения.

TensorFlow — это универсальный фреймворк машинного обучения, который позволяет специалистам по данным создавать, обучать и запускать различные модели ИИ на его основе.

TensorFlow также поставляется с удобным сервером отладки **TensorBoard**, который позволяет специалистам по данным собирать и визуализировать всю релевантную информацию об обучении, такую как логи, события и метрики, в веб-панели управления.

Ниже приведён пример скриншота TensorBoard и визуализации прогресса обучения модели:

![Визуализация обучения ИИ на базе TensorBoard](https://dt-cdn.net/images/tensorboard-1600-04dc516f95.png)

Хотя TensorBoard является отличным инструментом для локальной отладки модели ИИ, он не подходит для долгосрочной наблюдаемости работающей модели ИИ в продуктивной среде.

Поскольку сбор данных TensorBoard построен на основе **гибкого интерфейса обратных вызовов (callback) TensorFlow**, можно легко отправлять информацию о наблюдаемости работающей модели ИИ непосредственно в Dynatrace.

Всё, что необходимо, — это специализированная реализация обратного вызова TensorFlow, которая собирает данные и передаёт их в среду мониторинга Dynatrace.

## Обратный вызов (callback receiver) Dynatrace для TensorFlow

Реализация обратного вызова TensorFlow получает важные обновления информации во время фаз обучения и оценки модели.

Ниже приведена реализация обратного вызова Dynatrace для TensorFlow, который передаёт данные метрик во время обучения и оценки модели.

```
import tensorflow as tf



from tensorflow import keras



import requests



# Custom TensorFlow Keras callback receiver that sends the logged metrics



# to a Dynatrace monitoring environment.



# Read more about writing your own callback receiver here:



# https://www.tensorflow.org/guide/keras/custom_callback



class DynatraceKerasCallback(keras.callbacks.Callback):



metricprefix = ''



modelname = ''



url = ''



apitoken = ''



batch = ''



# Constructor that takes a metric prefix, the name of the current model that is used,



# the Dynatrace metric ingest API endpoint (e.g.: https://your.live.dynatrace.com/api/v2/metrics/ingest)



# and the Dynatrace API token (with metric ingest scope enabled)



def __init__(self, metricprefix='tensorflow.', modelname='', url='', apitoken=''):



self.metricprefix = metricprefix



self.modelname = modelname



self.url = url



self.apitoken = apitoken



def send_metric(self, name, value, tags):



tags_str = ''



for tag_key in tags:



tags_str = tags_str + ',{key}={value}'.format(key=tag_key, value=tags[tag_key])



line = '{prefix}.{name}{tags} {value}\n'.format(prefix=self.metricprefix, tags=tags_str, model=self.modelname, name=name, value=value)



self.batch = self.batch + line



def flush(self):



print(self.batch)



r = requests.post(self.url, headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + self.apitoken}, data=self.batch)



self.batch = ''



def on_train_end(self, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'train' })



self.flush()



def on_epoch_end(self, epoch, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'train' })



self.flush()



def on_test_end(self, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'test' })



self.flush()



def on_predict_end(self, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'predict' })



self.flush()
```

## Пример обучения и оценки модели Keras

В следующем примере модель Keras загружает известный набор данных (MNIST) и обучает последовательную модель Keras.

Настраивается обратный вызов Dynatrace для TensorFlow, который автоматически получает и передаёт метрики точности (accuracy) и потерь (loss) в настроенную среду мониторинга.

При продуктивном развёртывании модели (этап оценки) тот же обратный вызов Dynatrace используется для непрерывного получения данных наблюдаемости о работающей модели.

```
import tensorflow as tf



print("TensorFlow version:", tf.__version__)



import time



# load the Dynatrace callback receiver



from dynatrace import DynatraceKerasCallback



# Load a sample data set



mnist = tf.keras.datasets.mnist



(x_train, y_train), (x_test, y_test) = mnist.load_data()



x_train, x_test = x_train / 255.0, x_test / 255.0



# Define a model



model = tf.keras.models.Sequential([



tf.keras.layers.Flatten(input_shape=(28, 28)),



tf.keras.layers.Dense(128, activation='relu'),



tf.keras.layers.Dropout(0.2),



tf.keras.layers.Dense(10)



])



# Define a loss function



loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)



# Compile the model



model.compile(optimizer='adam',



loss=loss_fn,



metrics=['accuracy'])



# Define the tensor board callbacks



dt_callback = DynatraceKerasCallback(metricprefix='tensorflow', modelname='mnist-classifier', url='https://<YOUR_ENV>.live.dynatrace.com/api/v2/metrics/ingest', apitoken='<YOUR_TOKEN>')



# Train the model



model.fit(x_train, y_train, epochs=5, callbacks=[dt_callback])



# Use the model in production



while True:



model.evaluate(x_test,  y_test, verbose=2, callbacks=[dt_callback])



time.sleep(60)
```

## Визуализация метрик модели TensorFlow в Dynatrace

После регистрации обратного вызова Dynatrace для TensorFlow в вашей собственной модели ИИ все собранные метрики передаются в вашу среду мониторинга.

На скриншоте ниже показана визуализация метрики точности (accuracy) в Data Explorer, собранной с помощью обратного вызова TensorFlow:

![Наблюдаемость ИИ в Dynatrace для TensorFlow и Keras](https://dt-cdn.net/images/dynatrace-notebook-1920-31cf259f10.png)
