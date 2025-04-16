# Rootstrap_sql_head

AI agent that lets you talk to your database using natural language.

Features:

- AI Agent that can answer questions about your database
- Works with SQLite database (can be adapted to other databases)
- Runs tools (`list_tables`, `sample_table`, `describe_table`, `execute_sql`) and provides reasoning
- Uses Groq API for powerful language model capabilities

## Install

Make sure you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/).

Clone the repository:

```bash
git clone https://github.com/claramedeiros-ctrl/txtosqlbot.git
cd txtosqlbot
```

Install Python:

```bash
uv python install 3.12.8
```

Create and activate a virtual environment:

```bash
uv venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

Install package in editable mode:

```bash
uv pip install -e .
```

Install pre-commit hooks:

```bash
uv run pre-commit install
```

### Create SQLite database

You can use any SQLlite database. This project comes with a sample script that can create one for you:

```sh
bin/create-database
```

This should create a file called `ecommerce.sqlite` in the `data` directory. Here's a diagram of the database schema:

![SQLite database schema](.github/db-schema.png)

### Run Ollama, Qwen, and Groq API Setup

txtosqlbot can use Ollama for LLM inference. 
One model you can use is `gemma3-tools:12b`:

```bash
ollama pull PetrosStav/gemma3-tools:12b
```

But I found that it won't work well (not good enough tool support). Another good option is Qwen 2.5 7B:

```bash
ollama pull qwen2.5
```
### (Optional) Groq API

You can also use models from Groq. You'll need to:

Get your API key from https://console.groq.com/keys
Rename the .env.example file to .env and add your API key:

```bash
# On Windows
rename .env.example .env
# On macOS/Linux
mv .env.example .env

#edit the .env file to add your Grow API Key: 
#GROQ_API_KEY=your_api_key_here
```

Look into the [`config.py`]file to set your preferred model.

(Optional) Ollama Integration
The application can also use Ollama for local LLM inference:

```bash
# On Windows/macOS
ollama pull qwen2.5

```
You can configure which model to use in the config.py file.

## Run the Streamlit app

Run the app:

```bash
streamlit run app.py
```