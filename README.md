# Magic-AI-Wiki

The following is a wiki on building a 48 GB VRAM AI server for at home home lab enthusiasts. This was created based on my personal experience building such a server and what I learned. I made alterations based on community feedback as well. But the pricing and build was created in late 2023, in which the prices are no longer the same. But it's still achievable and I believe this wiki still serves great use, is very informative, but in my opinion. 

[wiki pages](https://github.com/magiccodingman/Magic-AI-Wiki/tree/main/Wiki)

[Main Build Guide](https://github.com/magiccodingman/Magic-AI-Wiki/blob/main/Wiki/Budget-AI-Workstation-Build.md)

[Recorded Sound Levels](https://github.com/magiccodingman/Magic-AI-Wiki/blob/main/Wiki/R730-Build-Sound-Warnnings.md)

[Helpful TPS chart](https://github.com/magiccodingman/Magic-AI-Wiki/blob/main/Wiki/TPS-Chart.md)

[Dell Server Fan Control](https://github.com/magiccodingman/Magic-AI-Wiki/blob/main/Scripts/Dell-Server-Fan-Control.py)

If you're utilizing Proxmox with PCI passthrough for your build. A note since 2025, the proxmox kernel version of 6.14 broke PCI passthrough with the Tesla P40's. If you install and pin version `6.8.12-15-pve` it'll work again.

Also please note that P40 maintenance is supported until July 2026. Be aware of future drivers and compatibility beyond that date. Though I do believe it's better to look at different GPU's moving forward.
