# Web Scrapers for Romanian Job Sites

Welcome to the repository of web scrapers designed to extract job listings from various Romanian job sites. This project aims to provide a comprehensive toolset for gathering, validating, and processing job data efficiently.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Scrapers Included](#scrapers-included)
- [Validation Functions](#validation-functions)
- [Contributing](#contributing)
- [Contact](#contact)

## About the Project

This repository contains a collection of web scrapers written in Python, specifically targeting job listing websites in Romania. The scrapers are designed to handle various formats and ensure data consistency through a set of validation functions.

## Features

- **Multiple Site Support**: Scrapers for different job sites in Romania.
- **Data Validation**: Functions to validate and clean the scraped data.
- **Easy to Extend**: Modular design to easily add new scrapers.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/HardChallenge/Scrapers_PeViitor_Razvan.git
    cd Scrapers_PeViitor_Razvan
    ```

2. **Install required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run a scraper and send data to peviitor.ro**:
     ```sh
    cd sites
    python3 scraper_name.py
    ```


## Scrapers Included

- **GFK Scraper**: Scrapes job listings from GFK.
- **Sievo Scraper**: Scrapes job listings from Sievo.
- **Von Consulting Scraper**: Scrapes job listings from Von Consulting.

Each scraper is located in the `sites` directory and can be run individually or together using the provided scripts.

## Validation Functions

- **validate_city(city)**: Ensures the city is spelled correctly. It's using the following:
     - counties (Map<String, List\<String>>): can identify a county based on a city
     - abreviate_counties (Map<String, Map\<String, String>>): same as 'counties', but names are abreviated

Validation functions are located in the `src` directory and are automatically applied during the scraping process.

## Contact

For questions or suggestions, feel free to contact me through [chichiraurazvan@yahoo.com](mailto:chichiraurazvan@yahoo.com).

---

Thank you for visiting my repository!
