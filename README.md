# Crewship Quickstart

A ready-to-deploy CrewAI research crew. Clone it, set your key, deploy — done.

## Deploy in 3 steps

### 1. Clone & install

```bash
git clone https://github.com/Crewship/crewai-quickstart.git
cd crewai-quickstart
# Install the Crewship CLI tool
curl -fsSL crewship.dev/install | bash
```

### 2. Set your API key

```bash
crewship env set OPENAI_API_KEY=sk-...
```

> **Using a different provider?** Change the `llm` field in `config/agents.yaml` and set the matching key instead — e.g. `ANTHROPIC_API_KEY` for Claude, `GROQ_API_KEY` for Groq (free tier), or no key at all for Ollama.

### 3. Deploy

```bash
crewship deploy
```

That's it. Your research crew is live.

---

## What's inside

This template ships a **two-agent research crew** powered by GPT-4o mini:

- **Researcher** — finds the latest info on a topic
- **Reporting Analyst** — turns raw research into a polished markdown report

The default topic is *"AI agents in production"*. Change it in `src/crewship_quickstart/main.py`.

## Run locally (optional)

```bash
cp .env.example .env          # add your OPENAI_API_KEY
crewai run
```

## Customise

- **Agents** → `src/crewship_quickstart/config/agents.yaml`
- **Tasks** → `src/crewship_quickstart/config/tasks.yaml`
- **Crew logic** → `src/crewship_quickstart/crew.py`

## Learn more

- [Crewship docs — Your First Crew](https://docs.crewship.dev/guides/your-first-crew)
- [CrewAI documentation](https://docs.crewai.com)
