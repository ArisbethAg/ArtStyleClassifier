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
  - **Validation:** 111 (10%)
- **Test:** 479 (30%)

**Pinturas no-impresionistas:**

- **Train:** 1081 (70%)
  - **Validation:** 108 (10%)
- **Test:** 464 (30%)

[Link del dataset actualizado (Google Drive)](https://drive.google.com/drive/folders/13U8wAopsLEXEF5I0QQ_WmhCwxb_A8Uqy?usp=sharing)

## Preprocesamiento de los datos

Se aplicó un redimensionamiento de 150x150 píxeles y se normalizaron las imágenes para que sus píxeles solamente tengan valores de 0 a 1.

También, a partir del set de train, se generaron nuevas imágenes. De forma más específica, un batch de 32 por cada época y con un rango de rotación de 20, un rango de brillo entre 0.8 - 1, y con posibilidad de cambiar su orientación vertical y horizontal.

## Validación de los datos

Se creó una carpeta de validación, en donde el 15% de los datos del set de train fueron almacenados. Para este set de imágenes también se aplicó un preprocesamiento a las imágenes para redimensionarlas y normalizarlas.

## Implementación del modelo

Para la implementación del modelo revise los siguientes papers:

[Artistic Style Recognition: Combining Deep and Shallow Neural Networks for Painting Classification](https://www.mdpi.com/2227-7390/11/22/4564)

[Evaluation of CNN Models with Transfer Learning in Art Media Classification in Terms of Accuracy and Class Relationship](https://www.polibits.cidetec.ipn.mx/ojs/index.php/CyS/article/view/4895/3668)

[Attention-based VGG-16 model for COVID-19 chest X-ray image classification](https://link.springer.com/article/10.1007/s10489-020-02055-x)

Y con lo revisado implementé un modelo de transfer learning, tomando como modelo base una red neuronal VGG-16, pre-entrenada con ImageNet, sin incluir su última capa. A este modelo posteriormente le agregué una capa densa de 64 neuronas con activación ReLu, una capa de Dropout del 30% y por último una capa densa de 1 neurona con activación sigmoid para hacer la clasificación entre pinturas impresionistas y no impresionistas.

Este modelo, posteriormente fue entrenado a lo largo de 10 épocas, obteniendo como resultado las siguientes métricas:

- **loss:** 0.4573
- **accuracy:** 0.7816
- **validation loss:** 0.4764
- **validation accuracy:** 0.7626

## Testing del modelo

En esta parte, usando el dataset de test, se evalúo el modelo con 25 steps y se obtuvo el siguiente resultado:

- **accuracy:** 0.6162

## Evaluación del modelo

Para evaluar el modelo, tome como referencia el siguiente paper:

[Artistic Style Recognition: Combining Deep and Shallow Neural Networks for Painting Classification](https://www.mdpi.com/2227-7390/11/22/4564)

En él, se mencionan las métricas de precision, recall y f1 score, e investigando más fondo estás se pueden definir de la siguiente manera:

- **Precision:** Una métrica para observar cuantas de las predicciones positivas son correctas. Se centra en la calidad de las predicciones positivas del modelo.

- **Recall:** También llamada Sensitivity, es una métrica para observar cuantos de los casos positivos el modelo clasificó correctamente.

- **F1 score:** Es una métrica que evalúa la eficiencia general del modelo combinando la precision y el recall. En otras palabras es el promedio armónico de la precision y el recall para medir la capacidad del modelo para ser preciso y completo al mismoo tiempo.

Tomando esto en cuenta, realicé la evaluación del modelo, obteniendo los siguientes resultados:

- **Precision:** 0.4864516129032258
- **Recall:** 0.8125
- **F1 score:** 0.6085552865213883

Con lo que se puede observar que el modelo tiene un muy buen recall pero que, en contraste, no tiene muy buena precisión y observando la matriz de confusión:

```
          label pos   label neg
pred pos     81           377
pred neg     398          87

```

Podemos ver que de las positivas todas las identificó correctamente, sin embargo de las negativas, clasficó la mayoría como positivas, con lo que podemos concluir en que el modelo se encuentra con overfitting.
