import re

class LaTeXToken:
    def _init_(self, token_type, content):
        self.token_type = token_type
        self.content = content

    def _str_(self):
        if self.token_type == "Itemize":
            items = "\n".join([f"\\item {item}" for item in self.content])
            return f"\\begin{{itemize}}\n{items}\n\\end{{itemize}}"
        else:
            return ""

def parse_latex(input_text):
    itemize_pattern = r"\\begin\{itemize\}(.+?)\\end\{itemize\}"
    item_pattern = r"\\item\s+(.+)"

    matches = re.findall(itemize_pattern, input_text, re.DOTALL)

    if matches:
        itemize_content = matches[0]
        items = re.findall(item_pattern, itemize_content)
        return LaTeXToken("Itemize", items)
    else:
        return None

f = open("itemize_tag.tex", "r")
input_text = f.read()

result = parse_latex(input_text)
if result:
    print(result.content)  # Print the items only
else:
    print("No itemize token found.")