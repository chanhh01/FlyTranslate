-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: flytranslate
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `languages` (
  `lang_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `lang_name` varchar(255) NOT NULL,
  `lang_code` varchar(255) NOT NULL,
  `lang_code_for_ocr` varchar(10) DEFAULT NULL,
  `display_lang_font_dir` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`lang_id`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `languages`
--

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
INSERT INTO `languages` VALUES (1,'Abkhazian','ab',NULL,NULL),(2,'Avestan','ae',NULL,NULL),(3,'Afrikaans','af','af',NULL),(4,'Akan','ak',NULL,NULL),(5,'Amharic','am',NULL,NULL),(6,'Aragonese','an',NULL,NULL),(7,'Arabic','ar','ar','segeoui.ttf'),(8,'Assamese','as','as',NULL),(9,'Avaric','av','ava',NULL),(10,'Aymara','ay',NULL,NULL),(11,'Azerbaijani','az','az',NULL),(12,'Bashkir','ba',NULL,NULL),(13,'Belarusian','be','be','segeoui.ttf'),(14,'Bulgarian','bg','bg','segeoui.ttf'),(15,'Bihari languages','bh','bh',NULL),(16,'Bislama','bi',NULL,NULL),(17,'Bambara','bm',NULL,NULL),(18,'Bengali','bn','bn','Nirmala.ttf'),(19,'Tibetan','bo',NULL,NULL),(20,'Breton','br',NULL,NULL),(21,'Bosnian','bs','bs',NULL),(22,'Catalan; Valencian','ca',NULL,NULL),(23,'Chechen','ce','che','segeoui.ttf'),(24,'Chamorro','ch',NULL,NULL),(25,'Corsican','co',NULL,NULL),(26,'Cree','cr',NULL,NULL),(27,'Czech','cs','cs',NULL),(28,'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic','cu',NULL,NULL),(29,'Chuvash','cv',NULL,NULL),(30,'Welsh','cy','cy',NULL),(31,'Danish','da','da',NULL),(32,'German','de','de',NULL),(33,'Divehi; Dhivehi; Maldivian','dv',NULL,NULL),(34,'Dzongkha','dz',NULL,NULL),(35,'Ewe','ee',NULL,NULL),(36,'Greek, Modern (1453-)','el',NULL,NULL),(37,'English','en','en',NULL),(38,'Esperanto','eo',NULL,NULL),(39,'Spanish; Castilian','es','es',NULL),(40,'Estonian','et','et','segoeui.ttf'),(41,'Basque','eu',NULL,NULL),(42,'Persian','fa','fa','segoeui.ttf'),(43,'Fulah','ff',NULL,NULL),(44,'Finnish','fi',NULL,NULL),(45,'Fijian','fj',NULL,NULL),(46,'Faroese','fo',NULL,NULL),(47,'French','fr','fr',NULL),(48,'Western Frisian','fy',NULL,NULL),(49,'Irish','ga','ga',NULL),(50,'Gaelic; Scottish Gaelic','gd',NULL,NULL),(51,'Galician','gl',NULL,NULL),(52,'Guarani','gn',NULL,NULL),(53,'Gujarati','gu',NULL,NULL),(54,'Manx','gv',NULL,NULL),(55,'Hausa','ha',NULL,NULL),(56,'Hebrew','he',NULL,NULL),(57,'Hindi','hi','hi','Nirmala.ttf'),(58,'Hiri Motu','ho',NULL,NULL),(59,'Croatian','hr','hr',NULL),(60,'Haitian; Haitian Creole','ht',NULL,NULL),(61,'Hungarian','hu','hu',NULL),(62,'Armenian','hy',NULL,NULL),(63,'Herero','hz',NULL,NULL),(64,'Interlingua (International Auxiliary Language Association)','ia',NULL,NULL),(65,'Indonesian','id','id',NULL),(66,'Interlingue; Occidental','ie',NULL,NULL),(67,'Igbo','ig',NULL,NULL),(68,'Sichuan Yi; Nuosu','ii',NULL,NULL),(69,'Inupiaq','ik',NULL,NULL),(70,'Ido','io',NULL,NULL),(71,'Icelandic','is','is',NULL),(72,'Italian','it','it',NULL),(73,'Inuktitut','iu',NULL,NULL),(74,'Japanese','ja','ja','msgothic.ttc'),(75,'Javanese','jv',NULL,NULL),(76,'Georgian','ka',NULL,NULL),(77,'Kongo','kg',NULL,NULL),(78,'Kikuyu; Gikuyu','ki',NULL,NULL),(79,'Kuanyama; Kwanyama','kj',NULL,NULL),(80,'Kazakh','kk',NULL,NULL),(81,'Kalaallisut; Greenlandic','kl',NULL,NULL),(82,'Central Khmer','km',NULL,NULL),(83,'Kannada','kn','kn','Nirmala.ttf'),(84,'Korean','ko','ko','gulim.ttc'),(85,'Kanuri','kr',NULL,NULL),(86,'Kashmiri','ks',NULL,NULL),(87,'Kurdish','ku','ku','segoeui.ttf'),(88,'Komi','kv',NULL,NULL),(89,'Cornish','kw',NULL,NULL),(90,'Kirghiz; Kyrgyz','ky',NULL,NULL),(91,'Latin','la','la',NULL),(92,'Luxembourgish; Letzeburgesch','lb',NULL,NULL),(93,'Ganda','lg',NULL,NULL),(94,'Limburgan; Limburger; Limburgish','li',NULL,NULL),(95,'Lingala','ln',NULL,NULL),(96,'Lao','lo',NULL,NULL),(97,'Lithuanian','lt','lt',NULL),(98,'Luba-Katanga','lu',NULL,NULL),(99,'Latvian','lv','lv',NULL),(100,'Malagasy','mg',NULL,NULL),(101,'Marshallese','mh',NULL,NULL),(102,'Maori','mi','mi',NULL),(103,'Macedonian','mk',NULL,NULL),(104,'Malayalam','ml',NULL,NULL),(105,'Mongolian','mn','mn',NULL),(106,'Marathi','mr','mr',NULL),(107,'Malay','ms','ms',NULL),(108,'Maltese','mt','mt',NULL),(109,'Burmese','my',NULL,'ntailu.ttf'),(110,'Nauru','na',NULL,NULL),(111,'Bokmål, Norwegian; Norwegian Bokmål','nb',NULL,NULL),(112,'Ndebele, North; North Ndebele','nd',NULL,NULL),(113,'Nepali','ne','ne','Nirmala.ttf'),(114,'Ndonga','ng',NULL,NULL),(115,'Dutch; Flemish','nl','nl',NULL),(116,'Norwegian Nynorsk; Nynorsk, Norwegian','nn',NULL,NULL),(117,'Norwegian','no','no',NULL),(118,'Ndebele, South; South Ndebele','nr',NULL,NULL),(119,'Navajo; Navaho','nv',NULL,NULL),(120,'Chichewa; Chewa; Nyanja','ny',NULL,NULL),(121,'Occitan','oc','oc',NULL),(122,'Ojibwa','oj',NULL,NULL),(123,'Oromo','om',NULL,NULL),(124,'Oriya','or',NULL,NULL),(125,'Ossetian; Ossetic','os',NULL,NULL),(126,'Panjabi; Punjabi','pa',NULL,NULL),(127,'Pali','pi','pi',NULL),(128,'Polish','pl','pl',NULL),(129,'Pushto; Pashto','ps',NULL,NULL),(130,'Portuguese','pt','pt',NULL),(131,'Quechua','qu',NULL,NULL),(132,'Romansh','rm',NULL,NULL),(133,'Rundi','rn',NULL,NULL),(134,'Romanian; Moldavian; Moldovan','ro','ro',NULL),(135,'Russian','ru','ru','segoeui.ttf'),(136,'Kinyarwanda','rw',NULL,NULL),(137,'Sanskrit','sa',NULL,NULL),(138,'Sardinian','sc',NULL,NULL),(139,'Sindhi','sd',NULL,NULL),(140,'Northern Sami','se',NULL,NULL),(141,'Sango','sg',NULL,NULL),(142,'Sinhala; Sinhalese','si',NULL,NULL),(143,'Slovak','sk','sk','segoeui.ttf'),(144,'Slovenian','sl','sl','segoeui.ttf'),(145,'Samoan','sm',NULL,NULL),(146,'Shona','sn',NULL,NULL),(147,'Somali','so',NULL,NULL),(148,'Albanian','sq','sq',NULL),(149,'Serbian','sr','rs_latin','segoeui.ttf'),(150,'Swati','ss',NULL,NULL),(151,'Sotho, Southern','st',NULL,NULL),(152,'Sundanese','su',NULL,NULL),(153,'Swedish','sv','sv',NULL),(154,'Swahili','sw','sw',NULL),(155,'Tamil','ta','ta','Nirmala.ttf'),(156,'Telugu','te','te','Nirmala.ttf'),(157,'Tajik','tg','tjk','segoeui.ttf'),(158,'Thai','th','th','ntailu.ttf'),(159,'Tigrinya','ti',NULL,NULL),(160,'Turkmen','tk',NULL,NULL),(161,'Tagalog','tl','tl',NULL),(162,'Tswana','tn',NULL,NULL),(163,'Tonga','to',NULL,NULL),(164,'Turkish','tr','tr','segoeui.ttf'),(165,'Tsonga','ts',NULL,NULL),(166,'Tatar','tt',NULL,NULL),(167,'Twi','tw',NULL,NULL),(168,'Tahitian','ty',NULL,NULL),(169,'Uyghur','ug','ug','segoeui.ttf'),(170,'Ukrainian','uk','uk','segoeui.ttf'),(171,'Urdu','ur','ur','segoeui.ttf'),(172,'Uzbek','uz','uz','segoeui.ttf'),(173,'Venda','ve',NULL,NULL),(174,'Vietnamese','vi','vi',NULL),(175,'Volapük','vo',NULL,NULL),(176,'Walloon','wa',NULL,NULL),(177,'Wolof','wo',NULL,NULL),(178,'Xhosa','xh',NULL,NULL),(179,'Yiddish','yi',NULL,NULL),(180,'Yoruba','yo',NULL,NULL),(181,'Zhuang; Chuang','za',NULL,NULL),(182,'Chinese','zh-CN','ch_sim','simsun.ttc'),(183,'Zulu','zu',NULL,NULL),(184,'Traditional Chinese','zh-TW','ch_tra','mingliu.ttc');
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-05 16:38:35
