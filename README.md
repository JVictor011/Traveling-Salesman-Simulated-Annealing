# Traveling Salesman Problem - Simulated Annealing

## Descrição

Este projeto implementa uma solução para o Problema do Caixeiro Viajante (TSP) utilizando o algoritmo de Simulated Annealing. O TSP é um problema clássico de otimização que busca encontrar o menor caminho possível que visita um conjunto de cidades e retorna à cidade de origem, minimizando a distância total percorrida.

## Funcionalidades

- **Algoritmo Simulated Annealing**: Implementação eficiente do algoritmo para resolver o TSP.
- **Leitura de Dados**: Leitura da matriz de distâncias entre cidades a partir de um arquivo de texto.
- **Solução Inicial Aleatória**: Geração de uma solução inicial aleatória para iniciar o processo de otimização.
- **Resultados**: Escrita do melhor itinerário e da distância total em um arquivo de resultados para fácil consulta.

## Instalação

Para instalar as dependências do projeto, utilize o gerenciador de pacotes `pip`:

```bash
pip install -r requirements.txt
```

## Uso

Para executar o projeto, utilize o seguinte comando:

```bash
python -m src.presentation.main
```

### Pré-requisitos

- Certifique-se de que os arquivos de entrada (por exemplo, `data/five_d.txt`) estão disponíveis e no formato correto.
- A matriz de distâncias deve estar organizada de forma que cada linha represente as distâncias de uma cidade para as outras.

### Exemplo de Formato do Arquivo de Distâncias

O arquivo `five_d.txt` deve conter a matriz de distâncias no seguinte formato:

```
0.0  3.0  4.0  2.0  7.0
3.0  0.0  4.0  6.0  3.0
4.0  4.0  0.0  5.0  8.0
2.0  6.0  5.0  0.0  6.0
7.0  3.0  8.0  6.0  0.0
```

## Testes

Para executar os testes unitários, você pode usar o `pytest`. Primeiro, certifique-se de que o `pytest` está instalado:

```bash
pip install pytest
```

Em seguida, execute os testes:

```bash
pytest
```

Os testes podem ser encontrados na pasta `tests/`. Eles cobrem as principais funcionalidades do projeto para garantir que tudo funcione corretamente.

