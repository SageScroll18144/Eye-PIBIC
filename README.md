# PIBIC-Eye
Repositório sobre o projeto de pesquisa PIBIC-EM envolvendo o uso de uma webcam para o rastreio dos olhos e com base no tempo de reação do usuário, deslocando um ponto na tela, é determinado se há algum tipo de patologia apresentada pelo paciente, tais como, Parkinson, transtornos do espectro autista e Alzheimer.

- Desenvolvedor.: [Felipe Santos](https://github.com/SageScroll18144)

## Estrutura
- Para a captura, tratamento e aplicação das técnicas de Processamento de Imagem, está sendo usado a biblioteca OpenCV.
- A parte gráfica do ponto é feita em Pygame.

## Processamento de Imagem
Na primeira parte é identificado a região da face e dos olhos pela técnica Viola-Jones. A identificação e captura da posição da pupila é feita pelo Algoritmo Blob. 

## Retorno 
O programa retorna o tempo de reação do usuário desde o deslocamento do ponto até o alinhamento entre o olho e o objeto.
~(Ainda escrever essa parte mais detalhada)~

## Código do Projeto
Este projeto contêm duas pastas que apresentam arquivos com códigos.

- main:
Aqui está contido todos os códigos principais do projeto.

- algoritmos:
Está é uma pasta que apresenta apenas códigos de testes de algoritmos.