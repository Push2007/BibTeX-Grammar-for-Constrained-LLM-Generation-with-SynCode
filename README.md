# SynCode BibTeX Constrained Generation
![Python Version](https://img.shields.io/badge/python-3.10-blue)
## Assignment Overview
This project demonstrates the use of SynCode to generate BibTeX citations using a constrained grammar. 
The goal is to **strictly** produce valid BibTeX entries in response to natural language prompts.
## Deliverables
1. bibtex.lark
   - Grammar file that models the syntax of a BibTeX citation

2. bibtex_syncode.py
   - Python file that...
       - Integrates the Llama-3.2-1B-Instruct Hugging Face Model with SynCode
       - Integrates the bibtex.lark grammar file with SynCode
       - Runs a series of prompts with the unconstrained & constrained SynCode models
       - Displays an output to said series of prompts, showing the difference in output between the unconstrained & constrained models
