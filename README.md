#About Phrasenoia

Phrasenoia is based on the ideas behind [diceware](http://world.std.com/~reinhold/diceware.html), and as such uses the diceware word list by default.

Other word lists can be used.

This package was developed specifically for Linux and OS X.
Portability patches for other *nixes are welcome.

##Entropy

This package treats gathering entropy very conservatively. In order to collect a uniform distribution of random numbers we do two things:
1. use /dev/random by default. On Linux systems, this is a much better source of entropy than /dev/urandom. This is also why I do not use the python random module for word selection.
2. After random number collection, if the random number falls outside the range we need, we discard the number instead of scaling it and creating a non-uniform distribution.

If you have low entropy on your Linux system, you may want to consider  Haveged: http://www.issihosts.com/haveged/