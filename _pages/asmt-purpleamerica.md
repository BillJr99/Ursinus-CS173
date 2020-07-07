---
layout: default
permalink: /Assignments/PurpleAmerica
title: "CS173: Intro to Computer Science - Purple America"
excerpt: "CS173: Intro to Computer Science - Purple America"

info:
  coursenum: CS173
  
---
# {{ page.title }}

## The Assignment (100 Points)

In the United States, many elections, including the presidential election, are decided by a "winner-take-all" system via a "first-past-the-post" model.  In this model, people in a region cast votes for their candidate of choice among a set of candidates.  Whichever candidate receives the plurality of votes cast "wins" the election.  In American presidential elections, winning a particular region results in receiving a number of "Electoral College" votes; in many states, all of the electoral college votes are cast for the candidate who won the "first-past-the-post" vote in that state.

This results in an electoral map like the one below from the 2008 United States presidential election, in which information is lost pertaining to the margin of victory.  For example, it is known that President Obama won the Commonwealth of Pennsylvania in 2008 (due to the blue color), receiving its 21 electoral college votes; similarly, it is known that Senator McCain won the state of Texas (due to the red color) and received its 34 electoral college votes.  It is not known from this visualization, however, whether these states were won by a single vote or by a landslide.  For this reason, it is important to carefully choose visualizations that convey as much information as possible, and to be clear about the limitations of the visualization.

![2008 Presidential Election Electoral College Votes from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/ElectoralCollege2008.svg/800px-ElectoralCollege2008.svg.png)

