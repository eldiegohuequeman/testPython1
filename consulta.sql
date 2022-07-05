-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para consulta
CREATE DATABASE IF NOT EXISTS `consulta` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `consulta`;

-- Volcando estructura para tabla consulta.consulta
CREATE TABLE IF NOT EXISTS `consulta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `canPacientes` int(11) DEFAULT NULL,
  `nomEspecialista` varchar(50) DEFAULT NULL,
  `tipoFConsulta` varchar(50) DEFAULT NULL,
  `Estado` varchar(50) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Hospital` (`hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.consulta: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `consulta` DISABLE KEYS */;
INSERT INTO `consulta` (`id`, `canPacientes`, `nomEspecialista`, `tipoFConsulta`, `Estado`, `hospital_id`) VALUES
	(1, 1, 'Carlos Silva', 'Pediatria', 'espera', 1),
	(2, 0, 'Felipe Avello', 'Urgencia', 'espera', 1),
	(3, 0, 'Claudia Reyes', 'Consulta General Integral', 'espera', 1);
/*!40000 ALTER TABLE `consulta` ENABLE KEYS */;

-- Volcando estructura para tabla consulta.hospital
CREATE TABLE IF NOT EXISTS `hospital` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombreHospital` varchar(50) DEFAULT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `consulta_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_hospital_paciente` (`paciente_id`),
  KEY `FK_consulta` (`consulta_id`),
  CONSTRAINT `FK_consulta` FOREIGN KEY (`consulta_id`) REFERENCES `consulta` (`id`),
  CONSTRAINT `FK_hospital_paciente` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.hospital: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `hospital` DISABLE KEYS */;
INSERT INTO `hospital` (`id`, `nombreHospital`, `paciente_id`, `consulta_id`) VALUES
	(1, 'Hospital 1', NULL, NULL);
/*!40000 ALTER TABLE `hospital` ENABLE KEYS */;

-- Volcando estructura para tabla consulta.ninop
CREATE TABLE IF NOT EXISTS `ninop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) DEFAULT NULL,
  `relacionPesoEstatura` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_ninop` (`paciente_id`),
  CONSTRAINT `FK_ninop` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.ninop: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `ninop` DISABLE KEYS */;
INSERT INTO `ninop` (`id`, `paciente_id`, `relacionPesoEstatura`) VALUES
	(8, 17, 14),
	(9, 18, 13),
	(10, 19, 13);
/*!40000 ALTER TABLE `ninop` ENABLE KEYS */;

-- Volcando estructura para tabla consulta.paciente
CREATE TABLE IF NOT EXISTS `paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `noHistorialMedico` int(11) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  `prioridad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Paciente` (`hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.paciente: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` (`id`, `nombre`, `edad`, `noHistorialMedico`, `hospital_id`, `prioridad`) VALUES
	(13, 'Eduardo Paillape', 19, 0, 0, 5),
	(14, 'pedro Reyes', 19, 1, 0, 2),
	(15, 'Pedro Jofre', 45, 0, 0, 4),
	(16, 'Matilde Gallardo', 70, 0, 0, 8),
	(17, 'Barbara Leal', 4, 8, 0, 3),
	(18, 'Diego Rivera', 2, 1, 0, 13),
	(19, 'Gustavo Flores', 12, 0, 0, 13),
	(20, 'Raul Llancaman', 19, 0, 0, 5);
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;

-- Volcando estructura para tabla consulta.panciano
CREATE TABLE IF NOT EXISTS `panciano` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) DEFAULT NULL,
  `tieneDieta` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_panciano` (`paciente_id`),
  CONSTRAINT `FK_panciano` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.panciano: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `panciano` DISABLE KEYS */;
INSERT INTO `panciano` (`id`, `paciente_id`, `tieneDieta`) VALUES
	(1, 15, 1),
	(2, 16, 1);
/*!40000 ALTER TABLE `panciano` ENABLE KEYS */;

-- Volcando estructura para tabla consulta.pjoven
CREATE TABLE IF NOT EXISTS `pjoven` (
  `fumador` tinyint(4) DEFAULT NULL,
  `paciente_id` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `FK_pjoven` (`paciente_id`),
  CONSTRAINT `FK_pjoven` FOREIGN KEY (`paciente_id`) REFERENCES `paciente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.pjoven: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `pjoven` DISABLE KEYS */;
INSERT INTO `pjoven` (`fumador`, `paciente_id`, `id`) VALUES
	(1, 13, 4),
	(0, 13, 5),
	(0, 14, 6),
	(1, 20, 7),
	(1, 20, 8);
/*!40000 ALTER TABLE `pjoven` ENABLE KEYS */;

-- Volcando estructura para tabla consulta.salaespera
CREATE TABLE IF NOT EXISTS `salaespera` (
  `id_sala` int(11) NOT NULL AUTO_INCREMENT,
  `id_hospital` int(11) DEFAULT NULL,
  `id_consulta` int(11) DEFAULT NULL,
  `id_paciente` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_sala`),
  KEY `FK_id_consulta` (`id_consulta`),
  CONSTRAINT `FK_id_consulta` FOREIGN KEY (`id_consulta`) REFERENCES `consulta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla consulta.salaespera: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `salaespera` DISABLE KEYS */;
INSERT INTO `salaespera` (`id_sala`, `id_hospital`, `id_consulta`, `id_paciente`) VALUES
	(52, NULL, 1, 17);
/*!40000 ALTER TABLE `salaespera` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
