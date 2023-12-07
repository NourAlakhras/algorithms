# Maximum Sum Subarray Finder

## Description
This Flask web application helps you find the maximum sum subarray using various algorithms, including brute force, divide and conquer, classical dynamic programming, and Kadane's dynamic programming.

## Installation
1. Clone the repository:
   git clone <[repository-url](https://github.com/NourAlakhras/algorithms.git)>
   cd cs311


2. Set up a virtual environment (recommended):
   python -m venv venv


3. Activate the virtual environment:
     venv\Scripts\activate

4. Install the dependencies:
   pip install -r requirements.txt


## Usage
1. Run the Flask application:
   python app.py


2. Access the application in your web browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter a comma-separated array of numbers and choose an algorithm from the dropdown menu. Click "Submit" to find the maximum sum subarray.

## Algorithms
- **Brute Force Algorithm:** Finds the maximum sum subarray using nested loops.
- **Divide and Conquer Algorithm:** Utilizes the divide and conquer technique to find the maximum sum subarray.
- **Classical Dynamic Programming Algorithm:** Applies dynamic programming to find the maximum sum subarray.
- **Kadane's Dynamic Programming Algorithm:** Implements Kadane's algorithm to find the maximum sum subarray.

## Folder Structure
- **app.py:** Flask application containing the algorithms and routes.
- **templates/index.html:** HTML template for the web interface.
- **requirements.txt:** List of Python dependencies.
- **.gitignore:** Gitignore file to exclude the virtual environment.

## Contributors
- [Nour Al Akhras – 220410351@psu.edu.sa]
- [Haifa Zain Eddin – 220410581@psu.edu.sa]
- ...