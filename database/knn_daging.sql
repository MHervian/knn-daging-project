-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2020 at 04:46 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `knn_daging`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_mentah`
--

CREATE TABLE `data_mentah` (
  `no_data` int(11) NOT NULL,
  `red_mean` float NOT NULL,
  `green_mean` float NOT NULL,
  `blue_mean` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_mentah`
--

INSERT INTO `data_mentah` (`no_data`, `red_mean`, `green_mean`, `blue_mean`) VALUES
(1, 212.42, 208.31, 198.08),
(2, 163.15, 162.22, 155.79),
(3, 196.14, 193.57, 183.63),
(4, 197.06, 193.84, 183.08),
(5, 159.66, 161.16, 154.46),
(6, 206.51, 198.8, 190.27),
(7, 163.85, 160.19, 150.76),
(8, 155.07, 151.52, 144.89),
(9, 221.59, 214.44, 209.77),
(10, 195.98, 189.72, 179.62),
(11, 199.86, 193.05, 183.29),
(12, 231.66, 224.15, 219.38),
(13, 226.07, 219.5, 215.15),
(14, 197.58, 193.51, 181.96),
(15, 167.03, 164.66, 157.28),
(16, 200.15, 199.21, 188.37),
(17, 192.23, 189.98, 178.74),
(18, 149.54, 149.73, 142.5),
(19, 186.1, 180.94, 170.85),
(20, 202.23, 195.44, 185.85),
(21, 158.81, 156.61, 151.37),
(22, 195.39, 189.52, 178.63),
(23, 202.61, 196.69, 185.42),
(24, 158.98, 157.37, 150.76),
(25, 225.24, 220.58, 217.47),
(26, 196.26, 192.71, 181.91),
(27, 159.37, 159.41, 154.8),
(28, 196.31, 192.16, 182.25),
(29, 200.17, 195.93, 186.12),
(30, 161.06, 159.21, 153.35),
(31, 204.58, 199.98, 187.9),
(32, 155.94, 154.03, 145.81),
(33, 204.34, 202.17, 190.51),
(34, 207.82, 203.77, 192.14),
(35, 162.25, 161.25, 152.79),
(36, 211.56, 206.67, 195.76),
(37, 200.23, 195.9, 184.47),
(38, 158.06, 156.76, 148.48),
(39, 203.93, 199.1, 187.05),
(40, 159.11, 158.24, 150.32),
(41, 216.04, 208.73, 201.66),
(42, 208.42, 201.78, 191.79),
(43, 145.76, 143.18, 132.53),
(44, 159.85, 155.41, 145.31),
(45, 147.81, 143.91, 132.73),
(46, 199.62, 195.31, 184.09),
(47, 218.93, 212.96, 201.18),
(48, 162.53, 158.95, 149.96),
(49, 210.44, 206.39, 197.19),
(50, 200.59, 196.55, 186.31),
(51, 158.4, 157.56, 150.89),
(52, 187.38, 182.81, 172.04),
(53, 201.94, 196.88, 186.14),
(54, 153.33, 151.94, 145.85),
(55, 173.39, 171.98, 160.75),
(56, 160.08, 153.87, 146.96),
(57, 188.07, 178.2, 168.14),
(58, 228.18, 220.55, 215.26),
(59, 176.85, 173.18, 162.38),
(60, 153.93, 150.93, 141.22),
(67, 216.04, 208.73, 201.66);

-- --------------------------------------------------------

--
-- Table structure for table `hasil_knn`
--

CREATE TABLE `hasil_knn` (
  `no_hasil` int(11) NOT NULL,
  `no_data` int(11) NOT NULL,
  `no_kategori` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hasil_knn`
--

INSERT INTO `hasil_knn` (`no_hasil`, `no_data`, `no_kategori`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1),
(7, 7, 1),
(8, 8, 1),
(9, 9, 1),
(10, 10, 1),
(11, 11, 1),
(12, 12, 1),
(13, 13, 1),
(14, 14, 1),
(15, 15, 1),
(16, 16, 1),
(17, 17, 1),
(18, 18, 1),
(19, 19, 1),
(20, 20, 1),
(21, 21, 1),
(22, 22, 1),
(23, 23, 1),
(24, 24, 1),
(25, 25, 1),
(26, 26, 1),
(27, 27, 1),
(28, 28, 1),
(29, 29, 1),
(30, 30, 1),
(31, 31, 2),
(32, 32, 2),
(33, 33, 2),
(34, 34, 2),
(35, 35, 2),
(36, 36, 2),
(37, 37, 2),
(38, 38, 2),
(39, 39, 2),
(40, 40, 2),
(41, 41, 2),
(42, 42, 2),
(43, 43, 2),
(44, 44, 2),
(45, 45, 2),
(46, 46, 2),
(47, 47, 2),
(48, 48, 2),
(49, 49, 2),
(50, 50, 2),
(51, 51, 2),
(52, 52, 2),
(53, 53, 2),
(54, 54, 2),
(55, 55, 2),
(56, 56, 2),
(57, 57, 2),
(58, 58, 2),
(59, 59, 2),
(60, 60, 2),
(62, 67, 2);

-- --------------------------------------------------------

--
-- Table structure for table `kategori`
--

CREATE TABLE `kategori` (
  `no_kategori` int(11) NOT NULL,
  `nama_cat` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kategori`
--

INSERT INTO `kategori` (`no_kategori`, `nama_cat`) VALUES
(1, 'Daging Sapi'),
(2, 'Daging Babi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_mentah`
--
ALTER TABLE `data_mentah`
  ADD PRIMARY KEY (`no_data`);

--
-- Indexes for table `hasil_knn`
--
ALTER TABLE `hasil_knn`
  ADD PRIMARY KEY (`no_hasil`),
  ADD KEY `fk_no_kategori` (`no_kategori`),
  ADD KEY `fk_no_data` (`no_data`);

--
-- Indexes for table `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`no_kategori`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_mentah`
--
ALTER TABLE `data_mentah`
  MODIFY `no_data` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT for table `hasil_knn`
--
ALTER TABLE `hasil_knn`
  MODIFY `no_hasil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `kategori`
--
ALTER TABLE `kategori`
  MODIFY `no_kategori` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hasil_knn`
--
ALTER TABLE `hasil_knn`
  ADD CONSTRAINT `fk_no_data` FOREIGN KEY (`no_data`) REFERENCES `data_mentah` (`no_data`),
  ADD CONSTRAINT `fk_no_kategori` FOREIGN KEY (`no_kategori`) REFERENCES `kategori` (`no_kategori`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
