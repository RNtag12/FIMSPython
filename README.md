<h1>Fruit Inventory Management System with Pandas and Json</h1>

<h2> Project Description</h2>
The Fruit Inventory Management System is a Python-based program created primarily for managing and tracking fruit goods in a shop. 
This robust system offers a number of capabilities for both administrators and users, including the ability to show product information, add new
items, update current products, delete products, generate purchase reports, and manage user-
specific data.
<br />


<h2>Libraries and modules</h2>

- <b>Pandas</b> 
- <b>Json</b>
- <b>os.path</b> 
- <b>time</b>
- <b>random</b> 


<h2>IDE  </h2>

- <b>Spider Anaconda </b>

<h2>Program steps:</h2>

<p>
  
- <b> The code begins with the appropriate
import lines to include the essential libraries for data processing and file handling, such as
pandas and json</b> 
  
- <b> Import modules such as os.path, time, and random for further functionality</b>

- <b> A dictionary named "available_products"; is constructed to contain
the initial fruit data. Each fruit is represented by a unique product ID, and its data such as name,
price, origin, quantity, and date are saved as dictionary values</b>

- <b> The json.dumps() function is used
to convert the dictionary to JSON format, and the resultant JSON string is saved to a file named
"data.json" for database storage</b>

- <b> The code then specifies two primary functions: &quot;admin()&quot; and
"user()". The "admin()" function handles administrative activities, whereas the "user()" function
handles user-specific functions.</b>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
