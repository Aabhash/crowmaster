
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/aabhash/crowmaster-bot/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Fleet_management welcomes more documentation, whether as part of the official fleet_management docs or in docstrings.

### Submit Feedback

The best way to send feedback is to file an issue.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

---

## Get Started!


Ready to contribute? Here's how to set up `crowmaster-bot` for local development.

1. Fork the `crowmaster-bot` repo on GitHub.
2. Clone your fork locally::

    ```$ git clone git@github.com:your_name_here/crowmaster-bot.git```

3. Install your local copy into a virtualenv. Set up your fork for local development:

    ```$ mkvirtualenv crowmaster-bot```
    
    ```$ cd crowmaster-bot/```
    
    ```$ python setup.py develop```

4. Create a branch for local development::

    ```$ git checkout -b name-of-your-bugfix-or-feature```

   Now you can make your changes locally.

5. Commit your changes and push your branch to GitHub::

    ```$ git add .```
    
    ```$ git commit -m "Your detailed description of your changes."```
    
    ```$ git push origin name-of-your-bugfix-or-feature```

7. Submit a pull request through the GitLab website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.
3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. 

Tips
----

To run a subset of tests::

```$ pytest tests.test_crowmaster-bot```
