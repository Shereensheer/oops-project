"# oops-project" 
# 🖼️ Multi Image Generator (OOP-based Streamlit App)

A simple and elegant image generator app built using **Python**, **Object-Oriented Programming (OOP)**, and **Streamlit**. Enter a keyword, choose how many images you want, and get fresh images from **Unsplash API** — with download functionality!

---

## 🚀 Features

- 🔍 Search for any keyword (e.g., cats, cars, mountains)
- 🧠 Clean class-based architecture using OOP principles
- 🌐 Fetch random images using the Unsplash API
- 🖼️ Display and download images directly in the browser
- 📱 Responsive and user-friendly UI with Streamlit

---

## 📂 Project Structure

```bash
.
├── main.py             # Main Streamlit app with OOP structure
├── requirements.txt    # Required packages
└── README.md           # Project documentation


 OOP Structure
BaseImageGenerator
An abstract class for image generation logic.

UnsplashImageGenerator (inherits from BaseImageGenerator)
Handles API requests and fetching image URLs from Unsplash.

 Setup Instructions
Clone the repo or copy the code files.

Create virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

streamlit run main.py


Unsplash API Access Key
Get your free key from Unsplash Developer Portal

Replace the UNSPLASH_ACCESS_KEY in main.py with your own key.


























