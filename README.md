# User Management API (Flask + MySQL)
API CRUD de Gestión de Usuarios con Flask y MySQL. Implementa autenticación JWT y manejo seguro de datos.

---

## 📂 Estructura de Carpetas:

```
user_management_api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   └── database.py
│
├── migrations/
│
├── tests/
│   ├── test_auth.py
│   ├── test_routes.py
│   └── test_models.py
│
├── venv
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

---

## 📌 Descripción:
Una API CRUD para gestionar usuarios, con autenticación JWT y base de datos MySQL.

---

## 🛠️ Tecnologías Utilizadas:
- Python (Flask)
- MySQL
- Flask-JWT-Extended
- SQLAlchemy
- Docker (opcional para despliegue)

---

## ✅ Instalación:

1. Clonar el repositorio:
```bash
git clone https://github.com/MatiasVasquez/user-management-api.git
cd user_management_api
```

2. Crear entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate   # En Linux o MacOS
venv\Scripts\activate     # En Windows
pip install -r requirements.txt
```

3. Configurar base de datos MySQL en el archivo `.env`:
```
DATABASE_URL=mysql+pymysql://usuario:password@localhost/db_name
JWT_SECRET_KEY=supersecretkey
```

4. Ejecutar migraciones:
```bash
flask db upgrade
```

5. Ejecutar la API:
```bash
python run.py
```

---

## 🚀 Endpoints CRUD:

| Método | Endpoint         | Descripción          |
|--------|-----------------|--------------------|
| POST   | /register       | Registro de usuario |
| POST   | /login          | Autenticación JWT |
| GET    | /users          | Listar usuarios |
| PUT    | /user/<id>      | Actualizar usuario |
| DELETE | /user/<id>      | Eliminar usuario |

---

## ✅ Pruebas:
```bash
pytest tests/
```

---

## 📂 GitHub Repo:
[User Management API](https://github.com/MatiasVasquez/user-management-api)
