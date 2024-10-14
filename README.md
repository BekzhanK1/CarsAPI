# Car Management Application - README

## English Version

### Installation and Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/BekzhanK1/CarsAPI.git
   ```

2. **Create and Activate Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**:

   - By default, the application uses SQLite, which is already configured.

5. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - Visit `http://127.0.0.1:8000/` in your browser to see the application.

### Using the API

1. **List All Cars**:

   - **Endpoint**: `GET /api/cars/`
   - **Description**: Retrieve a list of all cars in the system.

2. **Get Car Details**:

   - **Endpoint**: `GET /api/cars/<id>/`
   - **Description**: Retrieve details of a specific car.

3. **Add a New Car**:

   - **Endpoint**: `POST /api/cars/`
   - **Description**: Create a new car entry (authenticated users only).

4. **Edit a Car**:

   - **Endpoint**: `PUT /api/cars/<id>/`
   - **Description**: Update information about an existing car (only the owner can update).

5. **Delete a Car**:

   - **Endpoint**: `DELETE /api/cars/<id>/`
   - **Description**: Delete a car (only the owner can delete).

6. **Add a Comment to a Car**:
   - **Endpoint**: `POST /api/cars/<id>/comments/`
   - **Description**: Add a comment to a specific car (authenticated users only).

## Русская версия

### Инструкция по установке и запуску

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/BekzhanK1/CarsAPI.git
   ```

2. **Создайте и активируйте виртуальное окружение**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # В Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте базу данных**:

   - По умолчанию используется SQLite, которая уже настроена.

5. **Примените миграции**:

   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер разработки**:
   ```bash
   python manage.py runserver
   ```
   - Откройте `http://127.0.0.1:8000/` в браузере, чтобы увидеть приложение.

### Использование API

1. **Список всех автомобилей**:

   - **Endpoint**: `GET /api/cars/`
   - **Описание**: Получить список всех автомобилей в системе.

2. **Получить информацию об автомобиле**:

   - **Endpoint**: `GET /api/cars/<id>/`
   - **Описание**: Получить информацию о конкретном автомобиле.

3. **Добавить новый автомобиль**:

   - **Endpoint**: `POST /api/cars/`
   - **Описание**: Создать новую запись об автомобиле (только для авторизованных пользователей).

4. **Редактировать автомобиль**:

   - **Endpoint**: `PUT /api/cars/<id>/`
   - **Описание**: Обновить информацию об автомобиле (только владелец может обновлять).

5. **Удалить автомобиль**:

   - **Endpoint**: `DELETE /api/cars/<id>/`
   - **Описание**: Удалить автомобиль (только владелец может удалить).

6. **Добавить комментарий к автомобилю**:
   - **Endpoint**: `POST /api/cars/<id>/comments/`
   - **Описание**: Добавить комментарий к конкретному автомобилю (только для авторизованных пользователей).
