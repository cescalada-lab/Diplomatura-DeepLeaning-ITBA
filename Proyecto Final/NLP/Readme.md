# **Proyecto Final Bioinformática**

El objetivo del proyecto es **entender** la bioactividad de una _**molécula**_ (molecule_chembl_id) sobre una _**enzima**_ (Acetylcholinesterase), medida a través del _**indicador IC50**_ (standard_value).

Para lograrlo, se trabajó con los **_smiles de la fórmula química de las moléculas_** con **_técnicas de NLP_**: Principalmente la utilización de redes neuronales **LSTM** y de arquitecturas de **Text CNN**.

En la **Notebook 1**, se realiza un pre-procesamiento básico de los Datos. 

En la **Notebook 2**, se realiza un brebe Análisis y exploración básica de los Datos.

En la **Notebook 3**, se experimenta con varias arquitecturas de redes LSTM, Bidirectional y GRU.

En la **Notebook 4**, se experimenta con varias posibilidades de arquitecturas de text CNN.

En la **Notebook 5**, se hace una exploración de los embeddings entrenados en un modelo de Bidirectional + LSTM,  mediante una representación en dos dimensiones obtenida a través de TSNE para interpretar espacialmente la ubicación de los embeddings.

En la **Notebook 6**, se prueba una arquitectura prearmada para entender cómo performa.

