r# Job-Board
A Job portal on IBM cloud


# Job Board Project

Welcome to the Job Board project, a web application built using Python Flask and deployed on the IBM Cloud platform. This platform allows users to post job listings, apply for jobs, and review job listings. The technologies used include HTML, CSS, Python, and Docker for containerization.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Features

- **Job Posting:** Employers can post job listings, providing detailed information about the position, requirements, and application process.

- **Job Application:** Job seekers can apply for jobs directly through the platform by submitting their resumes and relevant details.

- **Job Review:** Users can review and rate job listings, providing feedback to employers and helping others make informed decisions.

## Technologies Used

- **Python Flask:** The web application is built using the Flask web framework to handle server-side logic and routing.

- **HTML and CSS:** The front-end is designed using HTML for structure and CSS for styling, providing a clean and intuitive user interface.

- **Docker:** Containerization is implemented using Docker, ensuring easy deployment and scalability.

- **IBM Cloud Platform:** The application is deployed on the IBM Cloud platform, offering scalability, reliability, and a range of cloud services.

- **Database :**  IBM Db2

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Python](https://www.python.org/) (version 3.x)
- [Docker](https://www.docker.com/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ayushjain2163/Job-Board.git
    cd Job-Board
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Build and run the Docker container:

    ```bash
    docker build -t Job-Board .
    docker run -p 5000:5000 Job-Board
    ```

5. Access the application in your browser at `http://localhost:5000`.

## Usage

1. Navigate to the application in your browser.

2. Explore job listings, post new jobs, apply for positions, and leave reviews.

3. Make sure to log in to access personalized features and track your applications.

## Contributing

Feel free to contribute to the development of this project. Fork the repository, make your changes, and submit a pull request.


## Acknowledgments

- Special thanks to the Flask and Docker communities for providing excellent tools and documentation.
- IBM Cloud for offering a reliable platform for deployment.
- Contributors and users who provide valuable feedback to improve the project.
