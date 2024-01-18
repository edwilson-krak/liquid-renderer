import json
import pathlib

import liquid


target = "example"
target_path = pathlib.Path(__file__).parent / "targets" / target


def get_template() -> liquid.Template:
    template_path = target_path / "template.liquid"
    with open(template_path, "r") as f:
        return liquid.Template(f.read())


def get_context() -> dict:
    context_path = target_path / "context.json"
    with open(context_path, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    template = get_template()
    context = get_context()
    rendered = template.render(**context)
    print(rendered)

    with open(target_path / "result.txt", "w") as f:
        f.write(rendered)
