""" PROCESSAMENTO DE IMAGENS """

import cv2 as cv

def process_image(path):
    # Conversão imediata da imagem para escala de cinza
    """ GRAYSCALE """
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)

    # Reescalonamento
    """ RESIZING """
    resized = cv.resize(img, (400, 600))

    # Bordas 
    """ CANNY """ 
    canny_edges = cv.Canny(resized, 125, 175)

    # Contornos
    """ CONTOURS """
    contours, hierarchies = cv.findContours(canny_edges.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    # Se tiver menos de 10 contornos, seta a cor do texto como VERMELHO
    # Se tiver mais de 10 contornos, seta a cor do texto como VERDE
    # Conforme o espaço de cores BGR (blue, green, red)
    if len(contours) < 10:
        img_class = 'VAZIA'
        text_color = (0,0,255)
    else: 
        img_class = 'COM TEXTO'
        text_color = (0,255,0)

    # Conversão de volta para escala BGR
    """ BGR """
    bgr = cv.cvtColor(resized, cv.COLOR_GRAY2BGR)

    """ PUT TEXT """
    cv.putText(bgr, f"{img_class}", (30,50), cv.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
    
    return bgr, canny_edges, img_class, len(contours)