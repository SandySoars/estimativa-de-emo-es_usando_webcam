import numpy as np
import cv2
import keras
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from pathlib import Path

# Supondo que você tenha um conjunto de dados de emoções e idade carregado
# x_train, y_train = carregar_dados_de_emocoes()  # Função fictícia para carregar os dados
# x_test, y_test = carregar_dados_de_idade()  # Função fictícia para carregar os dados

# Normalizar o dataset para valores entre 0 e 1
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Converter os vetores de classe para matrizes de classe binária
y_train_emotion = keras.utils.to_categorical(y_train_emotion, num_classes_emotions)
y_test_emotion = keras.utils.to_categorical(y_test_emotion, num_classes_emotions)

y_train_age = keras.utils.to_categorical(y_train_age, num_classes_age)
y_test_age = keras.utils.to_categorical(y_test_age, num_classes_age)

# Criar o modelo
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=(48, 48, 1), activation="relu"))
model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Adicionar mais camadas conforme necessário...
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes_emotions, activation="softmax"))  # Saída para emoções
# model.add(Dense(num_classes_age, activation="softmax"))  # Saída para idade, se necessário

# Compilar o modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinamento do modelo
model.fit(
    x_train,
    y_train_emotion,  # Treinando para emoções, você pode ajustar para idade
    batch_size=64,
    epochs=20,
    validation_data=(x_test, y_test_emotion),
    shuffle=True
)

# Salvar o modelo
model.save('modelo_emocoes.h5')
