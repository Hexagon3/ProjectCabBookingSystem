# Algorithm 


### Basic requirments 
```
class PassengerRequirements {
	is_shared: Boolean,
	car_detail:{
	  no_seat:int,
	  model:string,
	  is_ac: boolean
	}
	initial:cordinate,
	final:cordinate,
	schedule_time:time,
}

class Driver {
	is_shared:boolean,
	availabel_seat:int,
	total_seat:int,
	current:cordinate,
	estimated_free_time:time
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
