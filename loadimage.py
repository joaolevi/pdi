import cv2
import numpy as np

def load_image(path: str, name: str):

    caminho_da_imagem = path + name
    try:
        imagem = cv2.imread(caminho_da_imagem)
        array_numpy = np.array(imagem)
        print(f"Array length {array_numpy.shape}")

        tipo_imagem = imagem.dtype
        print(f"Tipo de dados original: {tipo_imagem}")

        imagem_uint8 = imagem.astype(np.uint8)
        imagem_uint16 = imagem.astype(np.uint16)
        imagem_float = imagem.astype(np.float32)

        # Analisar os tipos de dados após a conversão
        print(f"Tipo de dados após conversão para uint8: {imagem_uint8.dtype}")
        print(f"Tipo de dados após conversão para uint16: {imagem_uint16.dtype}")
        print(f"Tipo de dados após conversão para float32: {imagem_float.dtype}")

        fator_escala = 1.5
        imagem_scaled = (imagem_float * fator_escala).astype(np.uint8)

        cv2.imshow('Imagem Original', imagem)
        cv2.imshow('Imagem Escalada', imagem_scaled)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Erro ao carregar a imagem. Err: "+str(e))



if __name__ == "__main__":
    path = './images/'
    img1_name = "arvores-pb.jpg"
    img2_name = "cachorro-pb.jpg"
    img3_name = "cidade-pb.webp"
    img4_name = "olho-pb.jpg"

    # load_image(path=path, name=img1_name)
    load_image(path=path, name=img2_name)
    # load_image(path=path, name=img3_name)
    # load_image(path=path, name=img4_name)