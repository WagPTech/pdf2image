import os
from pdf2image import convert_from_path

# Local da pasta onde estão os arquivos PDF
folder = "f:/folder"

# Iterar por todos os arquivos na pasta
for filename in os.listdir(folder):
    # Verificar se o arquivo é um PDF
    if filename.endswith(".pdf"):
        print(filename)
        # Caminho completo para o arquivo PDF
        filepath = os.path.join(folder, filename)
        # Converter o arquivo PDF em uma lista de imagens
        images = convert_from_path(filepath, 500,poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')
        # Iterar por todas as páginas do PDF
        for i, image in enumerate(images):
            # Salvar a imagem como um arquivo PNG
            image.save(f"{os.path.splitext(filename)[0]}_page_{i + 1}.png", "PNG")
