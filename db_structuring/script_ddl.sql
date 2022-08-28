-- DDL(Linguagem de Definição de Dados) - Script para definição das estruturas de dados utilizadas no bd  

-- Desabilitando o modo estrito
SET GLOBAL sql_mode = '';

-- Criando o bd funcionarios
CREATE DATABASE funcionarios;

-- Selecionando o bd funcionarios
USE funcionarios;

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
  data_cancelamento DATE NOT NULL DEFAULT "0000-00-00",
  comportamento TEXT,
  PRIMARY KEY(id_empregado)
);