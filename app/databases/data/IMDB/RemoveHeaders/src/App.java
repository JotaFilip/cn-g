import java.io.File;
import java.util.Scanner;

public class App {

    private static final String LOCATION = "./";

    public static void main(String[] args) throws Exception {
        
        File dir = new File(LOCATION);

        for (String file : dir.list()) {

            if (!file.endsWith(".tsv"))
                continue;

            File tsv = new File(LOCATION+file);
            
            try (Scanner reader = new Scanner(tsv)) {
                System.out.println("Ficheiro: "+file);
                System.out.println("\t"+reader.nextLine());
                System.out.println("\t"+reader.nextLine());
                
            } catch (Exception e) { e.printStackTrace(); }
        }
    }
}
