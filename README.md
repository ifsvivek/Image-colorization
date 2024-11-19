# Image Colorization App

This project is an image colorization application that uses deep learning models to colorize grayscale images.

## Table of Contents
- [Image Colorization App](#image-colorization-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Models](#models)
  - [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/image-colorization-app.git
    cd image-colorization-app
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    streamlit run app.py
    ```

2. Upload a grayscale image using the file uploader in the web interface.

3. The application will colorize the image and display the result.

## Models

This project uses two pre-trained models for colorization:
- ECCV16
- SIGGRAPH17

The models are defined in the `colorizers` directory:
- [ECCV16](colorizers/eccv16.py)
- [SIGGRAPH17](colorizers/siggraph17.py)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.