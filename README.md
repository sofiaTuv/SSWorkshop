## Workshop
----
##Установка и запуск проекта
----
### 1. Склонировать репозиторий

```bash
git clone https://github.com/GHMan2021/globalsqa.git
```
----
### 2. Перейти в директорию проекта
### 3. Создать вируальное окружение

```bash
python -m venv venv
```
----
### 4. Активировать окружение
```bash
venv\Scripts\activate
```
----
### 5. Установка зависимостей
```bash
pip install -r requirements.txt
```
----
### 6. Запуск тестов
```bash
pytest --alluredir=allure-results
```
----
### 7. Запуск отчета allure по тестам
```bash
allure serve allure-results
```
