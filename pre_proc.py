# 1. Importação das Bibliotecas
import os
import numpy as np
import pandas as pd
from keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split

# 2. Carregar Dados de Emoções (FER2013)
def carregar_dados_de_emocoes(fer2013_csv_path):
    data = pd.read_csv(fer2013_csv_path)
    images = []
    labels = []
    for index, row in data.iterrows():
        pixels = np.fromstring(row['pixels'], sep=' ').astype('float32').reshape(48, 48)
        images.append(pixels)
        labels.append(row['emotion'])
    images = np.array(images)
    labels = np.array(labels)
    images = images / 255.0
    return images, labels

# Uso da função
x_train_emotions, y_train_emotions = carregar_dados_de_emocoes('fer2013.csv')

# 3. Carregar Dados de Idade (UTKFace)
def carregar_dados_de_idade(utkface_folder_path):
    images = []
    ages = []
    for filename in os.listdir(utkface_folder_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(utkface_folder_path, filename)
            img = load_img(img_path, target_size=(200, 200))
            img_array = img_to_array(img)
            images.append(img_array)
            age = int(filename.split('_')[0])
            ages.append(age)
    images = np.array(images)
    ages = np.array(ages)
    images = images / 255.0
    return images, ages

# Uso da função
x_train_age, y_train_age = carregar_dados_de_idade('caminho/para/utkface/')

# 4. Divisão dos Dados
x_train_emotions, x_test_emotions, y_train_emotions, y_test_emotions = train_test_split(
    x_train_emotions, y_train_emotions, test_size=0.2, random_state=42
)

x_train_age, x_test_age, y_train_age, y_test_age = train_test_split(
    x_train_age, y_train_age, test_size=0.2, random_state=42
)
