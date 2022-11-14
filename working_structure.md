# Working Structure & Planning

## Interface ( Frontend ):
1. Passenger
2. CarDriver 
3. Admin 
Single App for Two interface driver and Passenger.
Admin will login through web

## Sign up & Register Page
* **Sign Up as a user**
  1. User Name
  2. Set Password
  3. Email id
  4. Phone Number(Calling number)
* **Registration Page For Driver**
  0. Inherit From User
  1. Name
  2. Date of birth
  3. Aadher Number
  4. Address 
  5. Car type(no of seat)
  5. Car Details
  6. License No
  7. Driving Experience 
  8. Docuiment Uploade 1.Profile Photo; 2.Aadher Card; 3.Licence certificate
### Passenger Interface Component 
* **Login**(With name & password)
  1. User Name
  2. Password
* **Home / Instant Booking Page** <br>
  1. Navbar ->{ Navigation Menu Box, Profile}
  2. Navigation Menu Box         
      *  Order History 
      *  Profile
      *  Schedule
      *  Inbox   
      *  Settings 
  3. bottom Bar -> {List View, Map View}
  4. Content-> Two types 1. map based  2. Text Based
* **Profile Page**
* **Scheduled Booking Page**
* **Booking History Page**
### CarDriver Interface Component 
* **Login**(With name and password)
  1. User Name
  2. Password
* **Home / List of passenger request page** <br>
  1. Navbar ->{ Navigation Menu Box, Profile}
  2. Navigation Menu Box         
      *  Work History 
      *  Profile
      *  Inbox 
      *  About Car 
      *  Settings 
  3. bottom Bar -> {List View, Map View}
  4. Content-> Two types 1. map based  2. Text Based
* **Profile Page**
* **Travel History**(Total km, Placess)
* **Total profit**(Today, Last Month, Last year)

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





