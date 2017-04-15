## Installation

### Basic GitHub Checkout

This will get you going with the latest version of pythondoc and make it
easy to fork and contribute any changes back upstream.

1. **Check out pythondoc where you want it installed.**
   A good place to choose is `$HOME/.pythondoc` (but you can install it somewhere else).

        $ git clone https://github.com/shared-learning/pythondoc.git ~/.pythondoc


2. **Define environment variable `PYTHONDOC_ROOT`** to point to the path where
   pyenv repo is cloned and add `$PYTHONDOC_ROOT/bin` to your `$PATH` for access
   to the `pyenv` command-line utility.

        $ echo 'export PYTHONDOC_ROOT="$HOME/.pythondoc"' >> ~/.bash_profile
        $ echo 'export PATH="$PYTHONDOC_ROOT/bin:$PATH"' >> ~/.bash_profile

    **Zsh note**: Modify your `~/.zshenv` file instead of `~/.bash_profile`.
    **Ubuntu note**: Modify your `~/.bashrc` file instead of `~/.bash_profile`.


3. **Restart your shell so the path changes take effect.**
   You can now begin using pythondoc.

        $ exec $SHELL


#### Upgrading

If you've installed pyenv using the instructions above, you can
upgrade your installation at any time using git.

To upgrade to the latest development version of pythondoc, use `git pull`:

    $ cd ~/.pythondoc
    $ git pull

To upgrade to a specific release of pyenv, check out the corresponding tag:

    $ cd ~/.pythondoc
    $ git fetch
    $ git tag
    v0.1.0
    $ git checkout v0.1.0


----


## Command Reference

See [COMMANDS.md](COMMANDS.md).