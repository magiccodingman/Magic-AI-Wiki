# Llama 2 - Nouse Hermes GGUF

## Scenario Types
**First** - This means I ran the prompt for the first time. This will also incur a significantly higher evaluation time as the LLM will need to 
**Cache** - This means I ran the prompt with no changes again in instruct mode. This will cache the prompt evaluation that was done previously which takes the prompt evaluation out of the calculations. This will result in a faster TPS overall when the prompt is cached.

| Scenario | Model | Context | Tokens/s | Sample TPS | Prompt Eval TPS | Eval TPS |
|----------|-------|---------|----------|------------|-----------------|----------|
| First    | 13b   | Empty   | 18.28    | 978.74     |-----------------| 30.67 |
| Cache    | 13b   | Empty   | 21.23    | 1086.48    |-----------------| 30.57 |
