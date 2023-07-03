Making a journal of Renpy Tricks I find.

Why a separate document of tricks?
  I've trolled and explored through a number of Renpy forums. And, perhaps unfairly generalizing, it feels like, if you want to do something, and there isn't a specific Renpy section on how to do it, a healthy chunk of Renpy users will tell you that what you want to do is impossible.

  Maybe sometimes they're correct. But, sometimes there's a workaround! Or a method! Worst-case, these tricks will help me so I don't have to figure it out all over again. Best-case, someone who isn't me is reading this and it will help you!

Trick #1:
  Jump straight to ending.
    So, let's say you've done what I've done in this game. And made a point-and-click adventure where we pause the action for player input. BUT, in order to end the game, you need to hit the return at the top of your Renpy stack.

    Maybe you've coded the whole thing and you feel like your return should go all the way to the top. And it doesn't? WTF.

    No stress. We can just add a flag called gameOver. Set it to False.

    Then, when your player hits an ending condition, good or bad, set the flag to True.

    THEN, add at the top of your MyRoom function, an if statement. If gameOver then return. Boom! You now have the option to end your game at virtually any point in the stack!
