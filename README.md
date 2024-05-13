# Flask Faculty Slots Selection System

## Overview
This Flask project is a web application for managing student slot selections for faculty meetings. It allows students to register, log in, select available slots, and view their selected slots.

## Features
- User registration and authentication
- Slot selection for faculty meetings
- View selected slots

## Installation
To run this Flask application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/code-with-aneesh/My_Time_Table
    ```

2. **Navigate to the project directory**:
    ```bash
    cd your-repository
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Ensure you have MySQL installed and running.
    - Create a MySQL database named `the_app`.
    - Import the SQL schema provided in `database_schema.sql` to create the required tables.

5. **Run the application**:
    ```bash
    python app.py
    ```

6. **Access the application**:
    Open a web browser and go to `http://localhost:5000` to access the application.

## Usage
- **Register/Login**: Users can register for an account or log in if they already have one.
- **Select Slots**: Logged-in users can select available slots for faculty meetings.
- **View Selected Slots**: Users can view the slots they have selected.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
