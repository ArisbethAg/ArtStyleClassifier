# Art Style Classifier

## TC3002B

### Arisbeth Aguirre Pontaza A01274803

## Documentación del Dataset

**Descripción:** Este dataset contiene imágenes de diversas pinturas que pertenecen a la corriente del impresionismo o a otras corrientes artísticas.

**Fuente del Dataset:** El dataset original fue obtenido de Kaggle, [Best Artworks of All Time](https://www.kaggle.com/datasets/ikarus777/best-artworks-of-all-time/data). Sin embargo, este fue modificado por mí el 13 de abril del 2024.

**Autores:** [Icaro](https://www.kaggle.com/ikarus777), [artchallenge.ru](https://artchallenge.ru/?lang=en)

**Información Relevante:** La estructura inicial del dataset fue modificada, dividiendo a todos los trabajos de los artistas impresionistas de los de otras corrientes, para así poder identificar dicho estilo artístico de forma más fácil.

**Tamaño del dataset:**

- **Pinturas impresionistas:** 1595 (50.8%)
- **Pinturas de otras corrientes artísticas (no-impresionistas):** 1545 (49.2%)

**Distribución del dataset:**
La distribución del dataset fue hecha de forma aleatoria usando el script anexo randomized_images.py

**Pinturas impresionistas:**

- **Train:** 1116 (70%)
  - **Validation:** 111(15%)
- **Test:** 479 (30%)

**Pinturas no-impresionistas:**

- **Train:** 1081 (70%)
  - **Validation:** 108(15%)
- **Test:** 464 (30%)

[Link del dataset actualizado (Google Drive)](https://drive.google.com/drive/folders/13U8wAopsLEXEF5I0QQ_WmhCwxb_A8Uqy?usp=sharing)

## Preprocesamiento de los datos

Se aplicó un redimensionamiento de 150x150 píxeles y se normalizaron las imágenes para que sus píxeles solamente tengan valores de 0 a 1.