A gradient can be seen when the margin of victory is depicted on a similar map through the use of color shading, as in the figure below (from [270towin.com](http://270towin.com)).  Whereas the map above draws each region in either red or blue to indicate the winner, Vanderplei renders the map with a mixture of colors to indicate the proportion of votes received for each candidate in that region.  

![2008 Presidental Election Electoral College Votes with Margin of Victory Shading from 270towin](https://www.270towin.com/historical-presidential-elections/timeline/margin-of-victory/maps/2008_mov.png)

Robert Vanderplei proposed a [Purple America](https://en.wikipedia.org/wiki/Purple_America) map that visualizes the margin of victory with a gradient of colors.  In the example below, he draws each region at a county-by-county level instead of a state-by-state level, to depict a more granular gradient.

![County by County Election Results on a Purple America Map from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/8/8c/ElectionMapPurpleCounty.png)

Kevin Wayne developed a [SIGCSE Nifty Assignment](http://nifty.stanford.edu/2014/wayne-purple-america/purple-america.html) [^Wayne2014] in which you will draw this map using GPS coordinates for the regions (states or counties), and then color code those regions using electoral results.  The GPS coordinates of each region and the electoral results in those regions will be given to you.
[^Wayne2014]: Nick Parlante, Julie Zelenski, Josh Hug, John Nicholson, John DeNero, Antti Laaksonen, Arto Vihavainen, Frank McCown, and Kevin Wayne. 2014. Nifty assignments. In Proceedings of the 45th ACM technical symposium on Computer science education (SIGCSE ’14). Association for Computing Machinery, New York, NY, USA, 621–622. DOI:[https://doi.org/10.1145/2538862.2538995](https://doi.org/10.1145/2538862.2538995)


### Color Coding
To create the color codings, the proportion of votes cast for each of (up to) three candidates is converted into a RGB color.  An RGB color is defined by a "tuple," or collection of values: each value in this 3-tuple represents the proportion of red, blue, and green to be mixed in to the color shown.  This is called a 3-tuple because there are three values in the tuple (the red, blue, and green proportion).

We will use 24-bit color in this example, meaning that each of the three values (red, green, and blue) in the tuple can be represented with an 8-bit value.  

````markdown
<details>
  <summary>How many different values can you represent with an 8-bit value?  In other words, how many different pure "red" colors are there?  There will be an equal number of pure "blue" and pure "green" values as well.  (Click to reveal)</summary>
  
  Since each of the 8 bits is a binary bit value (0 or 1), there are two possibilities for each of the eight bit fields.  Thus, there are $2^{8}$ different values that can be represented using an 8-bit entry, or 256 distinct shades of pure red, pure blue, or pure green.  This includes the colors black (a value of 0) and white (a value of 255).
  
</details>
````  

````markdown
<details>
  <summary>How many different values can you represent with a 24-bit value?  In other words, how many different colors can we work with in total?  (Click to reveal)</summary>
  
  There are $2^{24}$ or approximately 16 million colors that we can represent as combinations of the 256 possible red values, 256 possible blue values, and 256 possible green values.  This is the same as combining three entries of up to 256 possibilities each (the 256 reds, 256 greens, and 256 blues), or $256^{3}$.  By the law of exponents, $2^{24} = (2^{8})^{3} = 256^{3}$.
  
</details>
````  

The color wheel below from Wikipedia shows some example color mixtures.  These values are in hexadecimal, so they range from 0x00 to 0xff for decimal values 0 to 255.  Here is a [guide](https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/number-systems-introduction) from Khan Academy to number systems and converting between hexadecimal, binary, and decimal. 

![RGB Color Wheel from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Palette_of_125_main_colors_with_RGB_components_divisible_by_64.gif/800px-Palette_of_125_main_colors_with_RGB_components_divisible_by_64.gif)

### Drawing Figures

https://algs4.cs.princeton.edu/code/algs4.jar

Importing a Jar (build.gradle)
Drawing a figure
        Color color = new Color(red, green, blue);
        
        StdDraw.setPenRadius();
        StdDraw.setPenColor(color); 
        StdDraw.filledPolygon(x, y); 
Looping to draw the figure

### Reading the GPS Coordinates File

http://nifty.stanford.edu/2014/wayne-purple-america/data/USA-county.txt

    /**
     *
     * @param filePath
     * @param contents
     * @return 
     * @throws IOException
     */
    public ArrayList readFile(String filePath, ArrayList<String> contents) throws IOException {
        /* https://www.journaldev.com/709/java-read-file-line-by-line */
        BufferedReader reader;
        FileReader fileReader;
       
        fileReader = new FileReader(filePath);
        reader = new BufferedReader(fileReader);
            
        String line = reader.readLine();
            
        while(line != null) {
            contents.add(line);
            line = reader.readLine();
        }
        
        reader.close();
        
        return contents;
    }

### Storing the Values from the File for Use
Using a Dictionary/HashMap (perhaps map of maps) to store values?
Converting the GPS coordinates to a 0-1 plane ((x - min) / (max - min))
Drawing those coordinates using StdDraw

### Reading the Electoral Votes File and Generating the Color Codes
Adding color from relative counts
http://nifty.stanford.edu/2014/wayne-purple-america/purple-america-data.zip

### Only Read the File Once: Using a Cache for Better Performance
Cache the lookup?

### Extension: Rendering a Different Map
Extending with different maps and other counters?

### Extension: Rendering with a Mercatur Projection
Extending with a Mercatur Projection? https://gis.stackexchange.com/questions/298619/mercator-map-coordinates-transformation-formula
* Compute mx and my for top left and bottom right points
** a = 6378137 (equatorial radius)
** Mercator_x = a * longitude
** Mercator_y = a * ln(tan(pi / 4 + latitude / 2))
* Compute Mercator distance
** Distance_Mercator = Sqrt((Mercator_x2 - Mercator_x1) ^ 2 + (Mercator_y2 - Mercator_y1) ^ 2)
** Distance_Map = Sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)
** Scale_factor = Distance_Mercator / Distance_Map
* Compute the origin scaled point
** Mercator_x0 = a * Longitude_origin
** Mercator_y0 = a * ln(tan(pi / 4 + Latitude_origin / 2)
* Compute all point lat/long
** Latitude = 2 * atan(exp((Scale_factor * -y + Mercator_y0) / a)) - pi / 2
** Longitude = (Scale_factor * x + Mercator_x0) / a
* Now scale to 0-1

## Programming Rubric

|  | Pre-Emerging (<50%) | Beginning (50%) | Progressing (85%) | Proficient (100%) |
|-|-|-|-|-|
| Data Structures (40%) | Incorrect/non-specified data structures were implemented to solve the problem, or the data structures specified were not used successfully | Data structures are chosen appropriately, but the implementation contains fundamental departures from the definition | Data structures are chosen appropriately and implemented in a functionally reasonable way, with minor areas of correction or improvement | Data structures are chosen appropriately and implemented faithfully to a standard, a reference, or an efficient implementation |
| Algorithm Implementation (40%) | The algorithm fails on the test inputs due to major issues, or the program fails to compile and/or run | The algorithm fails on the test inputs due to one or more minor issues | The algorithm is implemented to solve the problem correctly according to given test inputs, but would fail if executed in a general case due to a minor issue or omission in the algorithm design or implementation | A reasonable algorithm is implemented to solve the problem which correctly solves the problem according to the given test inputs, and would be reasonably expected to solve the problem in the general case |
| Code Quality and Documentation (10%) | Code commenting and structure are absent, or code structure departs significantly from best practice | Code commenting and structure is limited in ways that reduce the readability of the program | Code documentation is present that re-states the explicit code definitions | Code is documented at non-trivial points in a manner that enhances the readability of the program |
| Writeup/Submission (10%) | An incomplete submission is provided | The program is submitted, but not according to the directions in one or more ways | The program is submitted according to the directions with a minor omission or correction needed | The program is submitted according to the directions, including a readme writeup describing the solution |