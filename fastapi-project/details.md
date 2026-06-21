# Smart File Vault API

## Overview

Smart File Vault is a secure file management system built using FastAPI. The application allows users to upload, manage, update, and delete files while implementing modern backend engineering practices such as authentication, authorization, validation, middleware, rate limiting, and containerized deployment.

The goal of this project is to gain hands-on experience with API development, security, database management, deployment, and backend architecture.

---

## Objectives

* Learn FastAPI fundamentals
* Implement JWT Authentication
* Implement Access and Refresh Tokens
* Build CRUD APIs
* Use UUIDs instead of sequential IDs
* Apply request validation
* Implement middleware
* Add rate limiting
* Design a relational database
* Containerize using Docker
* Deploy on AWS EC2 using Nginx

---

## Features

### Authentication

* User Registration
* User Login
* Access Token Generation
* Refresh Token Generation
* Protected Routes

### File Management

* Upload File
* View Uploaded Files
* Update File Metadata
* Delete Files

### Validation

* File Size Validation
* File Type Validation
* Request Data Validation

### Security

* JWT Authentication
* Password Hashing
* Rate Limiting
* Middleware Logging

---

## Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* JWT
* Docker
* AWS EC2
* Nginx

---

## Database Entities

### User

* UUID
* Name
* Email
* Password Hash
* Created At

### File

* UUID
* File Name
* File Path
* File Size
* Uploaded By
* Created At

---

## Future Enhancements

* Role-Based Access Control
* File Sharing
* Cloud Storage Integration
* Email Notifications
* Audit Logs

---

## Status

Project currently under development as part of a 20-day backend engineering challenge.
