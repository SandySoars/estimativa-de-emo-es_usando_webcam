# Reconhecimento de Emoções 
Este projeto implementa um sistema que reconhece emoções em tempo real utilizando redes neurais convolucionais (CNNs) e a webcam.

## 📋 Funcionalidades

- Reconhecimento de emoções com base em expressões faciais.
- Captura de vídeo em tempo real via webcam.
- Modularidade para incluir novos modelos ou funcionalidades.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Frameworks:** TensorFlow/Keras, OpenCV
- **Bibliotecas:** NumPy, json
- **Dataset:** FER2013 para treinamento.

🚀 Como Executar o Projeto
1️⃣ Pré-processar os Dados
Execute o script pre_proc.py para preparar o dataset FER2013. Certifique-se de configurar corretamente o caminho para o arquivo CSV no script.
python pre_proc.py
2️⃣ Treinar o Modelo
Treine o modelo utilizando o script train_model.py. Os arquivos gerados, como a arquitetura do modelo (.json) e os pesos (.h5), serão salvos automaticamente no diretório principal.
python train_model.py
3️⃣ Testar o Modelo com a Webcam
Use o script test_model.py para realizar o reconhecimento de emoções em tempo real. Certifique-se de que os arquivos do modelo (modelo_classificacao_emocao.json, modelo_classificacao_emocao.weights.h5) e o arquivo de rótulos (rotulos.txt) estejam no mesmo diretório.
python test_model.py
## Dica: Pressione Esc para encerrar a aplicação.

🌟 Possíveis Melhorias
Ajustar para diferentes condições de iluminação.
Adicionar suporte para mais categorias de emoções.
Otimizar o desempenho para dispositivos com hardware limitado.
🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request.



