import java.util.Arrays;

public class Person {
	
	// reasonable distances to move in 5 minutes on foot
	public static final double AVG_X_SPEED = 0.002274;
	public static final double AVG_Y_SPEED = 0.003889;
	
	// location
	public double lat;
	public double lon;
	
	// velocity
	public double xVelocity;
	public double yVelocity;
	
	// destination
	public Location destination;
	
	// how many cycles will the person spend at the given destination
	public int cyclesToSpend;
	public int cyclesSpent;
	
	// initialize person in random point on map
	public Person(){
		lat = Map.randomLat();
		lon = Map.randomLon();
		changeDestination("00_00_0000_00_00");
	}
	
	public void move(String currentTime) {
		calculateVelocity();
		lat = lat + yVelocity;
		lon = lon + xVelocity;
		if(yVelocity == 0 && xVelocity == 0) {
			cyclesSpent++;
		}
		if(cyclesSpent >= cyclesToSpend) {
			changeDestination(currentTime);
			cyclesSpent = 0;
		}
	}
	
	public void changeDestination(String currentTime) {
		// if it is dinner time 
		int hour = Time.getHour(currentTime); 
		int chance = Map.rando.nextInt(2);
		if(hour == Time.LUNCH_HOUR || hour == Time.DINNER_HOUR || hour == Time.BREAKFAST_HOUR) {
			if(chance == 1) {
				this.destination = Map.randomLocation();
				this.cyclesToSpend = destination.cycles + Map.rando.nextInt(4);
			}
		} else {
			// if it isn't meal time randomly hang around 
			this.destination = new Location("", Map.randomLat(), Map.randomLon(), 0);
			this.cyclesToSpend = Map.rando.nextInt(2);
		}
//		System.out.println("hour == breakfast? " + (hour == Time.LUNCH_HOUR || hour == Time.DINNER_HOUR || hour == Time.BREAKFAST_HOUR));
//		System.out.println("destination = " + destination.name + " " +
//				destination.lat + ", " + destination.lon);
	}
	
	public void calculateVelocity() {
		double yDistance = destination.lat - this.lat;
		double xDistance = destination.lon - this.lon;
		if(yDistance > 0) {
			yVelocity = AVG_Y_SPEED;
			if(lat + yVelocity > destination.lat) {
				yVelocity = yDistance;
			}
		} else {
			yVelocity = -AVG_Y_SPEED;	
			if(lat + yVelocity < destination.lat) {
				yVelocity = yDistance;
			}
		}

		if(xDistance > 0) {
			xVelocity = AVG_X_SPEED;
			if(lon + xVelocity > destination.lon) {
				xVelocity = xDistance;
			}
		} else {
			xVelocity = -AVG_X_SPEED;
			if(lon + xVelocity < destination.lon) {
				xVelocity = xDistance;
			}
		}
	}
	
	public static void main(String args[]) {
		Person p = new Person();
//		System.out.println("person at " + p.lat + ", " + p.lon);
		p.move("10_01_2017_07_40");
		p.move("10_01_2017_07_45");
		p.move("10_01_2017_07_50");
		p.move("10_01_2017_07_55");
		p.move("10_01_2017_08_00");
		p.move("10_01_2017_08_05");
		p.move("10_01_2017_08_10");
		p.move("10_01_2017_08_15");
		p.move("10_01_2017_08_20");
//		System.out.println("person at " + p.lat + ", " + p.lon);
	}
}
