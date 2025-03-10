from langchain_community.document_loaders import CSVLoader
import os

data_dir = 'data'

# Iterar sobre los archivos en el directorio de datos
for filename in os.listdir(data_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_dir, filename)
        loader = CSVLoader(file_path, encoding="utf-8")
        documentos = loader.load()
        print("TYPE:", type(documentos))


for i,doc in enumerate(documentos, start=1):
    print(f"documento {i}: \n", doc)

print("Fin de la carga de documentos")
    