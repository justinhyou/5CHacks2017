import java.io.PrintWriter;
import java.util.ArrayList;

public class BigBrother {
	public static final int PEOPLE_NUM = 100;
	public static final String START_TIME = "10_01_2017_00_00";
	public static final String END_TIME = "11_01_2017_23_55";
	public static final String TIME_INCREMENT = "00_00_0000_00_05";

	public String currentTime;
	
	private ArrayList<Person> people = new ArrayList<Person>();
	
	public BigBrother() {
		currentTime = START_TIME;
		for(int i = 0; i < PEOPLE_NUM; i++) {
			people.add(new Person());
		}
	}
	
	public void moveAll() {
		for(int i = 0; i < people.size(); i++) {
			people.get(i).move(this.currentTime);
		}
	}
	
	public void printFile() {
		String data = "latitude,longitude\n";
		for(int i = 0; i < people.size(); i++) {
			Person p = people.get(i);
			data = data + p.lat + "," + p.lon;
			if(i != people.size()-1) data = data + "\n";
		}
		String fileName = "C:/Dev/hackathon_busyness/5CHacks2017/busyness/data/";
		try(PrintWriter out = new PrintWriter(fileName + currentTime + ".csv")) {
		    out.println(data);
		} catch(Exception e) {
			System.out.println(e);
		}
	}
	
	public void nextCycle() {
		moveAll();
		printFile();
		currentTime = Time.addTime(currentTime, TIME_INCREMENT);
	}
	
	public static void main(String args[]) {
		BigBrother bb = new BigBrother();
		while(!bb.currentTime.equals(END_TIME)) {
			bb.nextCycle();
		}
		bb.nextCycle();
	}
}
