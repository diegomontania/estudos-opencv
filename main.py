import cv2

def exibeJanela(imagem):
    cv2.imshow('janela de imagem', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    #carregando imagem
    #imagem pode ser carregadas como 'cv2.IMRED_COLOR' : -1, 'cv2.IMRED_GRAYSCALE' : 0, e 'cv2.IMRED_UNCHANGED' : 1 (com transparencia)
    #img = cv2.imread('assets/image.jpg', -1)
    #img = cv2.imread('assets/image.jpg', 0)
    img = cv2.imread('assets/image.jpg', 1)

    #redimensionando imagem
    img = cv2.resize(img, (200, 200))

    #rotacionando
    img = cv2.rotate(img, cv2.cv2.ROTATE_180)

    # exibindo imagem em uma janela
    exibeJanela(img)

    #salvando o arquivo no mesmo caminho do anterior
    cv2.imwrite('nova_imagem.jpg', img);

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
