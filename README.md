# Movie Recommendation System 🎥

## Overview
This **Movie Recommendation System** is a web application that suggests movies based on user input. The system uses a **content-based recommendation algorithm** to recommend movies similar to those the user likes. The frontend is built using **Streamlit**, and the backend processes are powered by **machine learning**.

## Features
- Users can search for a movie and get a list of similar movies.
- Movie recommendations are based on features such as genre, plot, and user ratings.
- The system uses a **content-based filtering** approach.
- Built with a user-friendly interface using **Streamlit**.
- Data is processed with **Pandas** and **Scikit-learn**.

## Project Architecture
- **Frontend**: Streamlit for the user interface.
- **Backend**: Python-based Machine Learning model using `sklearn`.
- **Database**: MongoDB (optional for storing user ratings or movie metadata).
- **Model**: Content-based recommendation using cosine similarity.

## Requirements
To run this project locally, ensure you have the following installed:

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **MongoDB** (Optional, if you are integrating with a database)

### Install the dependencies
You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

Example `requirements.txt` file:
```text
streamlit
scikit-learn
pandas
numpy
```

## How It Works
1. **Data Preprocessing**: The movie dataset is preprocessed to extract relevant features such as title, genre, and plot.
2. **Model Training**: The system uses **cosine similarity** to compute similarity between movies based on their features.
3. **Recommendation Engine**: When a user inputs a movie, the system finds movies similar to the selected one by computing their cosine similarity score.
4. **Web Interface**: The **Streamlit** interface allows the user to interact with the system easily.

## Getting Started

### Clone the repository
First, clone this repository:

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### Running the Application
Once you have cloned the repository and installed the necessary dependencies, run the application using Streamlit:

```bash
streamlit run app.py
```

This will launch the web app locally, and you can access it at `http://localhost:8501`.

## File Structure
```plaintext
├── app.py               # Main Streamlit application
├── model.py             # Contains the recommendation model logic
├── similarity.pkl       # Precomputed similarity matrix
├── movies.csv           # Dataset containing movie information
├── requirements.txt     # Dependencies
└── README.md            # Project Documentation
```

## Dataset
The dataset used in this project contains metadata of movies such as:
- Movie title
- Genre
- Plot description
- Ratings

This data can be fetched from popular datasets such as **IMDb**, **TMDB**, or **MovieLens**.

## Example Usage
1. Launch the Streamlit application.
2. Enter the name of a movie you like in the search bar.
3. The app will suggest a list of movies similar to the one you searched for.

## Screenshots
![App Interface](./screenshots/app_interface.png)

## Future Enhancements
- **Collaborative Filtering**: Integrating collaborative filtering to recommend movies based on user preferences and ratings.
- **User Authentication**: Adding login functionality for users to save their favorite movie recommendations.
- **Improved UI**: Enhance the UI/UX of the web application with more styling and interactive features.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue to discuss the changes you wish to make.

## License
This project is licensed under the **MIT License**.
