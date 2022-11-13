# Working Structure & Planning

## Interface ( Frontend ):
1. Passenger
2. CarDriver 
3. Admin 
Single App for Two interface driver and Passenger.
Admin will login through web

## **Sign up & Register Page**(As Driver or as a passenger) or **Login**
* **For Passenger** <br>
  1. Name
  2. Father's and Mother's name
  3. Date of birth
  4. Present address
  5. Aadher details etc....
  6. Uploade 1.Profile Photo; 2.Aadher Card; 3.Birth cirtificate; 4.Voter card;....
* **For Driver** <br>
  1. Own Details (Same as Passenger register page)
  2. Car Details
### Passenger Interface Component 
* **Login**(With name & password)
* **Home / Instant Booking Page** <br>
  1. Navbar ->{ Navigation Menu Box, Profile}
  2. Navigation Menu Box -> { Inbox, ..., Settings}
  3. bottom Bar -> {List View, Map View}
  4. Content-> Two types 1. map based  2. Text Based
* **Scheduled Booking Page**
* **Booking History Page**
### CarDriver Interface Component 
* **Login**(With name and password)
* **Home / List of passenger request page** <br>
  1. Navbar ->{ Navigation Menu Box, Profile}
  2. Navigation Menu Box -> { Inbox, Show Car details, ..., Settings}
  3. bottom Bar -> {List View, Map View}
  4. Content-> Two types 1. map based  2. Text Based
* **Travel History**(Total km, Placess)
* **Total profit**

## Modules 
1. Passenger Interface (Frontend) --> react native
2. CarDriver Interface (Frontend) --> react native
3. Admin Interface (Frontend) --> django (now default)
4. Passenger API --> Django restframework
5. CarDriver API --> Django restframework
6. Decision_system (Suggestion)--> Algorithm 
7. Admin 

## Working Method
1. Passenger will send **requerments request**
2. Requests are compairing and best n requests will be provided to CarDrivers
3. CarDrivers will chose to accept Passengers and send the request 
4. According to coice of CarDrivers Passenger can see available Car 
5. Passenger will decide for which Cardriver he/she will go.





