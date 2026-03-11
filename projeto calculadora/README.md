# Calculadora com CustomTkinter

Este é um projeto simples de **calculadora com interface gráfica em Python**, desenvolvido utilizando a biblioteca **CustomTkinter** para criar uma interface moderna.

A aplicação permite realizar **operações matemáticas básicas** através de botões interativos em uma interface gráfica.

## Tecnologias utilizadas

* Python 3
* CustomTkinter

## Estrutura do Projeto

```
.
├── app.py
└── README.md
```

### app.py

Arquivo principal do programa.  
Responsável por:

* Criar a **interface gráfica da calculadora**
* Exibir a expressão matemática digitada pelo usuário
* Realizar cálculos matemáticos
* Limpar a operação quando necessário

A calculadora permite inserir:

* Números de **0 a 9**
* Operações matemáticas:

```
+
-
*
/
```

Também é possível utilizar **parênteses** para realizar cálculos mais complexos.

Quando o botão **"="** é pressionado, o sistema calcula a expressão digitada e exibe o resultado na tela.

Se a expressão for válida, o sistema exibirá:

```
Resultado do cálculo
```

Caso ocorra algum erro na expressão:

```
Erro!
```

---

## Como executar o projeto

### 1 Instalar a biblioteca necessária

```bash
pip install customtkinter
```

### 2 Executar o sistema

No terminal:

```bash
python app.py
```

---

## Funcionalidades

✔ Interface gráfica moderna  
✔ Botões numéricos  
✔ Operações matemáticas básicas  
✔ Suporte a parênteses  
✔ Botão para limpar a expressão  
✔ Tratamento de erro para cálculos inválidos  

---

## Melhorias futuras

Algumas melhorias que podem ser implementadas:

* Histórico de cálculos
* Mais operações matemáticas
* Melhor validação de expressões
* Interface mais completa
* 📦 **estrutura profissional de projeto**
