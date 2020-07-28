# main
Pasta principal que contêm os códigos do eye tracker. Aqui encontramos os seguintes arquivos:

## eye
Arquivo principal do projeto. Para a detecção e rastreamento da pupila é necessário primeiramente detectar a região da face e em seguida a dos olhos. Para realizar está tarefa estamos utilizando o algoritmo Violao-Jones, uma descrição desta tecnica pode ser encontrada no link:<_https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html?highlight=viola%20jones_ >. Os classificadores podem ser encontrados na pasta 'haarcascades'. Após a identificação da face e dos olhos é detectado a pupila pelo algoritmo de Blob.

## dot
Este arquivo quando importado cria uma janela gráfica de fundo branco contendo um ponto vermelho na tela. A ação do objeto em cena é dado pela seguinte função:
```python
def move_dot()
```
Que realiza o movimento no ponto no eixo x de maneira randômica.

Para sair da janela é só fazer a chamada do método:
```python
def exit_window()
```

## blob
A detecção de Blob atua identificando regiões da imagem que apresentam um conjunto de peculiaridades(cor, área, circularidade, convexidade, Por razão da inércia mínima para a inércia máxima, ...).

Neste arquivo não definimos os parâmetros do detector Blob, está parte está contido no arquivo principal do projeto. Nesse arquivo há apenas o método de detecção.

```python
def blob_process(img, detector, threshold)
```
### Argumentos
- _img_:

A imagem que será feita a detecção.

- _detector_:

Este argumento é informado o detector Blob. Este objeto é criado após definir os parâmetros para a detecção Blob.

- _threshold_:

Valor da binarização.

Neste método é preciso ser feito um tratamento de erosão, dilatação e suavização por média na imagem.
```python
cv2.erode(img, None, iterations=2)
```
- Método de erosão da imagem. Aqui é retirado ruídos brancos da imagem e realiza a desconexão de dois objetos conectados.
```python 
cv2.dilate(img, None, iterations=4) 
```
- Método de dilatação da imagem. Uma vez chamado o método de erosão, o objeto de busca tende a diminuir o seu tamanho e para que isso não ocorra chamamos este método para dilatar os objetos em cena.
```python
cv2.medianBlur(img, length)
```
- Método de suavização por média da imagem. Está tecnica altera o valor atribuido ao pixel pelo cálculo de média simples dos pixels adjacentes e do valor original do pixel central, para isso ocorrer inicialmente definimos uma sub-matriz de tamanho 'length x length'(segundo argumento do método). A operação de troca de valor é feita no pixel central.

## cutEye
Apresenta o método que recorta 25% da parte superior da imagem. Isto corresponde a sobrancelha. Devemos retirar está parte da imagem para não ocorrer algum tipo de empecilho na etapa de binarização.
```python
def cut_eyebrows(img)
```
É passado como argumento apenas a imagem e retorna o mesmo objeto após o procedimento feito. 

## cutImg
Apresenta um método que faz um recorte da região de alguma parte da imagem e salva o objeto na pasta informada. Teve como finalidade salvar a imagem da região dos olhos para a realização de testes de algoritmos.

```python
def salveSubImg(x, y, w, h, image, ROI_number=0, folder='')
```
- _x_:

Posição 'x' do elemento na imagem.

- _y_:

Posição 'y' do elemento na imagem.

- _w_:

Valor que corresponde a largura da imagem. 

- _h_:

Valor que corresponde a altura da imagem.

- _image_:

Imagem que será feita o recorte.

- _ROI_number_:

Número que corresponde ao índice da imagem. Assume como padrão o valor 0.

Valor 
- _folder_:

Nome da pasta onde será salva a imagem.

## lut
Apresenta um método que aplica uma _Look up Table_ (LUT) e retorna a mesma imagem clareada.

```python
def adjust_gamma(image, gamma=1.0)
```
É passado como argumento a imagem e a variavel 'gamma' que assume como valor padrão 1.

## pathFile
Apresenta um método que retorno o caminho de um arquivo. É passado como argumento o nome do arquivo.

```python
def path(file)
```
## getCircle
Apresenta o método de segmentação por borda Hough Circle. Está foi a primeira ideia para a segmentação da pupila.

```python
def circle(img, dp, minDist, param_1, param_2, minR=0, maxR=0, condGray=True)
```
### Argumentos
- _img_:

A imagem que será feita a leitura dos circulos.

- _dp_:

Parâmetro que vota se a imagem apresenta ou não um circulo.

- _minDist_:

Valor mínimo para a distância entre os circulos

- _param_1_:

Valor passado na borda Canny.
```python
cv2.Canny(img, param_1, param_1/2)
```
- _param_2_: 

Valor do acumulador de threshold.

- _minR_:

Valor mínimo de busca do raio do círculo.

- _maxR_:

Valor máximo de busca do raio do círculo.

- _condGray_:

Este argumento deve assumir valor 'False' caso a imagem já esteja em escala de cinza.

O retorno deste método é uma tupla com três valores correspondendo a posição do circulo e o raio da circunferência. 