# 🖥️ Cadastro de Máquinas (SENAI)

**Curso:** Desenvolvimento de Sistemas — SENAI  
**Tecnologias:** Python, Django, SQLite

---

## 📌 Sobre o Projeto
Este projeto é uma aplicação web em **Django** desenvolvida como simulado no SENAI.  
O objetivo é informatizar o cadastro de **colaboradores** e o gerenciamento das **máquinas** sob responsabilidade deles.

---

## 🛠 Funcionalidades
- **Cadastro de Colaboradores**  
  - Nome completo  
  - E-mail (com validação)  
  - Setor  
  - Mensagem de sucesso após cadastro  

- **Cadastro de Máquinas**  
  - Nome da máquina  
  - Número de patrimônio  
  - Modelo  
  - Setor  
  - Colaborador responsável (selecionado a partir dos cadastrados)  
  - Mensagem de sucesso após cadastro  

- **Gerenciamento de Máquinas**  
  - Listagem de todas as máquinas com seu colaborador responsável  
  - Edição de registros  
  - Exclusão de registros  

---

## 🎨 Estilo (UI/UX)
- Fonte: **Segoe UI**  
- Tamanhos:  
  - Títulos → 24px  
  - Subtítulos → 20px  
  - Textos → 16px  
- Paleta de cores:  
  - Azul principal: `#0078D7`  
  - Cinza claro: `#F8F8F8`  
  - Amarelo destaque: `#FFB900`  
  - Texto: `#222222`  
  - Branco para formulários/cards  
  - Bordas/linhas: `#EDEDED`  
- Botões:  
  - Fundo azul `#0078D7`, texto branco  
  - Hover: `#005A9E`  
- Layout:  
  - Formulários centralizados, espaçamento entre elementos e leve sombra  

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar repositório
```bash
git clone https://github.com/leonardogranata/cadastro-maquinas-senai.git
cd cadastro-maquinas-senai
```
### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Criar banco e aplicar migrações
```bash
python manage.py migrate
```
### 5️⃣ Rodar servidor
```bash
python manage.py runserver
Acesse em http://127.0.0.1:8000/ no navegador.
```
---
📚 Projeto acadêmico desenvolvido como simulado avaliativo no SENAI.
