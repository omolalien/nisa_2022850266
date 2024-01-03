-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 07:07 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_ticket_concert`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_ticket_order`
--

CREATE TABLE `customer_ticket_order` (
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Quantity` int(10) NOT NULL,
  `Ticket_Type` varchar(10) NOT NULL,
  `Merchandise` varchar(10) NOT NULL,
  `Total_Price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_ticket_order`
--

INSERT INTO `customer_ticket_order` (`Name`, `Email`, `Phone`, `Quantity`, `Ticket_Type`, `Merchandise`, `Total_Price`) VALUES
('anisa', 'noyen@gmail.com', '0132757069', 1, 'Tier A', 'Yes', 450),
('nazihah', 'icing.lola@gmail.com', '0193217627', 2, 'Tier B', 'No', 1000),
('san', 'choi@gmail.com', '0128576049', 3, 'Tier C', 'Yes', 1850);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
