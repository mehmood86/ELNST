---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Home
---

<h1> Instructions to run tests </h1>

---
**NOTE**

These instructions are for Linux based distribution such as Ubuntu.

It is assumed that the selenium is already installed on your local machine see [installation](https://selenium-python.readthedocs.io/installation.html){:target="_blank"} guide



---

Clone ELNST repository from Github
{% highlight shell %}
git clone https://github.com/mehmood86/ELNST
{% endhighlight %}

Install a virtual environment to keep installation in isolation
{% highlight shell %}
python3 -m pip install --user --upgrade pip virtualenv
{% endhighlight %}

Now, go to ELNST directory and activate virtual environment and install required libraries
{% highlight shell %}
cd ELNST 
python3 -m venv env 
source env/bin/activate 
python3 -m pip install -r requirements.txt 
{% endhighlight %}

Finally, run tests by specifying environment variable $URL and path to test file
{% highlight shell %}
URL="http://localhost:4000/home"
SELENIUMTESTS="seleniumTests/Tests"

echo "1- running userManagement.py " 
URL=$URL python3 $SELENIUMTESTS/userManagement.py

{% endhighlight %}
You can also run specific test from each testclass

{% highlight shell %}
URL="http://localhost:4000/home"
SELENIUMTESTS="seleniumTests/Tests"

echo "1- running userManagement.py " 
URL=$URL python3 $SELENIUMTESTS/userManagement.py LoginTest.test_dataset_upload

{% endhighlight %}