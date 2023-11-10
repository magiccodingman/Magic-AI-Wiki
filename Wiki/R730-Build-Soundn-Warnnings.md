# Sound Warning (Solutions at the bottom)
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

### My Personal Decibel Level Readings**

The following is my personal tests with a decibel reader. I walked quite close to the server and would go as far as a couple feet away from the server to get a broad range of the sound

| Decibel Level (dB) | Fan %     | Scenario            | Notes |
|--------------------|-----------|---------------------|-------|
| 55 - 65            | 30% - 40% | Idle / low load     | ----- |
| 70 - 75            | 70% - 80% | Running 70b LLM     | Would spike to 80% rarely and for a short period of time |
| 73 - 78            | 80%       | Generating 40 cat images on Stable Diffusion     | Would hover 70% to 80% at first, but after 28 cat images, it stayed at 80% until all cats were generated  |


# Solutions
I've got a whole room dedicated to my servers and equipment. And anything that's louder than what I'm okay with goes to my garage. But not everyone has that luxury and I understand that. There are some solutions though. But please note I have not worked on these solutions myself, nor will I in the immediate future. But here's some solutions I would personally implement that would be effective, cheap, and easy enough.

1.) **Add active cooling to the Tesla P40 GPU's!** The major cause of the fans needing to ramp up is the Tesla P40 GPU's as they've got no cooling on them as they rely on the server fans to cool them down. There's many guides and mods you can perform and find online that'll tell you how to easily add fans to the Tesla P40 GPU's. This is most likely the easiest solution in my opinion and you'll definetly see success with any amount of determination. If you do this, just remember to adjust the python script I provide by deleting part of the script where it ramps the fans based on the GPU's. This way it only ramps the fans based on the CPU's tempuratures. This'll reduce the sound low enough for the majority of individuals. You likely could get away with 20% or even 10% fan speeds at that level (my script defaults to 30% as the lowest) as long as you gauge the temps yourself properly.

2.) **Replace the R730 Fans!** There's some really cool guides online like [this link here if you click on this text](https://www.brentozar.com/archive/2010/01/how-to-make-a-dell-poweredge-quieter/). These guides will walk you through replacing the fans inside the server with much quieter fans. This direction is a really cool option to me and I'm personally considering it myself. Maybe not the easiest or cheapest solution, but it'd be really cool to perform. But please be mindful that this direction is not plug and play! You can't just change the fans on these servers and you'll be required to do some soddering and wire splicing. Just be weary of this fact.

If anyone does either of the following above methods to quiet down their server. I'd love to have someone contact me on this repository or through any other means to give me their results and decibel readings! If yall learn something and tell me, I'd be happy to pass the knowledge along.
