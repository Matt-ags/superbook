# 🦸 Superbook: Uma Rede Social para Heróis

Um projeto de rede social full-stack, construído com Django, focado em um universo de super-heróis. Os usuários podem se cadastrar, fazer login (inclusive com o Google!) e interagir em um feed.

---

### ✨ Funcionalidades Principais

* **Autenticação Completa:** Sistema de cadastro e login de usuários.
* **Login Social:** Login rápido e seguro utilizando contas do Google (OAuth2).
* **Feed Interativo:** Usuários podem criar e visualizar postagens.
* **Perfis de Herói:** Cada usuário possui seu perfil.
* **Interface Responsiva:** Design adaptável a celulares e desktops (feito com Bootstrap).

---

### 🚀 Aplicação em Produção (Deploy)

A aplicação está no ar e funcionando! Você pode acessá-la e testar clicando no link abaixo:

> ### 🔗 [Acesse o Superbook aqui!](https://superbook.onrender.com/auth/login/).
---

### 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

* **Back-end:** Python (Django)
* **Front-end:** HTML5, CSS3, Bootstrap 5
* **Banco de Dados:** PostgreSQL (em produção), SQLite3 (em desenvolvimento)
* **Autenticação:** Django AllAuth, Google OAuth2
* **Deploy:** Render (para aplicação e banco de dados)

---

### 📸 Screenshots

| Tela de Login | Feed Principal |
| :---: | :---: |
| <img width="1365" height="644" alt="tela_login_superbook" src="https://github.com/user-attachments/assets/9f163852-b628-48b7-900a-b0dfcb8d0ae6" /> | <img width="1365" height="644" alt="perfil_superbook" src="https://github.com/user-attachments/assets/29e44137-4c59-4aa1-9ca4-3f32a099f0a0" /> |



---

### ⚙️ Como Rodar o Projeto Localmente

Se você quiser rodar este projeto na sua própria máquina, siga estes passos:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Matt-ags/superbook.git
    cd superbook
    ```

2.  **Crie e ative um ambiente virtual (venv):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crie um arquivo `.env`** na raiz do projeto e adicione suas chaves:
    *(Você precisará criar suas próprias chaves na Google Cloud Console para o OAuth2 funcionar)*
    ```ini
    SECRET_KEY=SUA_CHAVE_SECRETA_DO_DJANGO
    DEBUG=True
    
    # Chaves do Google OAuth2
    GOOGLE_CLIENT_ID=SUA_CLIENT_ID_DO_GOOGLE
    GOOGLE_CLIENT_SECRET=SUA_CLIENT_SECRET_DO_GOOGLE
    ```

5.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Rode o servidor:**
    ```bash
    python manage.py runserver
    ```

Acesse `http://127.0.0.1:8000/` no seu navegador.

---

### 👨‍💻 Autor

Feito com 💙 por **Mateus**
