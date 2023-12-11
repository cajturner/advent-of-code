import java.io.FileNotFoundException;
import java.util.*;
import java.io.File;
import java.util.stream.Collectors;

public class Day10 {
    enum DIRECTION {
        NORTH ,
        EAST,
        SOUTH,
        WEST ;
    }
    public enum PIPE {
        NORTH_SOUTH ('|', List.of(DIRECTION.NORTH, DIRECTION.SOUTH)),
        EAST_WEST ('-', List.of(DIRECTION.EAST, DIRECTION.WEST)),
        NORTH_EAST ('L', List.of(DIRECTION.NORTH, DIRECTION.EAST)),
        NORTH_WEST('J', List.of(DIRECTION.NORTH, DIRECTION.WEST)),
        SOUTH_WEST('7', List.of(DIRECTION.SOUTH, DIRECTION.WEST)),
        SOUTH_EAST('F', List.of(DIRECTION.SOUTH, DIRECTION.EAST)),
        GROUND('.', List.of()),
        START('S', List.of());
        private final char c;
        private final List<DIRECTION> validDirections;
        PIPE(char c, List<DIRECTION> validDirections) {
            this.c = c;
            this.validDirections = validDirections;
        }
        public static PIPE fromChar(char c) {
            for (PIPE p : PIPE.values()) {
                if (p.c == c) {
                    return p;
                }
            }
            return null;
        }

        public boolean isValidDirection(DIRECTION sourceDirection) {
            return switch (sourceDirection) {
                case NORTH -> this.validDirections.contains(DIRECTION.SOUTH);
                case SOUTH -> this.validDirections.contains(DIRECTION.NORTH);
                case EAST -> this.validDirections.contains(DIRECTION.WEST);
                case WEST -> this.validDirections.contains(DIRECTION.EAST);
            };
        }

        public List<DIRECTION> getDirections() {
            return validDirections;
        }
    }

