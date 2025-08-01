# my-first-repo-Python-summer-2025


I added this sentence using the Github online interface to edit the file.

# My First Repo!

This is the README.md file. It uses the markdown language.

Here is a list:

  + Item 1
  + Item 2
  + Item 3

For more information about Markdown syntax, see the [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).

## Setup

Create an activate a virtual enviornment:

```sh
conda create -n my-first-env-2025 python=3.11

conda activate my-first-env-2025
```

```sh
pip install pytest
```

```sh
pip install -r requirements.txt
```

## Usage

Play a game of rock, paper, scissors:

### only work if this file does NOT import from other local py files
```sh 
python app/rps.py
```

### if this file imports from other local py files
```sh
python -m app.rps
```

## How we run the Web App

```sh
FLASK_APP=web_app flask run
```

## How we visit it in the browser

http://127.0.0.1:5000 


## Tests 

Run the tests: 

```sh
pytest
```