# Template for new Python project
Python boiler-plate templates for with VS Code

## References on setting up Python VSCode environment
* Setting up [VS Code settings, linter and formatter](https://medium.com/@ordinaryindustries/the-ultimate-vs-code-setup-for-python-538026b34d94)
* Setting up [Ruff](https://www.kdnuggets.com/enhance-your-python-coding-style-with-ruff) as the fastest linter
* [Configuring Ruff to use Black Formatter](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
* [Official Ruff Tutorial](https://docs.astral.sh/ruff/tutorial/#rule-selection)

## Recommended VSCode extensions:
* One Dark Pro
* Ruff
* Black Formatter
* Material Icon Theme

## Other Settings:
* Font Size cannot be set through `settings.json`, you will have to set it up through GUI Settings.
* If you're using the [VS Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), you can configure VS Code to fix violations on-save using Ruff, then re-format with the [Black Formatter extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), via the following settings.json:
```
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit"
    },
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```
* If not using [Black Formatter extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) and [VS Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python), we can use the default formatter from `Ruff`:
```
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```
