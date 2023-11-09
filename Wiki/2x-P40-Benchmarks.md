# Llama 2 - Nouse Hermes GGUF
This is using Llama 2 Nous Hermes GGUF with the llama.cpp loader. **For the 70b test scenarios, I used the nous-hermes-llama2-70b.Q4_K_M.gguf version!** If I just auto downloaded the 70b version from [here](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-70B-GGUF), it would try to auto load the Q5_0 version which would be too close to the VRAM limit and cause errors and crashes. The 13b model and 7b model, I just let the llama.cpp auto load whichever it chose since there was plenty of VRAM for those. Additionally, I maxed the gpu layers settings and split the tensors 24,24 between the 2X P40's.

## Scenario Types
**First** - This means I ran the prompt for the first time. This will also incur a significantly higher evaluation time as the LLM will need to 

**Cache** - This means I ran the prompt with no changes again in instruct mode. This will cache the prompt evaluation that was done previously which takes the prompt evaluation out of the calculations. This will result in a faster TPS overall when the prompt is cached.

| Scenario | Model | Context | Tokens/s | Sample TPS | Prompt Eval TPS | Eval TPS |
|----------|-------|---------|----------|------------|-----------------|----------|
| First    | 13b   | Empty   | 18.28    | 978.74     |-----------------| 30.67 |
| Cache    | 13b   | Empty   | 21.23    | 1086.48    |-----------------| 30.57 |
| First    | 13b   | 250     | 16.58    | 941.63     | 437.06          | 29.17 |
| Cache    | 13b   | 250     | 17.73    | 840.84     |-----------------| 28.47 |
| First    | 13b   | 500     | 15.51    | 1257.55    | 431.48          | 27.53 |
| Cache    | 13b   | 500     | 18.97    | 934.64     |-----------------| 27.04 |
| First    | 13b   | 1,000   | 14.22    | 1710.57    | 428.55          | 25.07 |
| Cache    | 13b   | 1,000   | 17.84    | 1194.65    |-----------------| 24.37 |
