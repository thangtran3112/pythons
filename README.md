## This Python repo is setup with `conda` (recommended):

- Install Miniconda or Anaconda. Anaconda has more packages

```bash
    brew install anaconda
    echo 'export PATH=/opt/homebrew/anaconda3/bin:$PATH' >> ~/.zshrc
    conda init zsh
    source ~/.zshrc
```

```bash
    conda create -p venv python=3.12
    conda activate venv/
```

- For Miniconda, we need to install specific python version:

```bash
    conda install python=3.12
```

## Install extra packages, such as `ipykernel`, `numpy`, etc

```zsh
    conda activate venv/
    pip install -r requirements.txt
```

or

```bash
    conda install -p /Users/trathanl/pythons/venv ipykernel --update-deps --force-reinstall  #This is better, it only changes venv

    pip install ipykernel # Alternative
```

## Other way of creating python venv with python

```bash
    python -m venv myenv
    myenv/Scripts/activate
```

Now we can install packages for `myenv`, such as

```bash
    pip install numpy
```

To deactivate, run `deactivate`

## Another way of setting up environment with virtualenv

```bash
    pip install virtualenv
    virtualenv -p python3 virtual_env
```

To activate:

```bash
    virtual_env/Scripts/activate
```

To deactivate:

```bash
    deactivate
```

## Using Ruff to check code style and grammars
