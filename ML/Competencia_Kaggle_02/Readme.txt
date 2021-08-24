Competencia N°2 Kaggle: 

Rossmann Store Sales

Se tiene que participar en la siguiente competencia de Kaggle:

https://www.kaggle.com/c/rossmann-store-sales

El objetivo de esta competencia es predecir las ventas futuras para una cadena de supermercado.
Para ello armamos una notebook con embeddings, configuramos y probamos: lr, epochs,batch size, cantidad de hidden layes, regularización L2, normalización de datos, tipos de funciones de activación, etc.
En Kaggle la métrica que se pidió en la competencia era el RMSE y a mi me dió 0.131 en el private score.

*Cabe aclarar que solo subo la notebook final, sin los archivos: train_normalized_data.fth y test_normalized_data.fth que contienen los datos ya pre procesados y normalizados en otra notebook, esto se debe a que estos archivos superan el tamaño máximo permitido de almacenamiento de Git y todavía no vimos cómo usar y configurar Git LFS para almacenar grandes volúmenes de datos.