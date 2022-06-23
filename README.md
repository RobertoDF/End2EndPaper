# Pyscipaper

Python tool to write a scientific paper with end-to-end reproducibility. Each number present in the paper can be conveniently linked to a data structure via f-Strings.

example:
```
number_areas = 8
f"We analyzed the LFP signals in {number_areas} brain areas... "
```
**Output:**\
We analyzed the LFP signals in 8 brain areas...   
 
## Requirements

https://github.com/elapouya/python-docx-template

## Usage

1. Clone this repo inside your project.
2. Update root directory in example_paper.py to reflect your folder structure.
3. Modify each section of the paper (abstract, introduction....).
4. Run example_paper.py, a formatted docx document will be  saved in the same folder.

