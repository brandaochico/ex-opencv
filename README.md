# Processamento de Imagens - OpenCV
### Exercício de OpenCV em Python para a cadeira de Processamento de Imagens, Unilasalle.

## <u>Dataset escolhido:</u> [RVL CDIP small](https://www.kaggle.com/datasets/uditamin/rvl-cdip-small/)

### Alunos e Funções:
* Francisco Brandão
> Codificação do processamento das imagens.
* Leandro Pinzon Filho
> Pesquisa e ideia de problema.
* Marcus Apolinário
> Pesquisa e ideia de problema.

## Problema
O problema escolhido para resolver foi o de identificação e separação de documentos vazios e escritos.
O dataset possui uma grande biblioteca de documentos que variam de formulários, cartas, artigos científicos, até e-mails.
Por não possuir nenhum documento em branco, foram geradas vinte imagens vazias para realizar esta comparação (arquivo [blank.py](https://github.com/brandaochico/ex-opencv/blob/main/blank.py)).

## Resolução
### Técnicas utilizadas:
* Conversão para escala de cinza (grayscale);
> Para facilitar a leitura e compreensão das imagens.
* Reescalonamento (resizing);
> Para padronizar os documentos.
* Identificação de bordas (canny);
> Para identificação de presença de textos.
* Contornos (contours);
> Para contagem de bordas presentes.
* Conversão para escala BGR (cvtColor);
> Para mostrar a imagem nas cores originais.
* Impressão de texto nas imagens (putText).
> Para identificação e separação de classes diferentes de documentos.
