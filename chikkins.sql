
DROP DATABASE IF EXISTS chikkins;

CREATE DATABASE chikkins 
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

CREATE TABLE public.cliente (
  cedula INTEGER NOT NULL,
  nombre VARCHAR(12),
  whatsapp VARCHAR(20) CHECK (whatsapp LIKE '+%'),
  email VARCHAR(20),
  CONSTRAINT cedula_pkey PRIMARY KEY (cedula)
);

CREATE TABLE public.pedido (
    id INTEGER NOT NULL,
    cedula_cliente INTEGER NOT NULL,
    cant_hamburguesas INTEGER CHECK (cant_hamburguesas >= 0),
    m_delivery NUMERIC(10,2) CHECK (m_delivery >= 0),
    m_total NUMERIC CHECK (m_total >= 0),
    CONSTRAINT pedido_pkey PRIMARY KEY (id),
    CONSTRAINT pedido_cedula_cliente_fkey FOREIGN KEY (cedula_cliente) REFERENCES cliente(cedula)
);