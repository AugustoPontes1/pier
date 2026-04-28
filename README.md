# pier

Pier is a [Harbor](https://www.harborframework.com/docs/tasks)-compatible framework for evaluating coding agents in sandboxed environments. It reads Harbor's task format and runs trials against it.

```bash
pier run -p path/to/task --agent claude-code --env modal
```

## Why pier

Pier is a fork. We wanted a smaller, more opinionated base to build on, starting with one thing Harbor couldn't do: run installed agents (Claude Code, Codex, etc.) in air-gapped tasks (`allow_internet = false`).

When the agent runs *inside* the sandbox, both the install step and the inference call need the network. Pier fixes that by letting agents declare their install scripts and a network allowlist, which environments then honor when setting up the sandbox.

More is planned from here, and pier will keep drifting from Harbor as we go.

## What works today

- **Task format:** Harbor-compatible.
- **Environments:** `docker`, `modal`.
- **Agents:** `nop`, `oracle`, `claude-code`, `codex`, `gemini-cli`, `opencode`, `mini-swe-agent`.

If your tasks allow internet, or your agent runs outside the sandbox, Harbor is the broader, more mature choice and you should probably use it.

## Install

```bash
uv tool install pier
# or
pip install pier
```

## Run

```bash
export ANTHROPIC_API_KEY=...
pier run -p path/to/task --agent claude-code --env modal --env-file .env
```

See `pier run --help` and `pier job --help` for everything else. Trials land under `jobs/<timestamp>/<trial_id>/`.
