

https://github.com/rastog18/BoilerHush/assets/130913444/3e23e55b-c336-49b8-8959-7f004bf662d6

# BoilerHush

BoilerHush is a website designed to help students find the nearest study spots, and how busy they're currently busy and even allows for room bookings. Inspired by my own experiences of struggling to find a quiet place to study during final exams, I wanted to create a tool that would make this process easier for students.

Throughout development, I faced significant hurdles in integrating JavaScript with Python-Flask, establishing communication channels, and finding suitable APIs for free geocoding services. Overcoming these obstacles required a deep dive into AJAX requests, Flask's routing mechanisms, and the intricacies of asynchronous programming. Thanks to the invaluable support from communities like Stack Overflow and thorough documentation, I not only surmounted these challenges but also honed my skills in web development significantly.

## Data Collection

The application collects data on study spots, including their names, addresses, opening/closing times, and popularity trends. This data is scraped from various sources using the `scrape` module and stored in a binary file (`data.dat`).

The geographical coordinates (latitude and longitude) of each study spot are stored in a text file (`co-ordinates.txt`) for distance calculations.

## Files and Their Roles

- `app.py`: The main Flask application file containing routes and logic for handling requests.
- `scrape.py`: Module for web scraping study spot data.
- `data.dat`: Binary file containing scraped study spot data.
- `co-ordinates.txt`: Text file containing geographical coordinates of study spots.
- `requirements.txt`: List of Python dependencies for the project.
- `templates/`: Directory containing HTML templates for the web pages.
- `static/`: Directory containing static files (CSS, images, JavaScript) for the web pages.

Developed by Shivam Rastogi.
