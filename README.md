# SpecServ

## Intention
These scripts (will) provide custom services for InspIRCd. The aim it to be lightweight, modular, and extremely easy to
work with, i.e., extremely easy to write new modules for.

Using and debugging this generally requires a good understanding on the InspIRCd s2s protocol, which is very poorly
documented unluckily. However, since this program should provide raw output from the server link, we could learn how it
works just by taking a look at the standard output. If I have enough time, which sadly I don't, I might also take a
look at the [Atheme Services](https://atheme.github.io) protocol codes and learn from there. However, for most people's
purposes, I believe that reading the output is enough.

I originally worked out a very disgustingly-coded version, [ULined](https://github.com/andrewrunxiyu/ulined). I used a
`config.py` and imported it as a configuration, and every plugin imported, rather than inheriting it / passing it from
the main program. This is one of the things that make the whole program's architecture extremely disgusting. It also
used plain `socket`s rather than `asyncio` or `trio`, I did not use `threading` either, which makes the server time out
from the network very often when I use time-consuming commands. This implementation tries to address
these problems.

Some of this is inspired by [FigServ](https://gitlab.com/xeroxIRC/FigServ) developed by `bigfoot`/`bigfoot547` (which
is now deprecated on xeroxIRC unluckily). Code from [miniirc](https://github.com/luk3yx/miniirc) by `luk3yx` is
directly used, including but not limited to the function that parses commands, namely, converting stuff like `:908
FJOIN #test 1625126809 + :qo,908AAAAAL` into a nice little tuple as follows:
```python
result = ('FJOIN',
 '908',
 {},
 ['#test', '1625126809', '+', ':qo,908AAAAAL'])
```
To explain, `FJOIN` is of course the command; `908` is the sender of the command, which is a server ID,
the empty dictionary usually holds ircv3 tags, and the list holds the arguments.

At the first time of writing this document, I didn't really come up with *any* actual code yet; they are all
imaginations. I learned from my awful experience developing ULined, and I believe that I should learn a bit more about
object-oriented programming and python mappings, i.e., dictionaries, first. I'll be so glad if anyone would help!

## Contact
- [Contact Andrew on IRC by connecting to his own (testing) network on TLS port 6697 of irc.andrewyu.org](ircs://irc.andrewyu.org:6697)
- [Contact Andrew on xeroxIRC located at TLS port 6697 of xeroxirc.net](ircs://xeroxirc.net:6697)
- [Contact AndrewYu on LiberaChat](ircs://irc.libera.chat:6697)
- [Email andrew@andrewyu.org](mailto:andrew@andrewyu.org)
