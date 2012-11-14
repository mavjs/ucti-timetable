import java.util.Date;
import java.util.Calendar;
import java.text.SimpleDateFormat;

public class UCTITimeTable {
    public static void main (String[] args) {
        TimeTable tt = new TimeTable("UC2F1201IT{ISS}");
        System.out.println(tt.GetUrl());
    }
}

class TimeTable {
    private String url1 = "http://webspace.apiit.edu.my/schedule/intakeview_intake.jsp?Intake1=";
    private String url2 = "&Submit=Submit&Week=";
    private Date monday;
    private String intake;
    private String FullUrl;

    public TimeTable(String Intake) {
        this.intake = Intake;
    }

    public Date DateMonday() {
        SimpleDateFormat fmt = new SimpleDateFormat("dd-MM-yyy");
        Calendar c = Calendar.getInstance();
        c.set(Calendar.DAY_OF_WEEK, Calendar.MONDAY);
        try {
            this.monday = fmt.parse(c.getTime().toString());
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return this.monday;
    }

    public String GetUrl() {
        this.FullUrl = this.url1 + this.intake + this.url2 + this.DateMonday().toString();
        return this.FullUrl;
    }
}
