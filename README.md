# Ethiopian Medical Business Data Warehouse
========================================

## Table of Contents
1. [Overview](#overview)
2. [Introduction](#introduction)
3. [Data Scraping and Collection Pipeline](#data-scraping-and-collection-pipeline)
4. [Data Cleaning and Transformation](#data-cleaning-and-transformation)
5. [Object Detection using YOLO](#object-detection-using-yolo)
6. [API Development with FastAPI](#api-development-with-fastapi)
7. [Installation and Usage](#installation-and-usage)

---

## Overview
The **Ethiopian Medical Business Data Warehouse** project focuses on creating a data warehouse that stores data collected from Ethiopian medical businesses by scraping specific Telegram channels. The project incorporates data collection, cleaning, object detection using YOLO, and an API built using FastAPI to expose the collected data for various applications.

---

## Introduction
The medical business landscape in Ethiopia is growing, with many professionals and businesses sharing their services and products via **Telegram channels**. This project seeks to efficiently scrape, clean, and organize the data from these channels, particularly for the healthcare industry. By integrating **YOLO** for object detection in relevant images or videos, and making the data accessible through **FastAPI**, this project aims to provide a powerful resource for analysis and business insights.

---

## Data Scraping and Collection Pipeline
The data is collected from a range of medical-related Telegram channels such as **DoctorsET**, **Chemed Telegram Channel**, and **Yetenaweg**. This pipeline automates the extraction of messages, images, and video content shared in these channels.

### Key Steps:
1. **Automated Data Collection**: Scraping of data using Python scripts.
2. **Data Storage**: Saving the collected data in structured formats (e.g., CSV) for analysis.

---

## Data Cleaning and Transformation
After collection, the raw data is cleaned and transformed to ensure it is suitable for analysis. The key steps involve handling missing values, removing duplicates, and standardizing the data formats.

### Main Tasks:
- Remove unnecessary or corrupt data.
- Standardize formats for text and images.
- Save cleaned data as `preprocessed_tg_data.csv`.

---

## Object Detection using YOLO
**YOLO (You Only Look Once)** is applied to analyze the images and videos related to Ethiopian medical businesses. This allows for the automatic detection and classification of relevant objects such as medical equipment, products, and services.

### Steps:
1. Image and video input is processed using **YOLO**.
2. Detected objects are stored in the PostgreSQL database for further analysis.

---

## API Development with FastAPI
A **FastAPI** application is developed to expose the cleaned and processed data, allowing other applications or users to query the data easily.

### Features:
- Support for **CRUD operations** on the data.
- Fast and efficient querying of business-related data.
- Integrated with a PostgreSQL backend.

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hermelawesene/Kara-solution-WEEK7.git
   ```
   
