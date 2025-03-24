def macro_processor(source_code):
    macro_definitions = {}
    output = []
    lines = source_code.split("\n")
    in_macro = False
    macro_name = ""
    macro_body = []

    for line in lines:
        words = line.split()

        if not words:
            continue

        if words[0] == "MACRO":
            in_macro = True
            macro_name = words[1]
            macro_body = []
        elif words[0] == "MEND":
            in_macro = False
            macro_definitions[macro_name] = macro_body
        elif in_macro:
            macro_body.append(line)
        elif words[0] in macro_definitions:
            expanded_macro = [stmt.replace("&ARG", words[1]) if "&ARG" in stmt else stmt for stmt in
                              macro_definitions[words[0]]]
            output.extend(expanded_macro)
        else:
            output.append(line)

    return "\n".join(output)


# Example source code with macros including arguments
source_code = """
MACRO ADD &ARG
LOAD &ARG
ADD B
STORE &ARG
MEND
START
ADD A
ADD C
END
"""

expanded_code = macro_processor(source_code)
print(expanded_code)
