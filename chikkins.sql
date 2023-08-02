
DROP DATABASE IF EXISTS chikkins;

CREATE DATABASE chikkins 
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

CREATE TABLE public.cliente (
  cedula INTEGER NOT NULL,
  nombre VARCHAR(12),
  whatsapp VARCHAR(20),
  email VARCHAR(50),
  CONSTRAINT cedula_pkey PRIMARY KEY (cedula)
);

CREATE TABLE public.pedido (
    id serial NOT NULL,
    cedula_cliente INTEGER NOT NULL,
    cant_hamburguesas INTEGER CHECK (cant_hamburguesas >= 0),
    m_delivery NUMERIC(10,2) CHECK (m_delivery >= 0),
    m_total NUMERIC CHECK (m_total >= 0),
    estado VARCHAR(12),
    fecha VARCHAR,
    metodo_pago VARCHAR(10),
    municipio VARCHAR(40),
    ciudad VARCHAR(40),
    remarks VARCHAR(80),
    CONSTRAINT pedido_id_pkey PRIMARY KEY (id),
    CONSTRAINT pedido_cedula_cliente_fkey FOREIGN KEY (cedula_cliente) REFERENCES cliente(cedula)
);