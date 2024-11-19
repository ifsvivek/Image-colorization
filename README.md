# Image Colorization

This project is an image colorization application that uses deep learning models to colorize grayscale images.

## Table of Contents

- [Image Colorization](#image-colorization)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Models](#models)
  - [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/ifsvivek/Image-colorization
    cd Image-colorization
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

-   [ECCV16](colorizers/eccv16.py)
-   [SIGGRAPH17](colorizers/siggraph17.py)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
