// sblood
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class datetime_convert {
    public static void main(String[] args) {
        // String representing date
        String dateStr = "03-17-2025 10:45:30";
        // Create a formatter of form yyyy/mm/dd
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yy-MM-dddd HH:mm:ss");
        LocalDateTime dateObj = LocalDateTime.parse(dateStr, formatter);
        String formattedDate = dateObj.format(DateTimeFormatter.ofPattern("MM/dd/yyyy ss:HH:ss"));

        System.out.println(formattedDate);
    }
}
