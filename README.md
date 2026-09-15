# game-prediction

An unfinished Flask scaffold that was meant to scrape football team form from SofaScore and ask a
local DeepSeek-R1 model to predict a match outcome.

> **This does not run.** It is an early sketch, not a working application. The sections below
> describe what the code says, and what is wrong with it, rather than pretending otherwise.

## What the code contains

| File | Contents |
| --- | --- |
| `predictor.py` | The Flask app — a single `/` route that takes a team name, scrapes it, predicts, and saves the result to MongoDB |
| `app.py` | `predict_match_outcome()` — loads `deepseek-ai/DeepSeek-R1` via `transformers` and generates a completion from a prompt |
| `scraper.py` | `scrape_match_data()` — fetches a SofaScore team page |
| `database.py` | PyMongo client, `soccer_db.matches` collection |
| `config.py` | Two placeholder strings: `MONGO_URI` and `OPENAI_API_KEY` |
| `models.py` | Empty file |
| `templates/`, `static/` | A base template, a one-input form, and a stylesheet |

## Why it doesn't work

1. **The files are wired up backwards.** `predictor.py` holds the Flask app and does
   `from predictor import predict_match_outcome` — importing from itself. That function actually
   lives in `app.py`. The import fails immediately.
2. **The scraper doesn't scrape.** `scrape_match_data()` requests the page and builds a
   `BeautifulSoup` object, then throws it away and returns hardcoded placeholder data
   (`"recent_form": "WDLWW"`, `"injuries": ["Player A - Hamstring", ...]`). No real data is ever
   extracted. SofaScore is also a JavaScript-rendered site, so `requests` + BeautifulSoup would not
   have worked without a different approach.
3. **The model is not runnable on ordinary hardware.** `AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1")`
   pulls a several-hundred-billion-parameter model into memory. `requirements.txt` also lists
   `openai`, and `config.py` has an `OPENAI_API_KEY` placeholder, suggesting an API-based approach
   was considered at some point — but no OpenAI code was ever written.
4. **`config.py` ships placeholder values**, so the MongoDB client cannot connect.

## Tech stack (as declared)

Flask, PyMongo, Requests + BeautifulSoup 4, Hugging Face `transformers` + `torch`, and `openai`
(listed in `requirements.txt` but never imported).

## If you want to revive it

The minimum to get something running:

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt      # note: pulls torch; the DeepSeek-R1 download is not viable
```

1. Move `predict_match_outcome()` out of `app.py` into `predictor.py` (or fix the import to
   `from app import predict_match_outcome`), and rename the files so the Flask entry point is `app.py`.
2. Replace `deepseek-ai/DeepSeek-R1` with a hosted API call or a small local model.
3. Write a real parser, or swap SofaScore for an API with a public football-data endpoint.
4. Fill in `config.py` from environment variables rather than committing values.

**TODO: verify** whether a working version ever existed outside this repo — the committed history
(the last commit deletes an `index.html`) does not contain one.

## Status

**Abandoned prototype.** Last commit February 2025. No `.gitignore`.

## Licence

**Proprietary software — all rights reserved.** Copyright © 2026 Joel Harold Onyango.

This repository is not open source. The full terms are in [LICENSE](LICENSE); in
summary, you may not copy, redistribute, modify, sublicense, publish, re-host or
commercially exploit this software, in whole or in part, without the prior
written permission of the copyright holder. Access to this repository does not
grant any licence beyond reading it.
