import numpy as np
import tensorflow as tf

def generate_data(samples=500):
    X, y = [], []
    for _ in range(samples):
        good = np.random.normal(loc=[0, 9.8, 0, 0, 0, 0], scale=0.5)
        X.append(good)
        y.append([1, 0])
        bad = np.random.normal(loc=[2, 7, 1, 0.5, -0.3, 0.8], scale=1.0)
        X.append(bad)
        y.append([0, 1])
    return np.array(X), np.array(y)

X, y = generate_data()

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(6,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(6, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=30, batch_size=16)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("posture_model.tflite", "wb") as f:
    f.write(tflite_model)
