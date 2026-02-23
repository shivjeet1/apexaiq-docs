---
layout: default
title: "WEEK3 Documentation"
### This Readme consists all the tasks required to be completed before the end of [WEEK3]
---

# Selenium Documentation

### **Introduction** 
Selenium is a popular open-source tool for automating web browser interactions. Firefox is a fast and secure web browser developed by Mozilla. Firefox uses GeckoDriver to control and interact with Firefox during automated testing. GeckoDriver is a component of the Selenium automation framework that allows communication between the Selenium WebDriver and the Firefox web browser.
At the core of Selenium is [WebDriver](https://www.selenium.dev/documentation/webdriver/), an interface to write instruction sets that can be run interchangeably in many browsers. Once you’ve installed everything, only a few lines of code get you inside a browser.

#### What is [WebDriver](https://www.selenium.dev/documentation/webdriver/) ?

WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server.

Selenium WebDriver refers to both the language bindings and the implementations of the individual browser controlling code. This is commonly referred to as just WebDriver.
GeckoDriver is designed and developed by Mozilla for Firefox Web Browser which is used to allow developers to automate their interactions with firefox. It is also a component of Selenium WebDriver API and internal communication of Firefox.

* Firefox is a browser which works on Gecko Engine.
* Chrome is a browser which works on Blink Engine which is a fork of Apple's Webkit.

## Selenium Setup on Arch Linux

This guide provides a straightforward method for setting up a Selenium environment on an Arch Linux system. The instructions focus on using Python for scripting and leverage the `pacman` package manager for easy installation of browsers and their corresponding WebDrivers.

### Installation Steps

The setup process is broken down into three main parts: installing a web browser, installing the WebDriver, and installing the Selenium client library for Python.

#### Step 1: Install a Web Browser

Selenium requires a web browser to automate. You can choose between Firefox or Chromium (the open-source foundation of Google Chrome). Install your preferred browser using `pacman`.

* **To install Firefox:**
    ```bash
    sudo pacman -Syu firefox
    ```

* **To install Chromium:**
    ```bash
    sudo pacman -Syu chromium
    ```

#### Step 2: Install the Corresponding WebDriver

The WebDriver is a critical component that allows Selenium to communicate with and control the browser. You must install the driver that matches your chosen browser.

* **For Firefox, install GeckoDriver:**
    ```bash
    sudo pacman -S geckodriver
    ```

* **For Chromium/Chrome, install ChromeDriver:**
    ```bash
    sudo pacman -S chromedriver
    ```

> **Note:** Installing both the browser and its WebDriver from the official Arch repositories via `pacman` is highly recommended. This ensures that their versions are compatible, which helps prevent common `SessionNotCreatedException` errors.

#### Step 3: Install the Selenium Python Library

With the browser and driver installed, the final step is to install the `selenium` library for Python using `pip`.

1.  **Ensure `pip` is installed:** If you don't have it already, install the Python package manager.
    ```bash
    sudo pacman -S python-pip
    ```

2.  **Install the `selenium` library:**
    ```bash
    pip install selenium
    ```

    It is considered a best practice to manage Python project dependencies within a virtual environment. This prevents conflicts with system-wide packages.

    ```bash
    # Create a virtual environment in your project directory
    python -m venv .venv

    # Activate the environment
    source .venv/bin/activate

    # Now, install selenium inside this isolated environment
    pip install selenium

    # To deactivate the environment when you're done, simply run:
    # deactivate
    ```

Your system is now fully configured to write and run Selenium automation scripts with Python on Arch Linux.
