# LightView Insurance

## Overview

This project is an insurance application built using Django, designed to manage various aspects of insurance policies, claims, and customer interactions. The application allows users to create and manage insurance policies, file claims, and access detailed information about their insurance coverage.

## Features

- **User Authentication**: Secure login and registration system with role-based access control for administrators and customers.
- **Policy Management**: Allows users to view, create, and manage their insurance policies, including policy details, premiums, and coverage information.
- **Claims Processing**: Users can file claims online, track the status of their claims, and receive updates from the insurance provider.
- **Admin Dashboard**: Provides administrators with a comprehensive view of the system, including policy management, claims processing, and customer support.
- **Notifications**: Automated email notifications for policy renewals, claim updates, and other important events.
- **Search and Filter**: Powerful search and filter options to help users quickly find relevant information.

## Technologies Used

- **Backend**:
  - Django
  - Python
  - Django Rest Framework (for API development)



- **Database**:
  - SQLite 

- **APIs**:
 
  - Celery (for handling asynchronous tasks)
  - Redis (for caching and background task management)
  - Docker (for containerization, if used)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/insurance-application.git
