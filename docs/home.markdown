---
layout: page
title: List of testCases
permalink: /home/
---

<h2>User Management TestCases</h2>

|# |name |description |
|:-----|:----|:------------|
|1 |Create new user|Create new user with following default standard credentials|
|2 |Login validation by return key|Login with newly created user via return key|
|3 |Login validation by button click|Login with newly created user via button click key|


<h2>TopFrame Interaction TestCases</h2>

|# |name |description |
|:-----|:----|:------------|
|1 |About click|Login as person and navigate to ‘About’ page and compare version of ELN with 1.1.0 (current chemotion ELN version is 1.0.3)|
|2 |Sign up click |Click on ‘sign up’ link and check if the ‘back’ link correctly redirected to home page|
|3 |Sign up user |Sign up a new User, wait for the page to load completely. Click logout and then click back link to check if session is expired correctly|
|4 |ELN click |Without login, click on chemotion drop down and then click ELN, it should redirect to chemotion eln home page|
|5 |Edit close click |Check if the ‘close’ button in sample structure editor works properly|
|6 |Edit cancel click |Check if the ‘cancel’ button in sample structure editor works properly|
|7 |Chemotion repository click |Check if the ‘chemotion repository link’ opens correct page|
|8 |Complat click |Check if the ‘complat link’ opens correct page|
|9 |Complat on github click |Check if the ‘complat_on_github link’ opens correct page |
|10 |Login invalid user |Check if after entering invalid user credentials it redirects to chemotion login page and nowhere else |
|11 |Login valid after invalid user |Check if it logins properly after an invalid attempt |
|12 |Forgot password after invalid user|Check if it redirects to ‘chemotion home page’ properly when ‘forgot password’ is clicked and then sign up link and then finally back link is clicked |
|13 |Invalid email after forgot password after invalid user |Check if it redirects to ‘chemotion home page’ properly when after an invalid login attempt, ‘forgot password link’ is clicked and wrong email address is inserted. Finally it should return ‘Email not found’ as error message and when sign up link is clicked and then back, it should again redirect to home page|

<h2>Sample Interaction</h2>

|# |name |description |
|:-----|:----|:------------|
|1 |Sample analyses tab |Selects first sample in list and open its analyses tab|
|2 |Open spectra |Selects first sample in list and open its analyses tab. Then click spectra editor button and finally close it |
|3 |QC tab |Check if sample ‘QC & Curation’ tab is loading its content properly|
|4 |Literature tab |Check if sample ‘literature’ tab is loading its content properly|
|5 |Results tab |Check if sample ‘results’ tab is loading its content properly|
|6 |Properties tab |Check if sample ‘properties’ tab is loading its content properly|
|7 |Edit molecule |Check if ‘molecule edit’ button is loading editor properly and closes with close button|
|8 |Enter name |Check if naming a sample ([custom_name + timestamp]) is working properly|
|9 |Enter Temperature |Check if inserting boiling temperature as well as melting temperature in sample properties tab functions properly|

<h2>Collection Interaction</h2>

|# |name |description |
|:-----|:----|:------------|
|1 |Import |Check if ‘import collections’ opens and close the popup window properly|
|2 |File select |Check if the ‘import collections’ properly loading a sample collection from a folder|
|3 |Export dialog |Check if ‘export collections’ opens and close the popup window properly|
|4 |Export collection |Check if the ‘export collections’ properly exporting a sample collection|

<h2>Sample Properties</h2>

|# |name |description |
|:-----|:----|:------------|
|1 |Stereo abs value |Check if switching between ‘stereo Abs’ drrop down list items saves correctly and reflected aside chemical name (upper left) on the display|
|2 |Stereo rel value |Check if switching between ‘stereo Rel’ drrop down list items saves correctly and reflected aside chemical name (upper left) on the display|
|3 |Density |Check if changing density correctly saves when save button is clicked|
|4 |dataset upload |Check if a file (for instance demo.svg) properly uploaded in the Datasets of analysis section|
|5 |update |Check if updating details (such as name) of sample Datasets persists new changes properly|