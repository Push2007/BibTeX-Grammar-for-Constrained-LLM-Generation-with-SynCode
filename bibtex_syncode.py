from syncode import Syncode
from lark import Lark

# Load BibTeX grammar
with open("bibtex.lark", "r") as f:
    grammar = f.read()

# Lark parser
parser = Lark(grammar, start="start", parser="lalr")

# Load SynCode
syn_llm = Syncode(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    grammar=grammar,
    parse_output_only=True,
    max_new_tokens=300
)


seed = "Create a BibTeX entry for a recent paper on LLM security. That's all, nothing else."

# Generate BibTeX
output = syn_llm.infer(seed)[0]
print("SynCode raw output:")
print(repr(output))

# Validate only if non-empty
if output.strip():
    parser.parse(output)
    print("Generated valid BibTeX:")
    print(output)
else:
    print("SynCode returned no valid BibTeX content.")

