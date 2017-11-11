
public class Location {
	
	public double lat;
	public double lon;
	public String name;
	public int cycles;
	
	public Location(String name, double lat, double lon, int cycles) {
		this.name = name;
		this.lat = lat;
		this.lon = lon;
		this.cycles = cycles;
	}	
}
