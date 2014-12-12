Title: MPA Dashboard
Date: 2011-09-17
Category: Web Design
Template: design_project
Slug: other-projects/mpa-dashboard
Thumb: http://www.andrewheiss.com/files/images/design/mpadash-thumb.png
Full: http://www.andrewheiss.com/files/images/design/mpadash-full.png
link: http://andrewheiss.com/mpadash/


* Drupal-based digital signage
* No manual updating required

This dashboard runs on a Mac Mini connected to a large plasma screen in the BYU MPA lounge. It pulls in information from different iCal calendars and RSS feeds and displays at-a-glance information about upcoming internships and jobs, Marriott School events, activities, conferences, student and faculty birthdays, and class deadlines.

Because the dashboard pulls information from other websites and services, it requires almost no maintenance. It's magic. :)

I based the design loosely on [Panic's incredible status board](http://www.panic.com/blog/2010/03/the-panic-status-board/). It runs on Drupal 6 with a bunch of modules that make the magic work. I use [Feeds](http://drupal.org/project/feeds) to aggregate and parse the RSS and iCal feeds, [Views](http://drupal.org/project/views) to filter and display the content in individual blocks, and [Views Slideshow](http://drupal.org/project/views_slideshow) to loop through all the different blocks and regions. 
