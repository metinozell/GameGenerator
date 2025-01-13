# Game Story and Character Generator

This project focuses on creating a program that generates unique game stories and characters with dynamic visualizations based on predefined genres and themes. It combines text generation and image synthesis to produce immersive narratives and character designs for game developers and storytellers.

## Overview

The project includes the following features:

1. **Story Generator**:
   - Automatically generates a unique game story based on a randomly selected genre and theme.
   - Creates immersive narratives set in vibrant, dynamic worlds.

2. **Character Creator**:
   - Generates character profiles with attributes like name, race, class, and traits.
   - Visualizes characters using **Stable Diffusion** to produce highly detailed fantasy-style illustrations.

## Features

- Random generation of game stories across genres such as fantasy, sci-fi, mystery, and more.
- Character creation with distinct personality traits, professions, and visual renderings.
- Uses Hugging Face's `Stable Diffusion` for AI-driven character illustrations.

## Requirements

- Python 3.9 or higher
- Hugging Face token (stored in `hugtoken.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/game-story-character-generator.git
   cd game-story-character-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Hugging Face token:
   - Save your Hugging Face token in a file named `hugtoken.txt` in the project root directory.

4. Run the program:
   ```bash
   python main.py
   ```

## How It Works

### Story Generation
The program selects a random genre and theme, constructs an immersive game narrative, and saves it to a `story.txt` file.

### Character Creation
The program randomly generates a character with attributes and uses **Stable Diffusion** to create an artistic visualization. The resulting image is saved as `<character_name>_character_card.png`.

## Example Outputs

### Generated Story
- **Genre**: Fantasy  
- **Theme**: Heroism  
- **Story**:
  ```
  In a world shaped by heroism, our tale begins in a mystical forest. The protagonist, while living a mundane life, suddenly finds themselves thrust into a grand adventure. Everything changes when a powerful sorcerer threatens the peace of the realm. Through trials and challenges, they forge unexpected alliances and confront inner conflicts, ultimately uncovering a deeper mystery that threatens the world's very existence.
  ```

### Character Profile
- **Name**: Clea  
- **Race**: Elf  
- **Class**: Wizard  
- **Trait**: Wise  

### Character Visualization
![Character Example](Dara_character_card.png)

### Character Visualization
![Character Example](Borin_character_card.png)

## Future Improvements

- Expand genre and theme library.
- Enhance character customization options.
- Add more advanced visualization settings.
- Develop a graphical user interface (GUI).

## Conclusion

This project demonstrates the power of AI in automating creative processes, offering game developers and storytellers a unique tool for rapid prototyping of stories and characters.

---

## Contribution
Feel free to open issues or submit pull requests to improve this project.

---

## License
This project is licensed under the MIT License.

---

Enjoy creating unique stories and characters!

---

## requirements.txt

```plaintext
transformers
diffusers
torch
numpy
```

