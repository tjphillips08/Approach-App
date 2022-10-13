# Approach

![Logo](https://i.imgur.com/HYfU6bpm.png)

## App Description:

 Approach is your one stop shop to finding another golfers in your area to play a round with. Have you or a friend ever wanted to go play golf and have no one to play with? It can be intimidating and anxiety ridden to go to a course for the first time and play by yourself. With Approach you are able to find other members of your golf course and even join a cllub where you and fellow amateurs can go try and pretend to know what you're doing on the golf course. It's a lot easier to perform "under par" with people in your group. 
 
 ## User Story:
 
 Welcome to Approach! When you first come to our app make sure to sign up for an account. Once your account is created, feel free to browse through all the local courses or search by your city, state or zipcode to see courses in your area. Once you find the course you are interested in, check out their website and get a feel for pricing, course rules and difficulty level. Also, you can see who are members of this course and maybe ones that would like to show you around and play a round together. After you've found your course, check out the different clubs. You and every other user of Approach have the ability to create your own club or join anothers. Once in the club you can message other members and set up the next tee time to go play!
 
 
 ## Wireframes:
 
 ## Home Page
![Screen Shot 2022-10-07 at 8 40 39 AM](https://user-images.githubusercontent.com/109078858/194567953-d485c0cb-add4-476e-82ef-e62c65650d27.png)


 
 This is how the homepage will look when you visit our website. You will see our nav bar, where you can navigate to the courses, clubs and sign up or login to your account. Also, you will notice the tour schedules for both the PGA and LPGA tours, so you can keep up with the next tournament. Who knows there might be one in your area.
 
 ## Courses
![Screen Shot 2022-10-07 at 8 40 55 AM](https://user-images.githubusercontent.com/109078858/194568034-1009caf2-268a-4c29-8684-442fe1666e43.png)

 
 When you navigate to our courses page, here is what you'll see. You will see all the courses listed below and can search by city, state, zipcode or name to find the courses in your area. 
 
 ## Course Details
![Screen Shot 2022-10-07 at 8 41 17 AM](https://user-images.githubusercontent.com/109078858/194568118-ba8b5781-828d-4e67-8dbc-9b3df2a2cad9.png)

 
 When you find that course you want more information about, just click on the picture of the course. This will pull up a detail page with the course name, address and a link to the course website. Feel free to look at their website for pricing and more detailed information about the course. 
 
 ## Clubs
 ![Screen Shot 2022-10-07 at 8 41 28 AM](https://user-images.githubusercontent.com/109078858/194568194-9a52c505-cb83-4e4a-bad9-8ebe18fe48fb.png)

 
 When you navigate to the clubs, you will be brought to this page of all clubs. Here you will see a full list of all the user created clubs. You will be able to see which course the club is tied too, so you can join a club that matches your interest. You also can create your own club!
 
 ## Course Details
 ![Screen Shot 2022-10-07 at 8 41 41 AM](https://user-images.githubusercontent.com/109078858/194568264-3e44008a-84d4-4f98-a39b-b67a42bff9dd.png)

 
 When you click onto the club, you will be brought to this page. This will show you all the members in the club and their contact information. This way you can see if this is a club you want to join . Don't forget to sign up as a member of your selected course. 
 
 
 ## ERD
 ![Screen Shot 2022-10-07 at 8 48 14 AM](https://user-images.githubusercontent.com/109078858/194568964-c2c1162f-428e-4d97-8678-8f5ed6ef76a5.png)
 
 For this application I am using three Data Models. As you can see from the ERD our three models consist of Course, Member and Club. There is a 1:M relationship between courses and their members, while there is a M-M relationship between the members and the clubs they are choosing.
 
 ## Technologies Used
 ![django-python-logo](https://user-images.githubusercontent.com/109078858/194570662-fb591432-26bc-45aa-ad59-f97415eb08f3.png)
 ![PostgreSQL-Logo](https://user-images.githubusercontent.com/109078858/194571618-6469808c-6b01-4ec3-b2ca-a3ed0e3699ed.png)


This application was built using a python/django full-stack. I used Python to implement all the functionality of the application, such as looping through content for display. Django was used heavily in this application to create my authorization for the application. Databases were created with PSQL to help build more dynamic relational database implementation. I used Summernote to change Admin forms that would help filter comments and posts for easy moderation. Also, utilized crispy forms to change and adapt my comment form for users. 


## Challenging Code

![Screen Shot 2022-10-13 at 9 57 06 AM](https://user-images.githubusercontent.com/109078858/195632507-83f18645-808d-4612-af46-c99bba9c8933.png)

This code was made in my Admin.py file. This is what I created to give my admin forms more functionality. I wanted to be able to moderate the comments that went through my site and creating a action field on my admin comments form, allowed me to moderate these comments. Also, I incorporated slugs into my post admin form to allow a dynamic url to each post based on the title of the post. Finally, I set up filters on these forms, so I would be able to easily navigate the comments by day, created-on and most recent to streamline the moderation portion of my website.



## API
https://developer.sportradar.com/docs/read/golf/Golf_v2#tournament-schedule
Sport Radar was used in this application to display tour schedules for both the PGA and LPGA tours on the homepage. There is a lot of functionality with this API that can be further implemented. 

## Stretch Goals
Updated at later date


 
 
 
