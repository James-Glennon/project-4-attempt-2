# Code Institute Portfolio Project 4: Second Attempt

*This a second attempt at the portfolio 4 project using a template as the original had poor UX

The original attempt repository is availible on [GitHub](https://github.com/James-Glennon/Portfolio-project-4)

# Portfolio Project 4: Full-stack development

Author: *James Glennon*

---
## About

The aim of this project is to create all aspects of a website for a restaurant/ diner which allows a customer to place a booking/ reservation.

### Design Thinking

This project will be designed primarily based on the experiences of the main personas I expect to interact with such a site/ booking system;

- The customer

- The restaurant staff

---
#### The Customer

The customer(s) I am primarily concerned with are;

- New customers who are not yet familiar with the restaurant.

- Returning customers who wish to make a booking.

The concerns I have identified for the new customer are;

- confirming the location / name of the restaurant.

- learning about the atmosphere, opening hours, and menu of the restaurant.

- being able to make a booking. *Required project objective*

For returning customers;

- being able to make a booking. *Required project objective*

- being able to navigate past unnecessary/ repeat info.

- being able to contact the restaurant for complaints/ feedback.
---
#### The Restaurant Staff

The restaurant staff I am primarily concered with are;

- The on-shift restaurant staff who will interact directly with customers.

- Managerial staff who will adjust staff hours based on the number of bookings.

The concerns I have identified for the on-shift staff;

- viewing bookings in an immediate and managable format (e.g only show today's/tomorrow's)

- to link bookings with customers (either with a name or a phone-number)

- to add/remove/alter bookings.

- ease of use. (It should be easier that making reservations on paper) *Main concern*

for Managerial staff;

- To see all recorded bookings in one place.

- To see who is working that day (outside project scope)
---

## Credit / References

### Media / UX

Main header image from [secretdublin.com](https://secretdublin.com/most-beautiful-restaurants/)
*[Image location](https://offloadmedia.feverup.com/secretdublin.com/wp-content/uploads/2022/02/28053553/49741353_2225002007716056_2774068992225050624_n.png)*

Dublin at night image from [IrishCentral.com](https://www.irishcentral.com/travel/travel-tips/what-to-do-winters-evening-dublin)
*[Image Location](https://www.irishcentral.com/uploads/article/117387/cropped_Dublin_City_Night_iStock.JPG?t=1667554775)*

Fine food image from [finefoodspecialist.co.uk](https://www.finefoodspecialist.co.uk/)
*[Image Location](https://www.finefoodspecialist.co.uk/media/homeimages/wagyu_steak_level_1_.jpg)*

Romantic diners image from [Clayton Hotel ballsbridge](https://www.claytonhotelballsbridge.com/blog/fine-dining-in-dublin/)
*[Image Location](https://www.claytonhotelballsbridge.com/wp-content/uploads/sites/8/2019/07/couple-enjoying-romantic-dinner-restaurant-1024x680.jpg)*

UX theme created by [Start Bootstrap](https://startbootstrap.com/previews/one-page-wonder)

favicon taken from [Icons8](https://icons8.com/icon/111450/dining-room)

---

### Code

HTML coded using [Bootstrap](https://getbootstrap.com/)

Website was built closely following instructions provided in the flask and database management lessons provided by Code Institute, taught by Tim Nelson

The following form was taken directly from one lesson and used in this project.



    <div class="row">
		<div class="col-lg-8 col-md-10 mx-auto">
			<p>Want to get in touch? Fill out the form below to send me a message and I will get back to you as soon as
                possible!</p>
			<form method="POST" name="sentMessage" id="contactForm" novalidate>
				<div class="control-group">
					<div class="form-group floating-label-form-group controls">
						<label>Name</label>
						<input type="text" class="form-control" placeholder="Name" name="name" id="name" required data-validation-required-message="Please enter your name.">
						<p class="help-block text-danger"></p>
					</div>
				</div>
				<div class="control-group">
					<div class="form-group floating-label-form-group controls">
						<label>Email Address</label>
						<input type="email" class="form-control" placeholder="Email Address" name="email" id="email" required data-validation-required-message="Please enter your email address.">
						<p class="help-block text-danger"></p>
					</div>
				</div>
				<div class="control-group">
					<div class="form-group col-xs-12 floating-label-form-group controls">
						<label>Phone Number</label>
						<input type="tel" class="form-control" placeholder="Phone Number" name="phone" id="phone" required data-validation-required-message="Please enter your phone number.">
						<p class="help-block text-danger"></p>
					</div>
				</div>
				<div class="control-group">
					<div class="form-group floating-label-form-group controls">
						<label>Message</label>
						<textarea rows="5" class="form-control" placeholder="Message" name="message" id="message" required data-validation-required-message="Please enter a message."></textarea>
						<p class="help-block text-danger"></p>
					</div>
				</div>
				<br>
				<div id="success"></div>
				<div class="form-group">
					<button type="submit" class="btn btn-primary" id="sendMessageButton">Send</button>
				</div>
			</form>
		</div>
