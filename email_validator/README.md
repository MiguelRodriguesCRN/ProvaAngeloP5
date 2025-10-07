# 📧 Email Validator

## 🎯 Objetivo
Desenvolver e implementar uma **suíte de testes unitários automatizados** que valide as regras de negócio de uma pequena aplicação, garantindo **alta cobertura das funcionalidades críticas**.

---

## 🧠 Descrição do Projeto
Este projeto consiste em um **validador de e-mail** desenvolvido em **Python**, utilizando **Pytest** para a criação e execução dos testes unitários.  
O objetivo é verificar se um e-mail informado segue regras de formatação válidas e garantir que todas as validações críticas estejam devidamente testadas.

---

## 🧩 Ferramentas Utilizadas
- **Linguagem:** Python 3.x  
- **Framework de Testes:** Pytest  
- **Cobertura de Testes:** pytest-cov  
- **Controle de Versão:** Git e GitHub  

---

## 🧾 Regras de Negócio Testadas

1. O e-mail **deve conter o caractere `@`**.  
2. O e-mail **deve conter pelo menos um `.` após o `@`**.  
3. O e-mail **não pode começar nem terminar com caracteres especiais** (`@`, `.`, `-`, `_`).  
4. O e-mail **não pode conter espaços em branco**.  
5. O domínio (parte após o `@`) **deve ter pelo menos um caractere antes e depois do ponto final**.  
6. O e-mail **deve ter comprimento entre 5 e 254 caracteres**.  

Todas essas regras foram cobertas por testes automatizados, garantindo que o comportamento do validador esteja de acordo com os requisitos definidos.

---

## 🧪 Exemplo de Saída dos Testes
============================= test session starts ============================= collected 9 items

tests/test_validator.py ......... [100%]

---------- coverage: platform win32, python 3.13 ---------- Name Stmts Miss Cover email_validator/validator.py 16 0 100% TOTAL 16 0 100%


Run
Copy code

✅ **Cobertura total de 100% obtida** sobre as regras de negócio críticas.

---

## 🖼️ Relatório de Cobertura

<img width="1086" height="400" alt="image" src="https://github.com/user-attachments/assets/f78ca0eb-1b9e-4df0-b810-5ee6b4f7810a" />

---

## 👨‍💻 Aluno
**Miguel Rodrigues Carneiro**  
Email: miguelrodriguescrn@gmail.com
