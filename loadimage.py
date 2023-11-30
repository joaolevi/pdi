import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path: str, name: str):

    caminho_da_imagem = path + name
    try:
        imagem = cv2.imread(caminho_da_imagem)
        imagem2 = cv2.imread(path+"arvores-pb.jpg")
        array_numpy = np.array(imagem)
        print(f"Array length {array_numpy.shape}")

        tipo_imagem = imagem.dtype
        print(f"Tipo de dados original: {tipo_imagem}")

        imagem_uint8 = imagem.astype(np.uint8)
        imagem_uint16 = imagem.astype(np.uint16)
        imagem_float = imagem.astype(np.float32)

        imagem2_uint8 = imagem2.astype(np.uint8)

        # Analisar os tipos de dados após a conversão
        print(f"Tipo de dados após conversão para uint8: {imagem_uint8.dtype}")
        print(f"Tipo de dados após conversão para uint16: {imagem_uint16.dtype}")
        print(f"Tipo de dados após conversão para float32: {imagem_float.dtype}")

        fator_escala = 1.5
        imagem_scaled = (imagem_float + imagem2_uint8).astype(np.uint8)

        cv2.imshow('Imagem Original', imagem)
        cv2.imshow('Imagem Escalada', imagem_scaled)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Erro ao carregar a imagem. Err: "+str(e))

def matrizes_opencv():
    # Criar duas matrizes no NumPy
    matrix_uint16 = np.random.randint(0, 65536, size=(600, 600), dtype=np.uint16)

# Gere uma matriz float 600x600 com valores entre 0 e 1
    matrix_float = np.random.rand(600, 600).astype(np.float32)

    # Multiplicar as matrizes
    result_matrix = np.dot(matrix_uint16, matrix_float)

    # Exibir as matrizes originais e a resultante usando o OpenCV
    print("Matrix A:")
    print(matrix_uint16)

    print("\nMatrix B:")
    print(matrix_float)

    print("\nResult Matrix:")
    print(result_matrix)

    # # Exibir as matrizes usando o OpenCV
    # cv2.imshow('Matrix A', matrix_uint16)
    # cv2.imshow('Matrix B', matrix_float)
    # cv2.imshow('Result Matrix', result_matrix)

    # # Aguardar até que uma tecla seja pressionada
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Exiba as matrizes geradas usando Matplotlib
    plt.figure(figsize=(12, 4))

    # Subplot para a matriz uint16
    plt.subplot(1, 3, 1)
    plt.imshow(matrix_uint16, cmap='viridis', interpolation='none')
    plt.title('Matriz uint16')
    plt.colorbar()

    # Subplot para a matriz float
    plt.subplot(1, 3, 2)
    plt.imshow(matrix_float, cmap='viridis', interpolation='none')
    plt.title('Matriz float')
    plt.colorbar()

        # Subplot para a matriz float
    plt.subplot(1, 3, 3)
    plt.imshow(result_matrix, cmap='viridis', interpolation='none')
    plt.title('Result Matrix')
    plt.colorbar()

    # Ajuste de layout para evitar sobreposição
    plt.tight_layout()

    # Exiba as figuras
    plt.show()



if __name__ == "__main__":
    path = './images/'
    img1_name = "arvores-pb.jpg"
    img2_name = "cachorro-pb.jpg"
    img3_name = "cidade-pb.webp"
    img4_name = "olho-pb.jpg"

    # load_image(path=path, name=img1_name)
    # load_image(path=path, name=img2_name)
    # load_image(path=path, name=img3_name)
    # load_image(path=path, name=img4_name)

    # matrizes()
    matrizes_opencv()