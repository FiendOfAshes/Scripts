# Scripts
Small, bare minimum projects with some useful functionality written in Python and Bash. The following is a list of scripts in this repository:
- fc.sh - a find-and-copy script written in Bash (==currently being updated.==)
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

## pdf_spider.py
Uses ```scrapy``` and ```pymupdf``` package to search for a word/phrase in past papers. It lists down papers containing the word/phrase along with the page number in a text file. 

- The ```allowed_domains``` and ```start_urls``` variables can be changed. 
- On Line 34, the ```needle``` variable can be changed to a different phrase. 
- Lines 16-17 can be uncommented to allow recursive searching for urls
- Line 19 and 20 can be modified for more specific urls

### Example
In yout terminal:
```python
scrapy runspider pdf_spider.py
```
#### Output
![image](https://github.com/user-attachments/assets/d16fdeba-57f8-41f9-a45a-eebc99fc8150)


