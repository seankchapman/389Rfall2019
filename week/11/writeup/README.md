# Writeup 1 - Web I

Name: Sean Chapman
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sean Chapman


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

This website is vulnerable to SQL injection attacks. When selecting a product, the backend of the site runs a query that probably looks something like `SELECT * FROM PRODUCTS WHERE ID='...'.` This means that if we pass in a query that is always true, we will be able to view all entries in the products table. I was able to find this out by clicking on one of the products, which took me to a link like `http://142.93.136.81:5000/item?id=1`. I decided to change the value of `id` to a query that is always true, in this case I  used `id='|| '1'='1'-- -;`. When the website ran this query it spat out all the products in the products table, allowing me to see the flag, which is `CMSC389R-{y0u_ar3_th3_SQ1_ninj@}`.

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

- Level 1: I was able to execute the attack by running the query `<script>alert("pwned")</script>`. 
- Level 2: In this level, I tried to execute the attack the same way as in level 1, but the website defended against `<script>` tags. Instead, I created an anchor tag, that executes javascript when clicked. The attack I executed was `<a href='javascript:alert("pwned")'>click me</a>`. This produced a message that contained a link with the text `click me`. Clicking on the link executed the javascript.
- Level 3: For this level, we had to inject our code in the URL of the website. The website was taking the name of the image to load, and passing it into an `<img src=''/>` tag, after appending `.jpg` onto the end of the input. In order to execute the attack, we had to make our input fit into the code such that it produced valid HTML. Our input closes the img tag, opens an `svg/onload` tag with the alert() command in it, closes this tag, and opens a new img tag without closing it. The input looks like this: `1.jpg'/><svg/onload='alert("test")'/><img src='2`.
- Level 4: To execute this attack, I had to use the input `');alert('`. Essentially what's happening here is the `');` at the beginning of the input ends the onload function. We can then add `alert('` to add the alert. We do not inlude the `');` at the end of the alert statement because it is already included in the context of the program.
- Level 5: The attack here can be executed on the signup page. In the URL of this page, we see `next=confirm`. This means that the value `confirm` is being passed into the href tag for the link. Changing this  to `next=javascript:alert()` will open the alert() popup when we click on the `Next` link.
- Level 6: The XSS attack can be executed by changing the value after the # to `HTTPS://www.google.com/jsapi?callback=alert`.

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.