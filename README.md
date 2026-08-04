<div align="center">

# 🔗 URL Shortener API

A production-style URL shortener backend built with FastAPI, SQLAlchemy, and SQLite.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Architecture](#architecture)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [API Documentation](#api-documentation)
- [Example Requests](#example-requests)
- [Screenshots](#screenshots)
- [Project Workflow](#project-workflow)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features

- Generate unique Base62 short codes for any valid URL
- Redirect from short code to original URL
- Click-count analytics per short URL
- Collision-safe code generation with automatic retry
- Centralized error handling with clean JSON error responses
- Auto-generated interactive API docs (Swagger/OpenAPI)

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite |
| Validation | Pydantic |
| Server | Uvicorn |

## Folder Structure