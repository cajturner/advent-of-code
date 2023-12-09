import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.*;
import java.io.File;

public class Day09 {

    private void part1(List<List<List<Integer>>> reportSteps){
        var predictions = new ArrayList<Integer>();
        for (List<List<Integer>> reportStep: reportSteps){
            var currentPrediction = 0;
            for(List<Integer> step: reportStep.reversed()) {
                currentPrediction = currentPrediction + step.reversed().get(0);
            }
            predictions.add(currentPrediction);
        }
        System.out.println(predictions);
        System.out.println(predictions.stream().reduce(Integer::sum).get());
    }

    private static void part2(List<List<List<Integer>>> reportSteps){
        var predictions = new ArrayList<Integer>();
        for (List<List<Integer>> reportStep: reportSteps){
            var currentPrediction = 0;
            for(List<Integer> step: reportStep.reversed()) {
                currentPrediction = step.get(0) - currentPrediction;
            }
            predictions.add(currentPrediction);
        }
        System.out.println(predictions);
        System.out.println(predictions.stream().reduce(Integer::sum).get());
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<String> lines = new ArrayList<>();

        File myObj = new File("/Users/cturner/personal/advent-of-code-23/09/res/input.txt");
        Scanner sc = new Scanner(myObj);
        while (sc.hasNextLine()) {
            String data = sc.nextLine();
            lines.add(data);
        }
        List<List<Integer>> reports = lines.stream().map(line -> (Arrays.stream(line.trim().split(" ")).map(Integer::parseInt).toList())).toList();
        System.out.println(reports);
        List<List<List<Integer>>> reportSteps = new ArrayList<>();
        for (List<Integer> report: reports){
            var reportStep = new ArrayList<List<Integer>>();
            var currentReadings = report;
            while (true){
                if (currentReadings.stream().allMatch(reading -> reading == 0)){
                    break;
                }
                reportStep.add(currentReadings);
                var newReadings = new ArrayList<Integer>();
                for (int i=0; i<currentReadings.size()-1; i++) {
                    newReadings.add(currentReadings.get(i + 1) - currentReadings.get(i));
                }
                currentReadings = newReadings;
            }
            reportSteps.add(reportStep);
        }
        part2(reportSteps);
    }

}