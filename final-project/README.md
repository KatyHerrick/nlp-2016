# The Comical Commit Classifier

### Introduction
Commit Logs From Last Night (http://www.commitlogsfromlastnight.com/) is an external project that aggregates self-deprecating and/or frustrated commit messages for humorous effect. It seems to do a simple search for keywords (usually curse words) to mark a commit message as good material for the website, but we want to take the method a step further and implement a program that takes commit logs from different repos on GitHub to identify whether the contents are “funny” or “serious” based on more complex criteria. We found a good model online of the implementation of a program that identifies “positive” and “negative” tweets, which we can modify for our own needs. We think the commit logs from GitHub will provide us a challenge, given its lack of proper sentence structure, coding-specific language, and repo-specific language. We have already found a few repositories that we can use as development corpuses, and then we can expand to larger ones for further testing.

### Files
1. raw_log_processor.py --> Given an unaltered file of logs (git log > repo_name_raw_logs.txt), will strip out all commit, author, and dates.
2. manual_annotator.py --> Given a processed file of logs (i.e. that only contains commit messages separated by a newline character), allows the user to manually mark each message as "funny" or "serious" in order to create an answer key for the classifier.
3. naive_classifier.py --> Uses nltk's NaiveBayesClassifier to classify a list of commits. Takes in a processed file of logs (i.e. that only contains commit messages separated by a newline character) and outputs a list of tuples of the form:
``` python
[(“commit message”, “funny”), (“commit message 2”, “serious"), …]
```
4. commit_classifier.py --> Our customized classifier that we tweak to give better results than the NaiveBayesClassifier. TBD if this is possible to do within our time frame.
5. scoring.py --> Given an answer key and the output from one of our classifiers, calculates the accuracy of the classifier.