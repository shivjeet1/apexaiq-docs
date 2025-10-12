---
layout: default
title: "WEEK3 Documentation"
### This Readme consists all the tasks required to be completed before the end of [WEEK3]
---

# Wallhaven Wallpaper Downloader

- This Documentation provides steps to be followed for setup and running of walpaprdl.py script, a command-line tool for downloading wallpapers from [wallhaven.cc](wallhaven.cc)
---

## Fork/Clone the repository
- Clone the Repository:
    ```bash
        git clone https://github.com/shivjeet1/apexaiq-docs.git
- Navigate to 'walpaprdl':
    ```bash
        cd apexaiq-docs/week2/code/walpaprdl

## Steps to Run 'walpaprdl'

1. Create a venv:
    ```bash
        python -m venv wal 

2. Activate your venv:
    - Linux
        ```bash
            source wal/bin/activate
    - Windows
        ```cmd
            .\wal\Scripts\activate

3. Install dependencies:
    ```bash
        pip install -r requirements.txt

4. Run walpaprdl:
    ```bash
        python walpaprdl.py 

5. Deactivate your venv:
    ```bash
        deactivate 


