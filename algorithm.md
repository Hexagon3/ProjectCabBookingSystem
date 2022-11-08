# Algorithm 


### Basic requirments 
```
class PassengerRequirements {
	initial:cordinate,
	final:cordinate,
	journey_time:time,
}

class Driver {
	availabel_seat:int,
	total_seat:int,
	current:cordinate,
}

AvailableDriverList = [d_1, d_2, ... , d_m]
PassengerRequirementsList = [pr_1, pr_2, .... , pr_n]

function distance(cordinate1,cordinate1){ 
	return by road shortest route distance in km or m.
}

sequence_distance([ ... cordinateList ]){
	dist = 0;
	route = []
	for i 0 to length_of_cordinateList - 2 :
		dist+= distance(length_of_cordinateList[i],length_of_cordinateList[i+1])
	route = on road shortest route by visiting the coordinates of list

    return route, dist
}

```
