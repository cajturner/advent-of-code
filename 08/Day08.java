import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.*;
import java.io.File;

public class Day08 {

    private void part1(Map<String, Node> nodes, String instructions){
        var current = "AAA";
        var endNode = "ZZZ";
        var steps = 0;
        var directionIndex = 0;
        while (!current.equals(endNode)){
            var node = nodes.get(current);
            var direction = instructions.charAt(directionIndex);
            if (direction == 'L') {
                current = node.left;
            } else {
                current = node.right;
            }
            steps += 1;
            directionIndex = (directionIndex + 1) % instructions.length() ;
        }
        System.out.println(steps);
    }

    private static void part2(Map<String, Node> nodes, String instructions){
        var currentNodes = nodes.entrySet().stream().filter(e-> e.getValue().isGhostStart()).map(Map.Entry::getKey).toList();
        Integer steps = 0;
        var directionIndex = 0;
        var end = false;
        List<BigInteger> stepsToZ = new ArrayList<>(currentNodes.stream().map(e -> BigInteger.valueOf(0l)).toList());
        while (!end){
            var direction = instructions.charAt(directionIndex);
            List<String> nextNodes = new ArrayList<>();
            for (String currentNode: currentNodes) {
                var node = nodes.get(currentNode);
                if (direction == 'L') {
                    nextNodes.add(node.left);
                } else {
                    nextNodes.add(node.right);
                }
            }
            steps += 1;
            directionIndex = (directionIndex + 1) % instructions.length() ;
            for (int i = 0; i < nextNodes.size(); i++) {
                if (nodes.get(nextNodes.get(i)).isEndNode()) {
                    stepsToZ.set(i, BigInteger.valueOf(steps.longValue()));
                }
            }
            if (stepsToZ.stream().allMatch(e -> e.longValue() != 0l)){
                end = true;
            }
            currentNodes = nextNodes;
        }
        var lcm = stepsToZ.stream().reduce( (a, b) -> {
            var gcd = a.gcd(b);
            var absProduct = a.multiply(b).abs();
            return absProduct.divide(gcd);
        });
        System.out.println(lcm);
    }

    public static void main(String[] args) throws FileNotFoundException {
        List<String> lines = new ArrayList<>();

        File myObj = new File("/Users/cturner/workspace/advent-of-code-23/08/res/input.txt");
        Scanner sc = new Scanner(myObj);
        while (sc.hasNextLine()) {
            String data = sc.nextLine();
            lines.add(data);
        }
        String instructions = lines.get(0);
        List<String> node_strings = lines.subList(2, lines.size());
        Map<String, Node> nodes = new HashMap();
        for (String node_str : node_strings) {
            var split = node_str.split(" = ");
            String name = split[0];
            String left = split[1].substring(1,4);
            String right = split[1].substring(6,9);
            nodes.put(name, new Node(name, left, right));
        }
        part2(nodes, instructions);


    }
}