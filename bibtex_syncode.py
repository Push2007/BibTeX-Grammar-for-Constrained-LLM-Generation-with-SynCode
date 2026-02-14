from syncode import Syncode
from lark import Lark

# Load BibTeX grammar
with open("bibtex.lark", "r") as f:
    grammar = f.read()

# SynCode Integration
original_syn_llm = Syncode(model="meta-llama/Llama-3.2-1B-Instruct", mode='original', device="cpu", max_new_tokens=150)
syn_llm = Syncode(model="meta-llama/Llama-3.2-1B-Instruct", grammar=grammar, parse_output_only=True, device="cpu", max_new_tokens=150)

seed1 = "Return a BibTeX citation for a conference paper by authors Smith and Johnson? Please do not repeat fields?"
#seed 1 is good

seed4 = "Return a BibTeX citation for a recent article on LLM security?"

seed2 = "Return a BibTeX citation on Marie Curie’s Ph.D. Thesis on Radioactive substances? Please use the @phdthesis entry type?"
#Seed2 is okay

seed3 = "Return a BibTeX citation for a paper on fiber optic telemetry systems by Murilidhar Seshadri?"
#Seed3 is great

# Constrained vs Unconstrained Outputs
output1 = syn_llm.infer(seed1)[0]
original_output1 = original_syn_llm.infer(seed1)[0]

output2 = syn_llm.infer(seed2)[0]
original_output2 = original_syn_llm.infer(seed2)[0]

output3 = syn_llm.infer(seed3)[0]
original_output3 = original_syn_llm.infer(seed3)[0]

print("PROMPT 1: " + seed1 + "\n")
print("SynCode Modified model's normal output:")
print(output1.strip() + "\n")
print("SynCode Original model's normal output:")
print(original_output1 + "\n")

print("PROMPT 2: " + seed2 + "\n")
print("SynCode Modified model's normal output:")
print(output2.strip() + "\n")
print("SynCode Original model's normal output:")
print(original_output2 + "\n")

print("PROMPT 3: " + seed3 + "\n")
print("SynCode Modified model's normal output:")
print(output3.strip() + "\n")
print("SynCode Original model's normal output:")
print(original_output3 + "\n")


