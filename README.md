# Full Stack Application Development Capstone Project - Dealership Management Web Application

## Project Overview
The **Dealerships Management & Reviews Application** is a cloud-native full-stack web application designed for a national car dealership network. The platform allows users to browse dealerships across different states in the United States, view detailed dealership profiles, browse vehicle inventories (car makes and models), read sentiment-analyzed customer reviews, and submit authenticated reviews.

## Architecture & Technology Stack
- **Frontend:** React, HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend / User Authentication:** Python, Django Web Framework, SQLite
- **Dealership & Reviews Database / Microservice:** Node.js, Express.js, MongoDB / Mongoose
- **AI Sentiment Analyzer Microservice:** Python, Flask, NLTK SentimentIntensityAnalyzer (VADER)
- **Containerization & Deployment:** Docker, Kubernetes / IBM Cloud Code Engine
- **DevOps & Automation:** GitHub Actions CI/CD Pipeline for continuous integration and linting

## Features
- **User Authentication:** Secure user registration, login, and session-based logout with CSRF protection.
- **Dealership Directory:** Dynamic browsing and state-filtering of dealerships across the country.
- **Dealer Details & Reviews:** View comprehensive dealer location info alongside real customer reviews with automated sentiment indicators (Positive, Neutral, Negative).
- **Review Submission:** Authenticated customers can post detailed reviews specifying purchase details, car make, model, and year.
- **Administrative Portal:** Django Admin interface for managing Car Makes, Car Models, and dealership inventory relationships.

## Project Structure
```
├── README.md
├── server/
│   ├── database/                     # Node.js Express & MongoDB microservice
│   │   ├── data/                     # JSON datasets for dealerships & reviews
│   │   ├── app.js                    # Express REST API endpoints
│   │   └── Dockerfile
│   ├── djangoapp/                    # Django application backend
│   │   ├── microservices/            # Sentiment analyzer Flask microservice
│   │   ├── models.py                 # CarMake and CarModel models
│   │   ├── views.py                  # API endpoints and proxy routes
│   │   ├── urls.py                   # App routing
│   │   └── admin.py                  # Django administration configuration
│   ├── djangoproj/                   # Django project configuration
│   └── frontend/                     # React frontend & static HTML pages
│       ├── src/components/           # React components (Login, Register, Dealers, etc.)
│       └── static/                   # Static HTML assets (About.html, Contact.html)
└── .github/workflows/ci.yml          # GitHub Actions CI/CD pipeline
```

## Authors & Acknowledgments
- **Developer:** Asawari Pawar
- **Course:** IBM Cloud-Native Full Stack Development Capstone (Coursera)
- **Sponsor:** IBM Developer Skills Network
