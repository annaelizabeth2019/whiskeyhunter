# Whiskey Hunter

**Whiskey Hunter** is a Django-based web application designed to help users discover and explore different types of whiskey. This project was created to familiarize myself with the basic functions of Django, including creating models, views, templates, and integrating a database.

## Features

- **Whiskey Database**: Store and manage a collection of whiskey entries.
- **Search Functionality**: Search for whiskeys by name, type, or origin.
- **User Interface**: Simple and intuitive UI built with Django templates.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/whiskey-hunter.git
   cd whiskey-hunter
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python3 manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python3 manage.py runserver
   ```

6. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate through the application to browse and search for different whiskeys.
- Add new entries or update existing ones as needed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
