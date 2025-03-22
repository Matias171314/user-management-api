-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS user_management;
USE user_management;

-- Crear la tabla de roles (para manejo de permisos)
CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE CHECK (email LIKE '%_@_%._%'), -- Asegura formato de email
    password_hash VARCHAR(255) NOT NULL, -- Para almacenar contraseñas encriptadas
    role_id INT NOT NULL,
    status ENUM('active', 'inactive') DEFAULT 'active', -- Control de estado
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);

-- Insertar roles básicos
INSERT INTO roles (role_name) VALUES ('admin'), ('user');
