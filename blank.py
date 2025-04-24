""" GERAR PÁGINAS EM BRANCO """

import cv2
import numpy as np
import os

output_dir = "data/blank"
os.makedirs(output_dir, exist_ok=True)

num_imagens = 20
altura = 800
largura = 600

for i in range(num_imagens):
    # Criar imagem branca 
    imagem = np.ones((altura, largura), dtype=np.uint8) * 255

    # Adicionar ruído leve 
    ruido = np.random.randint(0, 20, (altura, largura), dtype=np.uint8)
    imagem_ruidosa = cv2.subtract(imagem, ruido)

    caminho = os.path.join(output_dir, f"pagina_branca_{i+1}.jpg")
    cv2.imwrite(caminho, imagem_ruidosa)

print(f"{num_imagens} imagens em branco geradas em '{output_dir}'")
