## Configurando um Ambiente Virtual

Um ambiente virtual é uma forma de isolar as dependências do seu projeto do sistema global, permitindo que você mantenha um ambiente Python limpo e independente para cada projeto. Siga os passos abaixo para criar um ambiente virtual:

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório raiz do seu projeto.

3. Execute o seguinte comando para criar um novo ambiente virtual:

   ```bash
   python -m venv venv
   ```

   Isso criará um novo ambiente virtual na pasta "venv" do seu projeto.

4. Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS e Linux:

     ```bash
     source venv/bin/activate
     ```

   Você verá o prefixo `(venv)` no seu terminal, indicando que o ambiente virtual está ativado.

## Instalando Bibliotecas a partir de um Arquivo requirements.txt

Para instalar as bibliotecas listadas em um arquivo `requirements.txt`, siga as etapas abaixo:

1. Certifique-se de que seu ambiente virtual esteja ativado.

2. No terminal, execute o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

   Isso instalará todas as bibliotecas listadas no arquivo `requirements.txt` no seu ambiente virtual.

## Executando Testes Unitários com o Pytest e Relatório

O pytest é uma estrutura de teste amplamente utilizada para testes unitários em Python. Ele possui recursos poderosos, incluindo a capacidade de gerar relatórios de teste. Siga as etapas abaixo para executar testes unitários com o pytest e gerar um relatório:

1. Certifique-se de que você tenha o pytest instalado no seu ambiente virtual (você pode instalá-lo usando o comando `pip install pytest`).

2. No terminal, navegue até o diretório raiz do seu projeto (onde seus testes estão localizados).

3. Execute o seguinte comando para executar todos os testes:
   ```bash 
   export PYTHONPATH="${PYTHONPATH}:/src"
    ```
4.
   ```bash
   make test
   ```
      Isso executará todos os testes unitários no diretório atual.


## Generators
Os geradores (generators) em Python são estruturas de dados que produzem sequências de valores sob demanda.
Eles são uma alternativa eficiente e econômica em termos de memória em comparação com as listas,
especialmente quando lidamos com grandes conjuntos de dados ou sequências infinitas.

1- Economia de memoria, evita criacao e a alocacao de memoria para uma lista completa, so produzem valores quando sao explicitamente solicitados.
Tem suporte a operacoes em tempo real.

## Numpy 

3 Numpy para calculo -  A lib e escrito em C e otimizada para operacoes numericas, ele utilizar objeto de matriz multidimensional
chamado de ndarray que armazenar grande quantidade de dados em memoria de forma eficiente, e tem uma sobrecarga de memoria menor que as lista