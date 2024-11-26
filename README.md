# Reconhecimento de Emoções com Webcam

Este projeto implementa um sistema de reconhecimento de emoções em tempo real utilizando redes neurais convolucionais (CNNs) e a webcam do usuário. Foi desenvolvido para identificar emoções humanas com base em expressões faciais, oferecendo insights sobre o uso de aprendizado profundo no reconhecimento facial.

## 📋 Funcionalidades

- Captura de vídeo em tempo real via webcam.
- Reconhecimento de emoções básicas (alegria, tristeza, raiva, surpresa, neutro, etc.).
- Visualização direta das emoções detectadas na tela.
- Estrutura modular e fácil de modificar para incluir novas emoções ou ajustar modelos.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Frameworks:** TensorFlow/Keras, OpenCV
- **Bibliotecas:** NumPy, Matplotlib
- **Modelo de Rede Neural:** CNN treinada em dataset de expressões faciais (Ex.: FER2013 ou outro dataset de emoções).

⚙️ Treinamento de Modelo (Opcional)
Se desejar treinar seu próprio modelo, use o script em train_model.py e insira seu dataset em datasets. Certifique-se de que o dataset esteja formatado corretamente.

🖼️ Exemplo de Uso

O sistema identifica a emoção e exibe as informações na tela em tempo real.

🧪 Possíveis Melhorias
Implementar suporte a múltiplas emoções personalizadas.
Adicionar suporte para reconhecimento de gênero ou faixa etária.
Treinar o modelo com datasets maiores para maior precisão.
📝 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

