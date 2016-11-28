Title: Uses
Date: 2016-11-28
Slug: uses
Description: Andrew Heiss is working on several exciting and groundbreaking projects

People often ask me what programs I use for my writing and design. In truth, my workflow tends to look like [this](https://xkcd.com/1579/) or [this](https://xkcd.com/1172/), but here's a more detailed list of all the interconnected programs I use.

I try to keep this updated fairly regularly. As of November 28, 2016 this is what I'm using:

# Writing

- I permanently ditched Word as a writing environment in 2008 after starting grad school. I do all my writing in [pandoc-flavored](http://pandoc.org/) [Markdown](https://daringfireball.net/projects/markdown/) (including e-mails and paper-and-pencil writing)—it's incredibly intuitive, imminently readable, flexible, future proof, and lets me ignore formatting and focus on content.
- After years of using [WriteRoom](http://www.hogbaysoftware.com/products/writeroom), then [Byword](https://bywordapp.com/), I have recently settled on [Ulysses](http://ulyssesapp.com/) (in part because of recent [glowing reviews](https://brooksreview.net/2016/01/ulysses-all-the-things/)). I write pretty much everything in Ulysses now. At first I chafed at the fact that it stores everything in its own internal folder structure, since I store most of my writing in git repositories, but exporting a compiled Markdown file from a bunch of Ulysses sheets is trivial (and still easily trackable in version control).
- Ulysses has decent HTML previewing powers, but when I need more editorial tools, I use [Marked](http://marked2app.com/).
- The key to my whole writing workflow is the magical [pandoc](http://pandoc.org/), which converts Markdown files into basically anything else. I use [my own variation](https://github.com/andrewheiss/Global-Pandoc-files) of Kieran Healy's [Plain Text Social Science workflow](http://plain-text.co/) to convert Markdown to HTML, PDF (through LaTeX), and Word (through LibreOffice).
- I store all my bibliographic references, books, and articles in a [BibTeX](http://www.bibtex.org/) file that I edit with [BibDesk](http://bibdesk.sourceforge.net/).
- I read and annotate all my PDFs with [Skim](http://skim-app.sourceforge.net/) (and [iAnnotate](http://www.iannotate.com/) on iOS), since both export annotations as clean plain text.
- I store all my notes in [OneNote](https://www.onenote.com/) (I ditched Evernote after 7 years(!) because of their [new prices and policies](https://blog.evernote.com/blog/2016/06/28/changes-to-evernotes-pricing-plans/)).

# Development

## Science and research

- I post almost everything I write or develop on [GitHub](https://github.com/andrewheiss).
- I use [R](https://www.r-project.org/) and [RStudio](https://www.rstudio.com/) for most of my statistical computing, and I'm a dedicated devotee of the [hadleyverse](http://adolfoalvarez.cl/the-hitchhikers-guide-to-the-hadleyverse/) (especially [ggplot2](http://ggplot2.org/) and [dplyr](https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html)). I sometimes use [knitr](http://yihui.name/knitr/) and [RMarkdown](http://rmarkdown.rstudio.com/), but I generally just export figures and tables from R and reference them in my writing rather than making full-blown literate documents.
- I also use [Python](https://www.python.org/) ([3!](http://www.onthelambda.com/2014/05/13/damn-the-torpedoes-full-speed-ahead-making-the-switch-to-python-3/)) pretty regularly, especially for natural language processing (with [nltk](http://www.nltk.org/)) and web scraping (with [Requests](http://docs.python-requests.org/en/master/) + [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)). Every few months I play with pandas and numpy and Jupyter, but I'm far more comfortable with R for scientific computing.
- I use RStudio for editing R files, but I use [Sublime Text 3](https://sublimetext.com/3) for everything else.

## Web

- I run my main web server on a [DigitalOcean](https://www.digitalocean.com/) droplet, and [I spin up temporary droplets all the time](https://github.com/andrewheiss/cloud-config-files) to offload scraping scripts, complicated R models, and to create on-the-fly VPNs.
- I normally access my remote files through SSH in a terminal, but for more complicated things, I've found that [Mountain Duck](https://mountainduck.io/) is indispensable.
- My website uses [Pelican](http://blog.getpelican.com/).
- I use [Let's Encrypt](https://letsencrypt.org/) for SSL.

## Miscellaneous

- I use a[ system-wide hotkey](https://www.iterm2.com/features.html#hotkey-window) (``ctrl + ` ``) to open [iTerm2](https://www.iterm2.com/) from anywhere.
- I use [Homebrew](http://brew.sh/) to install Unix-y programs.
- I'm partial to both [Hack](https://sourcefoundry.org/hack/) and [Consolas](https://en.wikipedia.org/wiki/Consolas) for my monospaced fonts.


# Desktop apps

## Graphic design

- Though I regularly use LaTeX (through pandoc), I adore [InDesign CC](https://www.adobe.com/products/indesign.html) and use it to make fancier academic and policy documents. I also used it for [all the typesetting I did](https://github.com/andrewheiss/maxwell-institute-typesetting/blob/master/books-i-made.md) for [BYU's Neal A. Maxwell Institute](http://mi.byu.edu/).
- I use [Illustrator CC](https://www.adobe.com/products/illustrator.html) all the time to enhance graphics I make in R and to make non-data-driven figures and diagrams.
- I use [Lightroom](https://www.adobe.com/products/photoshop-lightroom.html) and [Photoshop](https://www.adobe.com/products/photoshop.html) too, but less often nowadays.
- Despite my dislike for Word and Excel, I use PowerPoint for all my presentations. It's not my favorite, but in the apocryphal words of Churchill, "PowerPoint is the worst form of slide editor, except for all the others."

## Productivity

- My secret for avoiding the siren call of the internet is [Freedom](https://freedom.to/). I have two blocklists: (1) *antisocial*, which blocks Facebook and Twitter, and (2) *nuclear*, which blocks everything. I generally turn on my antisocial blocklist for 4+ hours and write/develop away. I also use [Focus](http://www.focusapp.io/ "http://www.focusapp.io") to follow a kind of pomodoro schedule, but I sometimes miss notifications to take breaks.
- I was an early convert to [Todo.txt](http://todotxt.com/) and used it for years until my tasks and projects got too unwieldy. I switched to [Taskpaper](https://www.taskpaper.com/) for a while before recently settling on [2Do](http://www.2doapp.com/) (due to [incredibly](https://www.macstories.net/stories/why-2do-is-my-new-favorite-ios-task-manager/) [positive](https://brooksreview.net/2016/01/2do/) reviews), and I'm in love.
- [Fantastical 2](https://flexibits.com/fantastical)’s natural language input is a glorious thing.
- I keep a log of what I work on (and occasionally do more traditional diary-like entries) with [Day One 2](http://dayoneapp.com/) on both iOS and OS X.
- I use [TextExpander](https://smilesoftware.com/textexpander) to replace and expand a ton of snippets, and I use [Keyboard Maestro](https://www.keyboardmaestro.com/main/) to run dozens of little scripts that help control my computer with the keyboard.
- I used to use [Geektool](http://projects.tynsoe.org/en/geektool/) to show weather, iTunes track information, and my todo lists on my desktop, but I recently switched to [Übersicht](http://tracesof.net/uebersicht/) and it's fantastic.
- I use [Dropbox](https://www.dropbox.com) religiously and use [Crashplan](https://www.code42.com/crashplan/) to back up all the computers in our house to the cloud.
- With all these little helper apps, I use [Bartender](https://www.macbartender.com/) to keep my menubar clean.

# Hardware

- I use an early 2013 13″ MacBook Pro Retina, iPad Mini 2, and iPhone SE.
