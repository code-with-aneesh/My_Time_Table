-- Create a table to store user information
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create a table to store faculty slots
CREATE TABLE FacultySlots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    faculty VARCHAR(255) NOT NULL,
    slots DATETIME NOT NULL
);

-- Create a table to store selected slots by users
CREATE TABLE SelectedSlots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    slot_id INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    FOREIGN KEY (slot_id) REFERENCES FacultySlots(id),
    FOREIGN KEY (username) REFERENCES users(username)
);