    public static class Index {
        public final int x;
        public final int y;
        public Index(int x, int y) {
          this.x = x;
          this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Index index = (Index) o;
            return x == index.x && y == index.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public String toString() {
            return "Index{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }
    public static void main(String[] args) throws FileNotFoundException {
        Map<Index, PIPE> map = new HashMap<>();

        File myObj = new File("/Users/cturner/personal/advent-of-code-23/10/res/input.txt");
        Scanner sc = new Scanner(myObj);
        int row = 0;
        int yMax = 0;
        Index start = null;
        while (sc.hasNextLine()) {
            String data = sc.nextLine();
            for (int col = 0; col < data.length(); col++) {
                PIPE p = PIPE.fromChar(data.charAt(col));
                Index i = new Index(row, col);
                if (p != null) {
                    map.put(i, p);
                }
                if (p == PIPE.START) {
                    start = i;
                }
            }
            row++;
            yMax = data.length();
        }

        Map<Index, Integer> openLocations = new HashMap<>();
        assert start != null;
        if (checkLocation(map, new Index(start.x - 1, start.y), DIRECTION.NORTH)) {
            openLocations.put(new Index(start.x - 1, start.y), 1);
        }
        if (checkLocation(map, new Index(start.x + 1, start.y), DIRECTION.SOUTH)) {
            openLocations.put(new Index(start.x + 1, start.y), 1);
        }
        if (checkLocation(map, new Index(start.x, start.y + 1), DIRECTION.EAST)) {
            openLocations.put(new Index(start.x, start.y + 1), 1);
        }
        if (checkLocation(map, new Index(start.x, start.y - 1), DIRECTION.WEST)) {
            openLocations.put(new Index(start.x, start.y - 1), 1);
        }
        Map<Index, Integer> visitedLocations = new HashMap<>();
        visitedLocations.put(start, 0);
        while (!openLocations.isEmpty()) {
            var entry = openLocations.entrySet().stream().min(Comparator.comparingInt(Map.Entry::getValue)).get();
            var index = entry.getKey();
            var distance = entry.getValue();
            var pipe = map.get(index);
            var nextDirections = pipe.getDirections();
            visitedLocations.put(index, distance);
            for (DIRECTION d : nextDirections) {
                Index nextIndex = switch (d) {
                    case NORTH -> new Index(index.x - 1, index.y);
                    case SOUTH -> new Index(index.x + 1, index.y);
                    case EAST -> new Index(index.x, index.y + 1);
                    case WEST -> new Index(index.x, index.y - 1);
                };
                var x = checkLocation(map, nextIndex, d);
                if (!visitedLocations.containsKey(nextIndex) && checkLocation(map, nextIndex, d)) {
                    openLocations.put(nextIndex, distance + 1);
                }
            }
            openLocations.remove(index);
        }
        System.out.println(visitedLocations.entrySet().stream().max(Comparator.comparingInt(Map.Entry::getValue)).get().getValue());

        Map<Index, DIRECTION> pathLocations = new HashMap<>();
        if (checkLocation(map, new Index(start.x - 1, start.y), DIRECTION.NORTH)) {
            pathLocations.put(new Index(start.x - 1, start.y), DIRECTION.SOUTH);
        }else if (checkLocation(map, new Index(start.x + 1, start.y), DIRECTION.SOUTH)) {
            pathLocations.put(new Index(start.x + 1, start.y), DIRECTION.NORTH);
        }else if (checkLocation(map, new Index(start.x, start.y + 1), DIRECTION.EAST)) {
            pathLocations.put(new Index(start.x, start.y + 1), DIRECTION.WEST);
        } else if (checkLocation(map, new Index(start.x, start.y - 1), DIRECTION.WEST)) {
            pathLocations.put(new Index(start.x, start.y - 1), DIRECTION.EAST);
        }

        Set<Index> externalLocations = new HashSet<>();
        Set<Index>  internalLocations =  new HashSet<>();

        while (!pathLocations.isEmpty()){
            var entry = pathLocations.entrySet().stream().findFirst().get();
            pathLocations.remove(entry.getKey());
            var index = entry.getKey();
            var pipe = map.get(index);
            if (pipe == PIPE.START) {
                break;
            }

            var direction = pipe.getDirections().stream().filter(direction1 -> !direction1.equals(entry.getValue())).findFirst().get();
            switch (direction){
                case NORTH -> {
                    for(int y = index.y+1; y<yMax; y++){
                        var found = false;
                        var newIndex = new Index(index.x, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            internalLocations.add(newIndex);
                            found = true;
                        }
                        newIndex = new Index(index.x-1, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            internalLocations.add(newIndex);
                            found = true;
                        }
                        if (!found){
                            break;
                        }
                    }
                    for(int y = index.y-1; y>=0; y--){
                        var found = false;
                        var newIndex = new Index(index.x, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            externalLocations.add(newIndex);
                            found = true;
                        }
                        newIndex = new Index(index.x-1, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            externalLocations.add(newIndex);
                            found = true;
                        }
                        if (!found){
                            break;
                        }
                    }
                }
                case SOUTH -> {
                    for (int y = index.y+1; y < yMax; y++) {
                        var found = false;
                        var newIndex = new Index(index.x, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            externalLocations.add(newIndex);
                            found = true;
                        }
                        newIndex = new Index(index.x+1, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            externalLocations.add(newIndex);
                            found = true;
                        }
                        if (!found){
                            break;
                        }
                    }
                    for (int y = index.y-1; y >= 0; y--) {
                        var found = false;
                        var newIndex = new Index(index.x, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            internalLocations.add(newIndex);
                            found = true;
                        }
                        newIndex = new Index(index.x+1, y);
                        if (!visitedLocations.containsKey(newIndex)){
                            internalLocations.add(newIndex);
                            found = true;
                        }
                        if (!found){
                            break;
                        }
                    }
                }
            }
            switch (direction){
                case NORTH ->
                        pathLocations.put(new Index(index.x-1, index.y), DIRECTION.SOUTH);
                case SOUTH ->
                        pathLocations.put(new Index(index.x + 1, index.y), DIRECTION.NORTH);
                case EAST ->
                        pathLocations.put(new Index(index.x, index.y + 1), DIRECTION.WEST);

                case WEST ->
                        pathLocations.put(new Index(index.x, index.y - 1), DIRECTION.EAST);
            }
        }
        System.out.println("INTERNAL");
        System.out.println(internalLocations);
        System.out.println(internalLocations.size());
        System.out.println("EXTERNAL");
        System.out.println(externalLocations);
        System.out.println(externalLocations.size());

        for(int x = 0; x < row; x++) {
            for(int y = 0; y < yMax; y++) {
                Index index = new Index(x,y);
                if (internalLocations.contains(index)) {
                    System.out.print("*");
                }else if (externalLocations.contains(index)){
                    System.out.print("O");
                }else {
                    System.out.print(map.get(index).c);
                }
            }
            System.out.println();
        }
        System.out.println();
    }




    private static boolean checkLocation(Map<Index, PIPE> map, Index index, DIRECTION direction) {
        var pipe = map.get(index);
        return pipe!= null && pipe.isValidDirection(direction);
    }
}