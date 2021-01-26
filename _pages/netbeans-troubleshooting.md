---
layout: default
permalink: /NetBeans/Troubleshooting
title: "CS173: Intro to Computer Science - NetBeans Software Environment"
excerpt: "CS173: Intro to Computer Science - NetBeans Software Environment"
    
---
# {{ page.title }}

# Troubleshooting

## Java JDK Failure After Upgrading to Mac OS Big Sur
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
netbeans_jdkhome="YOUR-JRE-DIRECTORY-JERE"
```

Save and exit, and re-start NetBeans.

## Directory Permissions After Upgrading to Mac OS Big Sur
On some computers, opening, importing, saving, or exporting a project or library fails to access certain user directories like `Desktop` or `Downloads`.  Under the user directory, there is a directory called `NetBeansProjects` that can be accessed by NetBeans.  Using the filesystem or Finder, files in directories like `Downloads` can be moved to the `NetBeansProjects` directory prior to using them in NetBeans.

# Apporto
The NetBeans IDE software is also installed on Apporto, which can be reached from the cloud.  Here are [instructions](https://www.ursinus.edu/live/files/3550-apporto-instructionspdf) on how to access the software through Apporto.