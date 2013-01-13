---
layout: post
title: "What Python installations are scientists using?"
date: 2013-01-13 10:10
comments: true
categories:
- Python
- Distribution
---

Back in November 2012, I
[invited](https://twitter.com/astrofrog/status/269743084215103488) Python
users in science to fill out a survey to find out what Python, Numpy, and
Scipy versions they were using, and how they maintain their installation. My
motivation for this was to collect quantitative information to inform
discussions amongst developers regarding which versions to support, when those
discussions are based only on guessing and personal experience. In particular,
there has been some discussion in the [Astropy](http://www.astropy.org)
project regarding whether we should drop support for Numpy 1.4 (which
motivated this study).

In this post, I'll give an overview of the results, as well as access to the
raw data. First, I should mention that given my area of research and networks,
the only community I obtained significant data are Astronomers, so the results
I present here only include these (though I also provide the raw data for the
remaining users for anyone interested).

<!-- more -->

Before I show the results, I just want to make it clear that I am not claiming
that the results are a true sampling of Python user levels. I advertised the
poll via Twitter, a couple of Python mailing lists, and the Facebook group for
Astronomers. I delayed the announcement in each case, so that there may be
some useful information about the Python installations contained in the data
that I won't cover here. If anyone is interested about when the announcements
were made to correlate with response peaks in the data, please let me know!

With that out of the way... let's look at the results!

Overview
--------

First, some general stats - there were 313 responses in total, of which 244
were related to Astronomy (where I use the term in the broadest sense,
including solar physics, planetary science, astrophysics, and cosmology). The
responses were recorded between November 17th 2012 and December 2nd 2012 (at
which point the rate of responses had gone down to less than one a day).

Python Versions
---------------

{% img center /images/python_versions.png %}

As shown above, an overwhelming 80% of Astronomers use Python 2.7, and almost
15% use Python 2.6. Almost no-one uses Python 3.x for production work yet,
which is not surprising, given that at the time of the poll there were not
stable versions for all the crucial packages in a scientific Python stack (in
particular, Matplotlib only released their first Python 3.x compatible release
in December). It will be interesting to see how this fraction changes over the
next year (more on that in future blog posts).

Numpy Versions
--------------

{% img center /images/numpy_versions.png %}

In the above plot, *dev* includes anything that is a developer version more
recent than the 1.6.2 release (which was the latest stable release at the time
of the poll). The distribution is again significantly peaked, with almost 80%
of respondents using Numpy 1.6.x. There is more of a spread in the remaining
versions compared with the Python versions, but the vast majority of people
are using Numpy 1.5.x or more recent.

Scipy Versions
--------------

{% img center /images/scipy_versions.png %}

In the above plot, *dev* includes anything that is a developer version more
recent than the stable 0.11 release (which was the latest stable release at
the time of the poll). Unlike the Python and Numpy versions, which are almost
exclusively dominated by two versions, the Scipy versions show a larger
spread, with the most popular version, 0.10.x, representing only 45% of users.

I originally thought that Scipy released more often than Numpy, and this would
explain the difference, but it seems that both projects have been releasing at
a reasonably similar rate (see
[here](http://sourceforge.net/projects/numpy/files/NumPy/) and
[here](http://sourceforge.net/projects/scipy/files/scipy/)). Therefore, this
might be to do with package managers, or simply to the fact that Numpy is used
more often than Scipy, and users are therefore more likely to run into bugs
and update to the latest stable version? I have to admit that I would not even
be able to tell without checking what Scipy version I am using, whereas I know
I'm using Numpy 1.6.2 for production work.

Installation
------------

We now get to some very interesting statistics - how users install Python and
dependencies. While Python is awesome in many respects, installation is
probably the biggest hurdle that users have to jump to get started.

{% img center /images/install_methods.png %}

I'm not sure if anyone's quantitatively looked at this before, but this was
the first time that I really got a sense for all the different ways that one
can maintain a Python installation, and which methods are the most popular. I
should note that *Source* includes responses that indicated ``pip`` and
``easy_install``. And of course, some of these are not orthogonal, because
e.g. ``easy_install`` can be used to install additional packages not in EPD
for example. Nevertheless, we can make some interesting observations:

* If we combine the Linux Package Managers and MacPorts (one of the Mac
  Package Managers), this amounts to around 40% of installations, the single
  largest group.

* A small fraction (around 7%) have no idea how they installed Python and
  other packages, so they may run into issues when they try and upgrade in
  future. If you install Python for someone, please explain to them what you
  are doing and how they can update packages in future!

* Only a small fraction of people use the official binary installers, with
  many more people installing from source. This was surprising to me, given
  how quick/easy it is to install Python, Numpy, Scipy, and Matplotlib using
  the official installers. I think this is down to the fact that this is not a
  well-documented installation procedure, and is platform dependent.

* 'Custom' Astronomy-specific bundles (SciSoft and STScI Python) are not as
  widely used, which indicates that more effort should be put in getting
  packages in existing package managers than building new software stacks.

Summary
-------

To me, one of the most interesting results is that a large number of people
have a reasonably up-to-date installation, with Python 2.7 and Numpy 1.6.x,
and I imagine that the Python 2.7 peak is here to stay, given that the
transition to Python 3 will be slow. Supporting only Python 2.6 and above
seems like a sensible choice at this stage (and makes life easier for
developers), and given the imminent release of Numpy 1.7.0, I think that
software developers can start thinking about dropping support for Numpy 1.4 in
the near future. For Scipy, things are a little more difficult, given the
broad spread of versions, so developers should ensure that they know what
versions they are implicitly supporting, and to check what version users have
installed.

Finally, I think the most important thing for Python packages in terms of
installation is to ensure that they are included in package managers. Even if
it is easy to install packages via ``pip`` or ``easy_install`` in some cases,
putting packages in package managers ensures that users will more likely stay
up-to-date with the latest versions.

There is much more information still contained in the data (for example, some
of the above points can be correlated - do the people who do not know how they
installed Python correlate with the older versions?). For anyone who is
interested in looking at the data, I've placed the files and the scripts I
used to make the above plots in a GitHub repository
[here](https://github.com/astrofrog/python-versions-survey).

If you have any thoughts about the results, or find anything interesting in
the raw data, please leave a comment!

