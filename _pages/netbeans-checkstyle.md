---
layout: default
permalink: /NetBeans/CheckStyle
title: "CS173: Intro to Computer Science - NetBeans CheckStyle Plugin"
excerpt: "CS173: Intro to Computer Science - NetBeans CheckStyle Plugin"
    
---
# {{ page.title }}

This guide has been adapted from [Professor Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-tralie).

## Writing with Good Coding Style with Help from the CheckStyle NetBeans Plugin

Significant emphasis is placed upon [good coding style]({{ site.baseurl }}/Style-Guide) as we introduce the fundamental concepts of software development.  This is because it is so important to be able to read others' code easily.  Following a few guidelines will help all of us to write  consistent code in a way that does not hide the details of your approach in obscurity.  Even I must admit to forgetting the rationale behind complex code that I had written only a few weeks prior!  Had I followed these guidelines more closely, I would have saved so much time in the long run by not having to re-read, re-understand, and, sometimes, re-write my old code.  

There is an added challenge in learning to code while simultaneously learning to code well, but practicing good habits is the key to learning those good habits.  To help you do this, there is a [plugin for NetBeans](http://plugins.netbeans.org/plugin/3413/checkstyle-beans) called [CheckStyle](https://www.sickboy.cz/checkstyle/).  The plugin will flag some common poor code styles just like it flags syntax errors and unused variables, to help you optimize your style as you write and to catch potential issues before you forget how your code works (this really does happen!).

You can direct NetBeans to automatically download this plugin.  In NetBeans, go to `Tools->Plugins` and click the `Settings` tab

![]({{ site.baseurl }}/images/netbeans/netbeanspluginsettings.png)

Click `Add` to provide NetBeans with the URL of the plugin repository which houses our plugins, and paste the following repository URL: `http://www.sickboy.cz/checkstyle/autoupdate/autoupdate-3.xml`.  By installing the plugin directly through NetBeans using a plugin repository, updates to the plugin will be detected and automatically downloaded by NetBeans over time.

Now, you can actually select the plugins from this repository.  To do this, go to `Tools->Plugins` again, and go to the `Available Plugins` tab

![]({{ site.baseurl }}/images/netbeans/netbeansaddplugins.png)

Check the two plugins `Checkstyle Beans Library` and `Checkstyle Beans Plugin`, and then click `Install`.  You may need to read and accept a licence agreement or other confirmation prompts to install.

Now CheckStyle should be installed.  One final step remains: to configure CheckStyle with the types of code style rules that should be checked.  CheckStyle is a nice tool for allowing teams to write consistent code together according to best practices, and also to standards (for example, Google has their own custom set of rules to ensure that everyone writes their code in the same style, even beyond best practices).  A configuration file is used to specify these rules.  We have created a style file that you can use that includes many of the [Style Guide]({{ site.baseurl }}/Style-Guide) rules, without adding too many additional rules that would be overly pedantic.  

You can download our configuration file [here]({{ site.baseurl }}/files/checkstyle.xml).  You can save this file by right-clicking on the link and clicking "Save As".  To add our CheckStyle configuration file to the plugin, go to `Tools->Options` and then the `Miscellaneous` tab.  You will see a tab below this called `CheckStyle`.  Click `Browse` next to the `Configuration File` box, and select the file you just downloaded (it is likely in your "Downloads" folder by default, which is fine!).
