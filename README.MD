# Real Estate Management Site
A simple web app for real estate managers to list, showcase, and manage their property listings. Originally built for one of my past clients. It has these features:
- Display all listings.
- Search functionality for listings. Search by Address, Price range, Bed count, and more.
- Administration panel for creating new listings, updating existing listings, or deleting listings.

Other than that, we have some standard Contact, Help, Testimonials and FAQs sections and pages.

All in all, a pretty simple project.

There is a live demo hosted at: [Link](https://kaj-management.herokuapp.com/)

## Limitations of Heroku
For those of you who have experience with Heroku, you know that it has an ephemeral filesystem and inevitably, the images stored on the Live Demo will be deleted. So this is really only for testing the app out. 

For using it properly, you would need to deploy it on a real server. Or you could configure Django to use a different storage system, like Amazon S3 or something.
