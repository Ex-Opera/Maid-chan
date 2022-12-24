<h1 align="center"> ~Commands~ </h1>

<!-- ---------------------------------------------- -->
<br>

## 📝 Table of Contents

- [Home](../)
- [Pics](#pics)
- [Dice](#dice)
- [Utilities](#utilities)
- [Music](#music)

<br>

Note: The bot default prefix: ``m!``, but may vary depending on server config. Mention the bot to show bot's prefix of the server. 

---
<!-- ---------------------------------------------- -->

## Pics <a name="pics"></a>
This commands returns an embed link image to discord. <br>
- Anime <br>
The command **Anime** use **API Waifu Pics**, see [technologies used](#Technologies_Used) for more information. This command return **only images sfw**. <br>
Syntax example:
```
m!anime
``` 
You also can pass one argument for specify the anime type, syntax example:
```
m!anime waifu
```
Arguments list: waifu, neko, shinobu, megumin , bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe

<br>

- Hentai <br>
The command **Hentai** use **API Waifu Pics**, see [technologies used](#Technologies_Used) for more information. This command may be used **only nsfw chats**.<br>
Syntax example:
```
m!hentai
```
You also can pass one argument for specify the hentai type, syntax example:
```
m!hentai neko
```
Arguments list: waifu, neko, trap, blowjob

<br>

- Fox <br>
The command **Fox** use **Random Fox API**, see [technologies used](#Technologies_Used) for more information.
Syntax example:
```
m!fox
```

---
## Dice <a name="dice"></a>
- Dice <br>

This command is part of **RollDice Project**, see [technologies used](#Technologies_Used) for more information. The rolldice can roll dice at the interval that you choose, times as you want and sum bonus. And return list of rolls (with bonus if add) and total roll.<br>
Syntax example:
```
m!dice 2d30+4
``` 
"2" is amount of times the dice will be rolled, "30" is the dice side and "+4" is the bonus sum in total roll. If this command is used without a specified amount of rolls, it will just roll one time; without dice side ("30") it will return an error; without "+4" bonus, it will return without any bonus, the bonus multipliers are ``+`` ``-``, ``*`` or ``/``. <br>
Return example:
```
2d30+4
Rolls: [13, 1] Bonus: +4 -> 18
```

<br>

---
## Utilities <a name="utilities"></a>
- Say <br>
This command will return that you tell for repeat and will delete your message. <br>
Syntax example:
```
m!say Hello, world!
```
<br>

- Math <br>
This command do math operations. <br>
Syntax example:
```
m!math (2+2)*4
```
Operations supported: ``+`` ``-``, ``*``, ``/``, ``**`` and ``sqrt``.

<br>

- Avatar <br>
This command returns a link avatar image <br>
Syntax example:
```
m!avatar @Maid-chan#0233
```
If not passing **user id** or **user name**, it will return your avatar image.

<br>

- Ping <br>
This command will return ms response.
Syntax example:
```
m!ping
```
Return example:
```
Pong! 38ms.
```

<br>

- Scene Anime Search <br>
This command will search for anime using a Scene (gif, image, vídeo). This command use **Trace.moe API**, see [technologies used](#Technologies_Used) for more information. By limitations of API file size is limited to 10MB and the recommended resolution is 640 x 360px.
Syntax example:
```
m!animesearch https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg
```
Return example:
```
Similarity: 97.35

Anilist: https://anilist.co/anime/21034
Tittle romaji: Gochuumon wa Usagi desu ka??
Tittle romaji: Is the Order a Rabbit?? Season 2
Episode: 1
Time between: 0:04:48 and 0:04:52
```

## Music <a name="music"></a>
This command play some video from Youtube in voice channel. <br>

- Join <br>
Join in voice channel you are in.
Syntax example:
```
m!join
```

<br>

- Leave <br>
Leave of voice channel.
Syntax example:
```
m!leave
```

<br>

- Stop <br>
Stop play music.
Syntax example:
```
m!stop
```

<br>

- Play <br>
Play some video passing a link.
Syntax example:
```
m!play https://www.youtube.com/watch?v=9lNZ_Rnr7Jc
```

<br>

- Pause <br>
Pause Music.
Syntax example:
```
m!pause
```

<br>

- Resume <br>
Resume Music.
Syntax example:
```
m!resume
```
