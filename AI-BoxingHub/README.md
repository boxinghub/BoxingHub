# BoxingHub

## Website: [https://www.boxinghub.org](https://www.boxinghub.org)

### Complete PDF demo of the project: [Project Demo](https://drive.google.com/file/d/1RCXj8eFnj7AJ7g_S6-cP1TJ7YWzh98CX/view?usp=sharing)

### Video demo for the static website: [Watch Here](https://youtu.be/9yuzUpK1MCM)

#### Description
**_BoxingHub_** is a comprehensive web platform designed to promote boxing knowledge and foster a deeper understanding of boxing culture through the integration of artificial intelligence technologies.

#### Author
**Hongbo Wei**  
From Guiyang, China, a professional boxer 🥊 with a passion for AI/ML and software engineering 👨🏻‍💻.

### Overview

BoxingHub is a dynamic web application built using Django, HTML, CSS, JavaScript, and SQLite. Its design is fully responsive, offering a seamless user experience across all devices, including desktops, tablets, and mobile phones.

The platform serves as an educational resource for boxing enthusiasts, providing a wide range of content, including:

- Comprehensive boxing techniques, theories, rules, and gear recommendations.
- Information on top boxing clubs, including addresses and contact details.
- Interactive learning tools, such as an AI-powered boxing chatbot and punch classification feature.
- Developer contact information is available on every page for user support and feedback.

### Deployment

BoxingHub is hosted on a scalable web service platform, integrating Cloudflare CDN for efficient content delivery and SSL certification to ensure a secure network connection.

### Installation Instructions

*Prerequisites: Python 3.11, macOS Sonoma 14.6.1*

Follow these steps to set up the web application:

0. **Acquire API Keys and Access Tokens**
- Access Key and Acess Key ID from [AWS](https://aws.amazon.com/), AWS_DEFAULT_REGION=us-west-2
- Access Tokens from [Hugging Face](https://huggingface.co/)
- AI inference API Key from [Roboflow](https://roboflow.com/)

Put these in secret keys and tokens in a .env file

1. **Install dependencies**  
   ```bash
   pipenv shell
   pipenv install
   ```

2. **Run the server**  
   ```bash
   python manage.py runserver
   ```

### Folder Structure and File Descriptions

#### 1. **Web Application**  
- Contains the core Django framework files for building the website's structure and functionality.

#### 2. **Computer Vision**  
- Includes the components responsible for boxing punch classification using advanced computer vision models.
- **Images for testing can be find in static/images/computer-vision folder.**

#### 3. **Chatbot**  
- Houses the rule-based chatbot files designed to provide interactive learning experiences for users.

#### 4. **AWS LLMs** 
- Contains scripts and configurations for integrating AWS Bedrock with BoxingHub to utilize Large Language Models (LLMs) for generating personalized affirmations and enhancing user engagement. This includes API handling, prompt management, and response parsing.

#### 5. **NLP App** 
- Includes files and modules related to Natural Language Processing (NLP) functionalities used within the BoxingHub platform. This encompasses scripts for chatbot interaction, text analysis, and other NLP-driven features that enhance user interaction and provide educational content dynamically.
- **Audio files for testing can be find in static/audio folder.**

#### 6. **Pipfile and Pipfile.lock**  
- Define the virtual environment settings and dependencies required for the application, ensuring compatibility and reproducibility.

#### 7. **Static Folder**  
- Contains all static assets like CSS, JavaScript, fonts, and images to enhance the website's visual design and responsiveness.

- **bootstrap/**: Controls the aesthetic elements of the web application.
- **css/**: Manages styles related to color, layout, and responsiveness.
- **fonts/**: Defines the typography used across the platform.
- **images/**: Stores all images used, such as logos, backgrounds, and illustrative content.
- **js/**: Handles dynamic behaviors and interactions, such as scroll effects and user engagement features.

#### 8. **Templates Folder**  
Contains HTML files that dictate the layout and structure of each webpage.

- **base.html**  
The foundational layout template from which all other pages are extended.
- **index.html**  
Serves as the homepage, introducing BoxingHub's mission and content.

- **clubs.html**  
Displays information about various boxing clubs.
- **fundamentals.html**  
The Fundamentals page offers a comprehensive guide to boxing basics, covering key techniques, training regimens, and foundational knowledge essential for both beginners and experienced practitioners.
- **gears.html**  
Describes essential boxing gear like gloves, hand wraps, and protective equipment.
- **recovery.html**  
Provides guidance on recovery practices for athletes.
- **rules.html**  
Outlines the fundamental rules of professional boxing.

- **accessibility.html**  
The Accessibility page focuses on enhancing the usability of the platform for users with hearing impairments. It details the integration of advanced accessibility technologies like speech-to-text conversion and speaker diarisation, ensuring an inclusive learning environment.
- **aws_llms.html**  
This page explains the integration of Large Language Models (LLMs) via AWS Bedrock into BoxingHub. It highlights how generative AI provides tailored affirmations and contextual support, enhancing user engagement and motivation.
- **computer-vision.html**  
The Computer Vision page showcases the AI-powered punch classification feature. It utilizes advanced object detection models to analyze and classify boxing punches, providing users with real-time feedback to improve their boxing techniques.



- **moments.html**  
The Moments page is designed to capture and share memorable experiences from the BoxingHub community. It features user-generated content, including training highlights and milestone achievements, fostering a sense of community and shared learning.

---

These descriptions provide a concise overview of each new page added to your BoxingHub project, enhancing the README.md by offering clear insights into their purpose and content.

#### 9. **app.py**  
Contains the Django configuration settings, database connections, and route definitions for navigating the site and interacting with the database.

#### 10. **boxinghub.db**  
An SQLite3 database that records user interactions, such as "likes" and "loves," to enhance user engagement analytics.

---

![BoxingHub Preview](static/images/preview.png "BoxingHub")

😁 **Thank you for your interest in BoxingHub!**

---

© 2023-2049 [Hongbo Wei](https://github.com/hongbo-weia)

[![CC BY 4.0][cc-by-image]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
