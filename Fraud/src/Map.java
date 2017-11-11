import java.io.PrintWriter;
import java.util.Random;

public class Map {
	public static final double MAXLAT = 34.106891;
	public static final double MINLAT = 34.099606;
	public static final double MAXLON = -117.703131;
	public static final double MINLON = -117.714892;
	
	public static Random rando = new Random();	
	
	public static double randomLat() {
		return MINLAT + (MAXLAT - MINLAT) * rando.nextDouble();
	}
	
	public static double randomLon() {
		return MINLON + (MAXLON - MINLON) * rando.nextDouble();
	}
	
	
	public static Location[] locations = {
		new Location("Frary", 34.100443, -117.710929, 5),
//		new Location("Rains", 34.099063, -117.711581, 5),
		new Location("Frank", 34.096107, -117.711508, 5),
		new Location("Oldenborg", 34.097131, -117.711818, 6),
		new Location("Collins", 34.101542, -117.709005, 7),
		new Location("Malott", 34.102835, -117.710565, 5),
		new Location("Hoch-Shanahan", 34.105763, -117.709846, 4),
		new Location("McConnell", 34.102840, -117.705536, 5),
	};
	
//	0.000200;
	
	public static Location randomLocation() {
		return locations[rando.nextInt(locations.length)];
	}
		
	
	// for testing
	public static void main(String[] args) {
		String data = "latitude,longitude\n";
		for(int i = 0; i < 9; i++) {
			data = data + Map.randomLat() + "," + Map.randomLon() + "\n";
		}
		data = data + Map.randomLat() + "," + Map.randomLon();
		System.out.print(data);
		
		try(PrintWriter out = new PrintWriter("C:/Users/sarp/Desktop/test.csv")) {
		    out.println( data );
		} catch(Exception e) {
			System.out.println(e);
		}
	}
	
}
