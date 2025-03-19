# Scripts
Small, bare minimum projects with some useful functionality written in Python and Bash. The following is a list of scripts in this repository:
- web_scraper.py - web scraper for https://afltables.com/afl/stats/2024.html#. Scrapes Adelaide player numbers, names, games played and writes them into a .CSV file.
- fc.sh - a find-and-copy script written in Bash
- palette_generator.py
---
## palette_generator.py 
Has a single function that generates colour palettes based on a list of hex value inputs
- Allows size to be passed as a tuple (_width_, _height_) 
- saturation values for selective colours as a dictionary 
### Example:
```python 
web_palette = ['#7BB8E9', '#074869', '#077FBA', '#B1CBE0', '#1B8DEB', '#9B9898', '#000000']
palette_generator(web_palette, with_saturation={'#7BB8E9': 0.32, '#074869': 0.54, '#1B8DEB': 0.16, '#9B9898': 0.7})
```
#### Output
![image](https://github.com/user-attachments/assets/23bd6174-890a-488d-bc8c-c810e25fe928)







