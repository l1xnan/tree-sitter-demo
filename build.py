from tree_sitter import Language, Parser


languages = [
    "vendor/tree-sitter-go",
    "vendor/tree-sitter-javascript",
    "vendor/tree-sitter-python",
]

Language.build_library(
    # Store the library in the `build` directory
    "build/languages.so",
    # Include one or more languages
    languages,
)


GO_LANGUAGE = Language("build/languages.so", "go")
JS_LANGUAGE = Language("build/languages.so", "javascript")
PY_LANGUAGE = Language("build/languages.so", "python")

parser = Parser()
parser.set_language(PY_LANGUAGE)

code = """
def foo():
    if bar:
        baz()
"""

tree = parser.parse(bytes(code, "utf8"))
print(tree.text)
