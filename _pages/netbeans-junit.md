---
layout: default
permalink: /NetBeans/JUnit
title: "CS173: Intro to Computer Science - Unit Testing with the NetBeans Software Environment"
excerpt: "CS173: Intro to Computer Science - Unit Testing with the NetBeans Software Environment"
    
---
# {{ page.title }}

This guide has been adapted from [Professor Tralie](https://www.ursinus.edu/live/profiles/4502-christopher-tralie).

## Unit Testing

Let's say we want to test the code method we provided in the [introduction](.) article with [JUnit](https://netbeans.org/kb/docs/java/junit-intro.html).   You can follow the instructions in [that article](.) to open the sample project in NetBeans.  Then, right click on the class file, then choose `Tools -> Create/Update tests`

![]({{ site.baseurl }}/images/netbeans/CreateUpdateTests.png)

Then, check/uncheck the following boxes

![]({{ site.baseurl }}/images/netbeans/TestOptions.png)

This will create a new file for testing with an example test method for each method you created in your original class. You should be careful to comment out or delete the `fail` line at the end of the test, and be sure that your inputs and expected outputs are the expected behavior of your method. Once you've done this, you can right click on this file and click `run`, and the results of the test will be shown in a window:

![]({{ site.baseurl }}/images/netbeans/RunTests.png)

If you are interested in trying this test case out for yourself, here is the code from the screenshot above.  This test case asks if 1 is an even number, and should pass because it expects that the function will return  `false`.

```java
public class NewClassTest {
	public NewClassTest() {
	}

	@Test
	public void testIsEven() {
		System.out.println("isEven");
		int num = 1;
		boolean expResult = false;
		boolean result = NewClass.isEven(num);
		assertEquals(result, expResult);
		//fail("The test case failed");
	}
}
```