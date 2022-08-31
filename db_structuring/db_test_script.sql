-- DDL(Linguagem de Definição de Dados)
-- Script para definição das estruturas de dados utilizadas no banco de dados de teste local

-- Desabilitando o modo estrito
SET GLOBAL sql_mode = '';

-- Criando o dbfuncionarios
CREATE DATABASE dbfuncionarios;

-- Selecionando o dbfuncionarios
USE dbfuncionarios;

-- Criando a tabela dados_pessoais
CREATE TABLE dados_pessoais(
  id_pessoa INT NOT NULL AUTO_INCREMENT,
  codigo INT NOT NULL UNIQUE,
  nome VARCHAR(255) NOT NULL,
  data_nascimento DATE NOT NULL,
  cpf VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  PRIMARY KEY(id_pessoa)
);

-- Criando a tabela dados_empregados
CREATE TABLE dados_empregados(
  id_empregado INT NOT NULL AUTO_INCREMENT,
  codigo INT NOT NULL UNIQUE,
  cargo VARCHAR(255) NOT NULL,
  data_inicio DATE NOT NULL,
  data_cancelamento DATE DEFAULT NULL,
  comportamento TEXT,
  PRIMARY KEY(id_empregado)
);