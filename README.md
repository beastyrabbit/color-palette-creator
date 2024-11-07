# Color Palette Creator Tool

The Color Palette Creator Tool is a Python-based application that extracts dominant colors from images and generates detailed color palettes with variations in brightness and hue. Useful for color analysis, design projects, and creative inspiration.

GOTO [EXAMPLES](Examples)

## Features
- Extract dominant colors from images.
- Generate brightness and hue variations.
- Save color palettes as PNG files.
- Easy-to-use graphical user interface.

## Available Executable
An executable version of the Color Palette Creator Tool is available in the releases section. You can download and run the .exe without needing to install Python or dependencies. Please note that the .exe is currently not signed, so you may see warnings from your operating system when trying to run it.

I've also started working on macOS and Linux versions of the executable. These are not yet complete but will be available in future releases.

Let me know if you need any other adjustments!

## Important Note
This tool is designed to generate a color palette rather than perform a full picture analysis. For a more detailed color analysis of an image, consider using external tools like [Color Summarizer](https://mk.bcgsc.ca/color-summarizer//).

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/beastyrabbit/color-palette-creator.git
   cd color-palette-creator
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```sh
   python color_palette_creator.py
   ```

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License. See the `LICENSE` file for details.
[Localized License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Examples
### Explaination
In the images below, each pair represents a comparison between an input image (left) and the resulting color palette analysis (right). The analysis image on the right contains six color boxes organized as follows:

Top Colors: The first row on the right includes three boxes representing the main colors extracted from the original image:

Pure Colors: Key colors directly from prominent areas in the image.
Brightness Variations: These same colors adjusted for different brightness levels.
Hue Variations: The same colors with shifted hues.
Color Highlights: The second row contains a similar set of three boxes, but with different pure colors selected from accent and highlight areas in the image, followed by their brightness and hue variations.

Each box can be customized in terms of color count and value adjustments to match specific requirements.

### Pictures 
<p align="center">
  <!-- Combination 1 -->
  <a href="https://commons.wikimedia.org/wiki/File:017_Great_blue_turaco_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/017_Great_blue_turaco_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg/2560px-017_Great_blue_turaco_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg" alt="Original Image 1" width="600px" >
  </a>
  <a href="https://github.com/user-attachments/assets/3fa4ebf0-e65b-4ee5-9792-8fa6478062a4">
    <img src="https://github.com/user-attachments/assets/3fa4ebf0-e65b-4ee5-9792-8fa6478062a4" alt="Color Palette 1" width="67px">
  </a>
</p>

<p align="center">
  <!-- Combination 2 -->
  <a href="https://commons.wikimedia.org/wiki/File:Big_wave_breaking_in_Santa_Cruz.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Big_wave_breaking_in_Santa_Cruz.jpg" alt="Original Image 2" width="600px">
  </a>
  <a href="https://github.com/user-attachments/assets/1c4fbc62-a40e-45b3-b7d8-6b06d18d77fb">
    <img src="https://github.com/user-attachments/assets/1c4fbc62-a40e-45b3-b7d8-6b06d18d77fb" alt="Color Palette 2" width="67px">
  </a>
</p>

<p align="center">
  <!-- Combination 3 -->
  <a href="https://commons.wikimedia.org/wiki/File:003_Olive-bellied_Sunbird_in_flight_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/003_Olive-bellied_Sunbird_in_flight_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg/2560px-003_Olive-bellied_Sunbird_in_flight_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg" alt="Original Image 3" width="600px">
  </a>
  <a href="https://github.com/user-attachments/assets/1a5ca7a8-97db-4d0c-a9fc-4b95565e26f9">
    <img src="https://github.com/user-attachments/assets/1a5ca7a8-97db-4d0c-a9fc-4b95565e26f9" alt="Color Palette 3" width="67px">
  </a>
</p>

<p align="center">
  <!-- Combination 4 -->
  <a href="https://commons.wikimedia.org/wiki/File:Rainbow_yarn_for_knitting,_display_in_front_of_a_needlework_shop_in_Graz,_Austria,_GW23-100.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Rainbow_yarn_for_knitting%2C_display_in_front_of_a_needlework_shop_in_Graz%2C_Austria%2C_GW23-100.jpg/2560px-Rainbow_yarn_for_knitting%2C_display_in_front_of_a_needlework_shop_in_Graz%2C_Austria%2C_GW23-100.jpg" alt="Original Image 4" width="600px" height="400px">
  </a>
  <a href="https://github.com/user-attachments/assets/b126726a-d28f-4d38-98ee-dca006c4f967">
    <img src="https://github.com/user-attachments/assets/b126726a-d28f-4d38-98ee-dca006c4f967" alt="Color Palette 4" width="67px">
  </a>
</p>

<p align="center">
  <!-- Combination 5 -->
  <a href="https://commons.wikimedia.org/wiki/File:Rana_platanera_-_Boana_platanera.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/Rana_platanera_-_Boana_platanera.jpg" alt="Original Image 5" width="600px" height="400px">
  </a>
  <a href="https://github.com/user-attachments/assets/87210282-1e6d-4a80-ba89-7380b608f5fd">
    <img src="https://github.com/user-attachments/assets/87210282-1e6d-4a80-ba89-7380b608f5fd" alt="Color Palette 5" width="67px">
  </a>
</p>

<p align="center">
  <!-- Combination 6 -->
  <a href="https://commons.wikimedia.org/wiki/File:Ratargul_785_retouched.jpg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Ratargul_785_retouched.jpg/2560px-Ratargul_785_retouched.jpg" alt="Original Image 6" width="600px" height="400px">
  </a>
  <a href="https://github.com/user-attachments/assets/8119c49e-d54b-4993-b03b-c93591171cbb">
    <img src="https://github.com/user-attachments/assets/8119c49e-d54b-4993-b03b-c93591171cbb" alt="Color Palette 6" width="67px">
  </a>
</p>



