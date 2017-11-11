
public class Time {			
	
	public static final int BREAKFAST_HOUR = 8;
	public static final int LUNCH_HOUR = 12;
	public static final int DINNER_HOUR = 17;
	
	public static int getHour(String time) {
		String[] arr = time.split("_");
		return Integer.parseInt(arr[3]);
	}
	
	// TIMES HAVE TO BE IN MM:DD:YY:HH:MM FORMAT
	public static String addTime(String t1, String t2) {
		try {
			String[] arr1 = t1.split("_");
			String[] arr2 = t2.split("_");
			
			int[] times1 = {Integer.parseInt(arr1[0]), Integer.parseInt(arr1[1]),
					Integer.parseInt(arr1[2]), Integer.parseInt(arr1[3]), Integer.parseInt(arr1[4])}; 
			int[] times2 = {Integer.parseInt(arr2[0]), Integer.parseInt(arr2[1]),
					Integer.parseInt(arr2[2]), Integer.parseInt(arr2[3]), Integer.parseInt(arr2[4])};
			
			int mm = times1[0] + times2[0];
			int dd = times1[1] + times2[1];
			int yy = times1[2] + times2[2];
			int h = times1[3] + times2[3];
			int m = times1[4] + times2[4];
			
			
			if(m >= 60) {
				m = m-60;
				h++;
			}
			
			if(h >= 24) {
				h = h-24;
				dd++;
			}
			
			if(dd > 30) {
				dd = dd - 31;
				mm++;
			}
			
			if(mm > 12) {
				mm = mm - 12;
				yy++;
			}

			String month = "" + mm;
			String day = "" + dd;
			String year = "" + yy;
			String hour = "" + h;
			String minute = "" + m;
			if(mm < 10) {
				month = 0 + month; 
			}
			if(dd < 10) {
				day = 0 + day; 
			}
			if(h < 10) {
				hour = 0 + hour; 
			}
			if(m < 10) {
				minute = 0 + minute; 
			}
			return month + "_" + day + "_" + year + "_" + hour + "_" + minute; 
			
		} catch(Exception e) {
			System.out.println("TIMES AREN'T RIGHT" + e);
		}
		return "";
	}
	
	public static void main(String args[]) {
		System.out.println(Time.addTime("11_05_2018_11_15", "00_01_0000_13_41"));
		System.out.println(getHour("00_01_0000_13_41"));
	}
	
}
