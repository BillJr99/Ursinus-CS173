---
layout: default
permalink: /NetBeans/Troubleshooting
title: "CS173: Intro to Computer Science - NetBeans Software Environment"

    
---
# {{ page.title }}

# Troubleshooting

## Java JRE Moved After Upgrading to Mac OS Big Sur
Run the following command to find the current JRE installation:
```
java -version
```

This will provide a directory such as `/Library/Java/JavaVirtualMachines/jdk-11.0.7.jdk/Contents/Home`.  Copy this, and we will paste it into the NetBeans configuration file shortly.  To do this, edit the following file:

```
vim /Applications/NetBeans/Apache\ NetBeans\ 12.1.app/Contents/Resources/NetBeans/netbeans/etc/netbeans.conf
```

and update the line that says `netbeans_jdkhome` to the following (note that the comment character `#` has been removed, if present):

```
netbeans_jdkhome="YOUR-JRE-DIRECTORY-HERE"
```

Save and exit, and re-start NetBeans.

## Directory Permissions After Upgrading to Mac OS Big Sur
On some computers, opening, importing, saving, or exporting a project or library fails to access certain user directories like `Desktop` or `Downloads`.  Under the user directory, there is a directory called `NetBeansProjects` that can be accessed by NetBeans.  Using the filesystem or Finder, files in directories like `Downloads` can be moved to the `NetBeansProjects` directory prior to using them in NetBeans.  Alternatively, one can use [System Settings](https://macperformanceguide.com/blog/2020/20200119_1427-macOS-Catalina-add-java-fullDiskAccess.html), "Full Disk Access," and add NetBeans (under Applications) and Java (under Library - JavaVirtualMachines).

## Unit Tests
**Note**: You may need to replace your import lines, if you see the word `jupiter` in them.  You can specify `JUnit 4` in the `Create/Update Tests` window when you create your tests (it's ok to re-create them if needed), and then delete the imports in your test file and replace them with these instead, if so:

```java
import org.junit.Test;
import static org.junit.Assert.*;
```

# Apporto
The NetBeans IDE software is also installed on Apporto, which can be reached from the cloud.  Here are [instructions](https://www.ursinus.edu/live/files/3550-apporto-instructionspdf) on how to access the software through Apporto.

# Microsoft Teams Permissions

To screen-share Netbeans (or other software) on Microsoft Teams, the following permissions are required under "Security and Privacy" - "Accessibility" (add Microsoft Teams):

<iframe width="560" height="315" src="https://www.youtube.com/embed/Phit7ZOvtiw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
