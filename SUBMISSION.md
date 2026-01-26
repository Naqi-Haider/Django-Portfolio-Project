# Term Project - Web Fall 2025

## Personal Portfolio Website

**Student Name:** Naqi Haider  
**Student ID:** F2022266523  
**Course:** Web Development - Fall 2025

---

## Project Overview

A personal portfolio website built using Django framework with a multi-page architecture. The website fetches all content dynamically from a database and includes an admin dashboard for managing content.

## Technology Stack

- **Backend:** Django 6.0 (Python)
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Version Control:** Git/GitHub

## Project Structure

The project is organized into 5 separate Django apps:

| App | Description | URL |
|-----|-------------|-----|
| Bio | Home page with profile information | `/` |
| Education | Academic qualifications | `/education/` |
| Skills | Technical and soft skills | `/skills/` |
| Experience | Professional and academic experience | `/experience/` |
| Projects | Personal and academic projects | `/projects/` |

## Features

### Public Pages
1. **Home Page** - Bio section with name, title, and description
2. **Education Page** - List of academic qualifications
3. **Skills Page** - Technical skills organized by category
4. **Experience Page** - Professional and academic experiences
5. **Projects Page** - Portfolio of personal/academic projects

### Admin Features
- Secure login system
- Admin dashboard for content management
- CRUD operations for all sections:
  - Add, Edit, Delete education entries
  - Add, Edit, Delete skills
  - Add, Edit, Delete experience entries
  - Add, Edit, Delete projects

## Database Models

### Bio Model
- Name
- Job Title
- Description
- Profile Picture URL

### Education Model
- Degree
- Institution
- Start Year / End Year
- Description

### Skill Model
- Name
- Category (Programming, Frameworks, Tools, Soft Skills)
- Description

### Experience Model
- Title
- Organization
- Type (Professional/Academic/Internship)
- Start Date / End Date
- Description

### Project Model
- Title
- Project Type (Personal/Academic/Freelance)
- Technologies
- Description
- GitHub Link
- Live Demo Link

## Deployment

**Repository:** https://github.com/Naqi-Haider/Django-Portfolio-Project

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Naqi-Haider/Django-Portfolio-Project.git

# Navigate to project directory
cd Django-Portfolio-Project

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## Screenshots

The website includes the following pages:
- Home page with profile bio
- Education page with academic history
- Skills page with interactive skill display
- Experience page with work history
- Projects page with project portfolio
- Admin dashboard for content management

---

**Submitted by:** Naqi Haider (F2022266523)  
**Date:** January 2026
