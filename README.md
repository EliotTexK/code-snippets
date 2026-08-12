# The Absolute State of Cooding

"AI can write code for you, so there's no need to write anything from scratch. I am very smart."

-- CEO of some startup in the mid to late 2020s, (on the website X, formerly known as Twitter)

"Oh my god guys, cooders are sooooo cooooked!"

-- Bot reply to CEO

Let me transport you back in time. Way back in time to the long-lost era of 2021.

Back before chatbots. Back when all code was artisinally hand-crafted. Back when the programmer commanded the computer hardware DIRECTLY!!!

By directly, I don't mean COMPLETELY directly, of course. Let's be reasonable.

I mean, it's not like we had to BUILD the hardware.

And, we also didn't have to create BINARIES by hand. I mean, come on. We had assemblers.

Okay, and it's not like we had to create a different binary for each computer architecture. We had operating systems and compilers and interpreters.

And it's also not like we had to create control flow and memory management abstractions ourselves. We had `if`, `for`, and ownership semantics.

And nobody would have expected us not to reuse other people's code, which was specifically designed for reuse. Libraries, people!

And actually even if other people's code wasn't meant for reuse, we would still probably copy/paste from StackOverflow.

Yes, back then, programmers were independent craftsmen. Realizing all of our software from first principles!

Which is why it's such a shame that we've been obsoleted. Why write code **from scratch** when I can just start up an AGENTIC LOOP and...

(10 minutes and $150 worth of tokens later, $75 of which I paid for, $75 of which VC money paid for)

Wait what the hell is this shit?!? I just wanted you to graph some data in matplotlib! Why did you write 1000 lines of python code?

More importantly, why did it take 10 minutes? Wait a second!

In the time it took me to WRITE THE PROMPT necessary for you to perform the task (and write it unambiguously enough that you wouldn't fuck it up, since english is not a context-free language),
I could have just copy/pasted somebody else's code, and tweaked a few lines so that it fit my use case!

**Hell, I could have just copy/pasted MY OWN CODE!!!**

# Code Snippets

In a way, an LLM searches for information which has been lossily compressed, with context serving to index and iteratively narrow down what was requested.

Under this model, RLHF endows search with a "usefulness" heuristic, and the original uncompressed info is the training corpus.

Even if this is not exactly how an LLM works, this is often how we use it for programming. "Find me some StackOverflow-style code for this one thing."

I say we cut out the middleman when we can. Have a sort of caching layer between us and the LLM. There's code we've all written or searched for a dozen times before.

Snippets and ripgrep, my friends... Snippets and ripgrep. Fuzzy find also.

Integrate it into your workflow. Put it on a hotkey. Have your IDE integrate it into its own "snippets" system.

Why compose a whole prompt then wait for inference when a few keystrokes will do?

And I know that Google Search AI is pretty good for this use case, but it ain't tailored to you specifically

Only YOU know exactly how you would describe a piece of code

And only YOU know the ideal code format YOU would want
(You could reformat AI code but that's less convenient than having exactly what you want in "one shot")

And also you might want to avoid AI use for ethical reasons...

# How to Organize

Use keywords in the snippets themselves, so that when you ripgrep/fzf through them, it's easier to find what you need

This may work better than having non-overlapping categories (directories) for narrowing down search

Hey, maybe you can even get some kind of really fast custom LLM to search your snippets for you.
But this would only make sense if it takes less time/cognitive load to prompt it than to do fzf/rg keyword search.
