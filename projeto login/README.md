Aqui está um **README.md** que você pode usar no seu GitHub para esse projeto:

---

# Sistema de Login com CustomTkinter

Este é um projeto simples de **sistema de login e cadastro com interface gráfica em Python**, desenvolvido utilizando a biblioteca **CustomTkinter** para criar uma interface moderna.

O sistema possui duas telas principais:

* **Tela de Login**
* **Tela de Cadastro**

## Tecnologias utilizadas

* Python 3
* CustomTkinter

## Estrutura do Projeto

```
.
├── login.py
├── cadastro.py
└── README.md
```

### login.py

Arquivo principal do programa.
Responsável por:

* Criar a **tela de login**
* Validar usuário e senha
* Abrir a tela de cadastro

Usuário e senha padrão para teste:

```
Usuário: Rodrigo
Senha: 1234
```

Se os dados estiverem corretos, o sistema exibirá:

```
Login feito com sucesso!
```

Caso contrário:

```
Falha no login!
```

---

### cadastro.py

Responsável pela **tela de cadastro**.

Funções principais:

* Abrir uma nova janela de cadastro
* Permitir inserir:

  * Usuário
  * Email
  * Senha
* Validar se todos os campos foram preenchidos
* Retornar para a tela de login após cadastro concluído

Se os campos forem preenchidos corretamente:

```
Cadastro Concluído
```

Caso contrário:

```
Falha no cadastro
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
python login.py
```

---

## Funcionalidades

✔ Interface gráfica moderna
✔ Tela de login
✔ Tela de cadastro
✔ Validação de campos
✔ Navegação entre telas

---

## Melhorias futuras

Algumas melhorias que podem ser implementadas:

* Salvar usuários em **banco de dados**
* Criptografia de senha
* Validação de email
* Sistema de autenticação real
* Interface mais completa
* 📦 **estrutura profissional de projeto**

Seu README pode ficar **bem mais bonito para recrutadores no GitHub**.
