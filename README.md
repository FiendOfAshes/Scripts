# Scripts
Small, bare minimum projects with some useful functionality written in Python and Bash. The following is a list of scripts in this repository:
- fc.sh - a find-and-copy script written in Bash
- palette_generator.py
- pdf_spider.py
---
## palette_generator.py 
Has a single function that generates colour palettes based on a list of hex value inputs and:
- saturation values for selective colours as a dictionary 
### Example:
```python 
web_palette = ['#7BB8E9', '#074869', '#077FBA', '#B1CBE0', '#1B8DEB', '#9B9898', '#000000']
palette_generator(web_palette, with_saturation={'#7BB8E9': 0.32, '#074869': 0.54, '#1B8DEB': 0.16, '#9B9898': 0.7})
```
#### Output
![image](https://github.com/user-attachments/assets/23bd6174-890a-488d-bc8c-c810e25fe928)

--- 






