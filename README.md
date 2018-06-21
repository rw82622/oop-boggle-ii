# Boggle Challenge Part 2: Word Checker

## Summary

We are going to build off our last Boggle challenge by using our `BoggleBoard` generator to check the existence of a word against our generated boggle board.

The only rule is that the same dice cannot be reused in the same word. For example, if the word is "apple", you cannot use a die that landed as "P" twice. Instead the "P" must be on the board twice.

We are going to implement a `BoggleBoard#include?` method:

```python
board.include("apple") # => true or false, depending
```
**Note**: This method shouldn't care whether the word is **actually** a word in the dictionary.

### Step 1: Pseudocode

Stop! I know what you're about to do. I've done it many times before. You're about to jump in to writing code.

![Admiral Ackbar from star wars saying its a trap](http://i.imgur.com/LaJ9Kmo.gif)

Instead, get out some paper and draw out a 4x4 Boggle Board. Fill it with letters (perhaps utilizing your brand-spanking new generator). Pick a gibberish word (makes it easier to check letter by letter) and check if it's on the board.

Reflect on your mental process. How did you do decide if the word was on the board or not?

For our first iteration, let's try the most basic way to verify a word in a continuous line. i.e. vertically, horizontally, and diagonally.

Write your pseudocode for the algorithm.

**NOTE**: Only words with 3 letters or more count.

### Step 2: Implement "BoggleBoard#include?"

It's time to translate your pseudocode to python.

What, if any, instance methods do you need to define? Would your algorithm be easier to write if your board were stored in a different way?

What are the tradeoffs between storing the board as a 4x4 array of arrays vs. a single 16 element array?


## Resources

* [Boggle on Wikipedia](http://en.wikipedia.org/wiki/Boggle)
* [Play Boggle online](http://www.wordplays.com/boggle)
