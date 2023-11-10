# Warning
I'm very proud of what this server has accomplished, but that also doesn't mean it's perfect. The suggested server is a datacenter level server, which means it wasn't meant to be in your house! Please be mindful of the following warnings and precautions about the server before you make the decision to build/buy anything similar.

## Sound
The following table will help you relate the decibel levels I'm about to describe to sounds you'd be familiar with. This way you know what you're getting into when it comes to how loud this server is:

| Decibel Level (dB) | Comparable Sound                |
|--------------------|---------------------------------|
| 0                  | Threshold of hearing            |
| 10                 | Breathing                       |
| 20                 | Whisper, rustling leaves        |
| 30                 | Quiet rural area                |
| 40                 | Library, bird calls             |
| 50                 | Moderate rainfall               |
| 60                 | Normal conversation             |
| 70                 | Vacuum cleaner                  |
| 80                 | Heavy city traffic              |
| 90                 | Lawnmower                       |
| 100                | Motorcycle                      |
| 110                | Rock concert, chainsaw          |
| 120                | Thunderclap, sirens             |
| 130                | Jet takeoff (100 meters away)   |
| 140                | Fireworks, gunshot              |
| 150                | Balloon pop                     |
| 160                | Shotgun firing                  |

## This is not a quiet server by default!
I provide a quickly made python script within the guide that'll help control the sound levels of the R730 server. Because by default, the server does not recognize the Tesla P40 GPU's and will max out the fans to keep everything very cool. This is ridiculously loud and not really acceptable for most homes unless you're stickingn this server in a garage or shed where the sound can't bother anyone.

**My Personal Decibel Level Readings**

The following is my personal tests with a decibel reader. I walked quite close to the server and would go as far as a couple feet away from the server to get a broad range of the sound

| Decibel Level (dB) | Fan %     | Scenario            | Notes |
| 55 - 65            | 30% - 40% | Idle / low load     | ----- |
| 70 - 75            | 70% - 80% | Running 70b LLM     | Would spike to 80% rarely and for a short period of time |
| 73 - 78            | 80%       | Generating 40 cat images on Stable Diffusion     | Would hover 70% to 80% at first, but after 28 cat images, it stayed at 80% until all cats were generated  |
