# Flash Card App

This is a simple flashcard application built using Python's tkinter library. The application displays French words on one side of the flashcard and their corresponding English translations on the other side. Users can flip the flashcards to reveal the translations and mark their understanding by clicking on "Right" or "Wrong" buttons.

## Getting Started

These instructions will help you run the flashcard application on your local machine.

### Prerequisites

Before running the application, ensure you have Python installed on your system. You'll also need the following files:
- `french_words.csv`: CSV file containing French words and their English translations.
- `images/card_front.png`: Image file for the front side of the flashcard.
- `images/card_back.png`: Image file for the back side of the flashcard.
- `images/right.png`: Image file for the "Right" button.
- `images/wrong.png`: Image file for the "Wrong" button.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Flash-Card-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flash-card-app
   ```

3. Install the required Python libraries:

   ```bash
   pip install pandas
   ```

### Usage

1. Run the script:

   ```bash
   python Flash_Card_App.py
   ```

2. The flashcard application window will open, displaying a French word.
3. Wait for 3 seconds to reveal the English translation automatically, or click on the flashcard to reveal it immediately.
4. Click on the "Right" or "Wrong" buttons to mark your understanding and proceed to the next flashcard.

## Features

- Displays French words and their English translations on flashcards.
- Supports automatic flipping of flashcards after 3 seconds.
- Users can manually flip the flashcards by clicking on them.
- Provides "Right" and "Wrong" buttons for users to mark their understanding.

## Project Structure

- `flash_card_app.py`: Main Python script containing the implementation of the flashcard application.
- `data/french_words.csv`: CSV file containing French words and their English translations.
- `images/`: Directory containing image files for the flashcards and buttons.
- `README.md`: Markdown file containing information about the application and how to use it.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.


## Contact

For any inquiries or support, please contact [abhijeetsapar17@gmail.com].
