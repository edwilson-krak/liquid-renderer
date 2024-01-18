Script to quickly render liquid templates.

Installation:

```commandline
pip install -r requirements.txt
```

Usage:

- Create a directory at `src/targets/my-test/`
- Create a `template.liquid` file containing the liquid template to render
- Create a `context.json` file containing the context to render the template
  with
- Update the `target` variable in `main.py` to `"my-test"`
- Run `main.py`. The result will be put at `my-test/result.txt` and also printed
  to the terminal

If using Pycharm, installing the [liquid
plugin](https://www.jetbrains.com/help/ruby/liquid.html) is helpful.