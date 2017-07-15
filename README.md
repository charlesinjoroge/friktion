# friktion
Friktion application

Any questions or design decisions that's important for all of us to know, we can put here so they're easily seen without having to constantly question each other about them.

There's an `install.sh` as a basic script for getting whatever dependencies we add. It's nothing complicated right now, and will be really unhelpful if one of the install fails, but better than nothing.

## Twitter API
- We can currently get a list of trending topics worldwide
  - we could change this to be more regional if we want or mix between the two
    - Ex. 50% worldwide, 50% USA or something like that 
  - The [topics we get](https://github.com/cnjoroge/friktion/pull/1) aren't always the best for fostering discussion, but hey, it's a start
- Trying to figure out if we can filter out tweets related to certain topics...
- Need to find a good way with dealing with non-ASCII characters