# Llama 2 - Nouse Hermes GGUF
This is using Llama 2 Nous Hermes GGUF with the llama.cpp loader. **For the 70b test scenarios, I used the nous-hermes-llama2-70b.Q4_K_M.gguf version!** If I just auto downloaded the 70b version from [here](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-70B-GGUF), it would try to auto load the Q5_0 version which would be too close to the VRAM limit and cause errors and crashes. The 13b model and 7b model, I just let the llama.cpp auto load whichever it chose since there was plenty of VRAM for those. Additionally, I maxed the gpu layers settings and split the tensors 24,24 between the 2X P40's.

### Scenario Types
**First** - This means I ran the prompt for the first time. This will also incur a significantly higher evaluation time as the LLM will need to 

**Cache** - This means I ran the prompt with no changes again in instruct mode. This will cache the prompt evaluation that was done previously which takes the prompt evaluation out of the calculations. This will result in a faster TPS overall when the prompt is cached.

### Context Meaning
The contexts of 250, 500, 1k, 2k, 3k, and 4k are not the exact numbers, but just the ballpark of what I was aiming for. Here's the correlated numbers if you wish to see the details in complete accuracy. Also when I give the context to actual token count, I'm putting that context into Open Ai's tokenizer to get the actual token count from it.

**Empty** - Means I had nothing in the context at all. This'll cause the fastest generation.

**250** - is exactly 250 in context @ 219 tokens

**500** - is 496 context @ 440 tokens

**1k** - is 1009 context @ 886 tokens

**2k** - is 2031 context @ 1734 tokens

**3k** - is 3068 context @ 2620 tokens

**4k** - is 4094 context @ 3498 tokens

## Benchmarks

| Scenario | Model | Context | Tokens/s | Sample TPS | Prompt Eval TPS | Eval TPS |
|----------|-------|---------|----------|------------|-----------------|----------|
| First    | 7b   | Empty   |  32.68   |  1328.72    |-----------------| 46.01 |
| Cache    | 7b   | Empty   | 33.01    | 1353.31    |-----------------| 45.86 |
| First    | 7b   | 250     | 21.65    | 1105.18     | 704.79          | 42.95 |
| Cache    | 7b   | 250     | 25.67    | 1460.93     |-----------------| 43.14 |
| First    | 7b   | 500     | 22.51    | 1042.15    | 685.93          | 40.73 |
| Cache    | 7b   | 500     | 28.51    | 1116.50     |-----------------| 40.93 |
| First    | 7b   | 1k      | 24.73    | 1601.33    | 690.03          | 36.82 |
| Cache    | 7b   | 1k      | 25.52    | 1295.59    |-----------------| 35.32 |
| First    | 7b   | 2k      | 20.33     | 1370.96    | 653.66          | 30.75 |
| Cache    | 7b   | 2k      | 23.37    | 1114.11     |-----------------| 30.34 |
| First    | 7b   | 3k      | 14.69     | 1774.00    | 528.50          | 27.01 |
| Cache    | 7b   | 3k      | 20.70    | 1173.04     |-----------------| 26.13 |
| First    | 7b   | 4k      | 10.25     | 1389.56      | 650.51           | 23.65 |
| Cache    | 7b   | 4k      | 18.83    | 1465.68      |-----------------| 23.55 |
| First    | 13b   | Empty   | 18.28    | 978.74     |-----------------| 30.67 |
| Cache    | 13b   | Empty   | 21.23    | 1086.48    |-----------------| 30.57 |
| First    | 13b   | 250     | 16.58    | 941.63     | 437.06          | 29.17 |
| Cache    | 13b   | 250     | 17.73    | 840.84     |-----------------| 28.47 |
| First    | 13b   | 500     | 15.51    | 1257.55    | 431.48          | 27.53 |
| Cache    | 13b   | 500     | 18.97    | 934.64     |-----------------| 27.04 |
| First    | 13b   | 1k      | 14.22    | 1710.57    | 428.55          | 25.07 |
| Cache    | 13b   | 1k      | 17.84    | 1194.65    |-----------------| 24.37 |
| First    | 13b   | 2k      | 9.99     | 1718.57    | 398.84          | 20.65 |
| Cache    | 13b   | 2k      | 15.19    | 945.12     |-----------------| 20.38 |
| First    | 13b   | 3k      | 8.72     | 1777.84    | 332.48          | 17.94 |
| Cache    | 13b   | 3k      | 13.15    | 1003.43    |-----------------| 17.4 |
| First    | 13b   | 4k      | 4.49     | 1248.8     | 393.6           | 15.71 |
| Cache    | 13b   | 4k      | 11.06    | 1195.7     |-----------------| 15.61 |
| First    | 70b   | Empty   | 7.08     | 1267.90     |-----------------| 8.08 |
| Cache    | 70b   | Empty   | 7.41     | 1456.45     |-----------------| 8.14 |
| First    | 70b   | 250     | 5.85     | 1070.11     |  111.67         | 7.83 |
| Cache    | 70b   | 250     | 6.66    | 1133.77     |-----------------| 7.83 |
| First    | 70b   | 500     | 5.04    | 1576.71     | 112.47          | 7.64 |
| Cache    | 70b   | 500     | 6.68    | 1564.42     |-----------------| 7.63 |
| First    | 70b   | 1k      | 4.42    | 1213.99     | 105.24          | 7.05 |
| Cache    | 70b   | 1k      | 6.24    | 1629.41     |-----------------| 7.13 |
| First    | 70b   | 2k      | 4.00     | 1614.98    | 117.06          | 6.28 |
| Cache    | 70b   | 2k      | 5.63    | 1428.57     |-----------------| 6.31 |
| First    | 70b   | 3k      | 4.03     | 1498.1     | 107.83          | 5.60 |
| Cache    | 70b   | 3k      | 5.04    | 1331.67     |-----------------| 5.61 |
| First    | 70b   | 4k      | 2.85     | 1596.34    | 108.05           | 5.71 |
| Cache    | 70b   | 4k      | 5.40    | 1764.06     |-----------------| 5.65 |
