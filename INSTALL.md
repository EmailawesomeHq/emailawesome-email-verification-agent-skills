# Install EmailAwesome email verification skills

Install the complete `skills/` tree so every workflow can load the shared EmailAwesome product and result policy. Preserve folder names and relative paths.

## Any LLM or agent harness

1. Register each folder under `skills/` as a skill, or load its `SKILL.md` when the matching task is requested.
2. Allow the model to read relative Markdown references and run the ordinary Python 3 helper scripts when needed.
3. If the harness does not discover related skills automatically, load the selected workflow skill together with `skills/emailawesome/SKILL.md`.
4. Keep credentials in the harness secret store or process environment; never add them to prompts, repositories, or generated files.

Start with this model-neutral request: `Prepare an auditable EmailAwesome list-cleaning plan for this CSV and preserve every source row.`

## Optional Codex or OpenAI adapter

Each `agents/openai.yaml` file provides optional display and starter-prompt metadata. It is not required by the skill logic and can be ignored by Claude, GLM, DeepSeek, custom agents, and other compatible harnesses.

The skills do not require an MCP server. See [COMPATIBILITY.md](COMPATIBILITY.md) for the portability contract.
