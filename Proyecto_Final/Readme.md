# Proyecto Final Style Transfer
La idea de este Trabajo Práctico Final es reproducir el siguiente paper:
[A Neural Algorithm of Artistic Style](https://arxiv.org/pdf/1508.06576.pdf).

Cuyo objetivo es, a partir de dos imágenes (**una que aporte el estilo y otra que aporte el contenido**) analizar cómo es la _activación_ de las _primeras capas_ para la imagen que aporta el **estilo** y cómo es la _activación_ de las _últimas capas_ de la red convolucional para la imagen que aporta el **contenido**. A partir de esto se intentará sintetizar una imagen que active los filtros de las primeras capas que se activaron con la imagen que aporta el estilo y los filtros de las últimas capas que se activaron con la imagen que aporta el contenido.

A este _procedimiento_ se lo denomina **_Neural Style Transfer_**.

