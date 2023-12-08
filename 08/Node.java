public class Node {
    public String name;
    public String left;
    public String right;

    public Node(String name, String left, String right) {
        this.name = name;
        this.left = left;
        this.right = right;
    }

    public boolean isEndNode() {
        return this.name.endsWith("Z");
    }

    public boolean isGhostStart(){
        return this.name.endsWith("A");
    }

    @Override
    public String toString() {
        return "Node{" +
                "name='" + name + '\'' +
                ", left='" + left + '\'' +
                ", right='" + right + '\'' +
                '}';
    }
}