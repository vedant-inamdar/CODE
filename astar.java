import java.util.*;

public class astar {

    public static final int[][] possible_moves = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

    public static List<List<Integer>> solve(List<Integer> startstate, List<Integer> goalstate) {

        List<List<Integer>> solution = new ArrayList<>();
        List<List<Integer>> openlist = new ArrayList<>();
        List<List<Integer>> closelist = new ArrayList<>();

        openlist.add(startstate);
        while (!openlist.isEmpty()) {

            List<Integer> currState = openlist.get(0);
            openlist.remove(0);
            if (Arrays.equals(currState.toArray(), goalstate.toArray())) {
                solution.add(currState);
                break;
            }
            closelist.add(currState);

            for (int[] move : possible_moves) {
                int emptyindex = currState.indexOf(0);
                int newRow = emptyindex / 3 + move[0];
                int newCol = emptyindex / 3 + move[1];
                int newIndex = newRow * 3 + newCol;

                if (newRow >= 0 && newRow < 3 && newCol >= 0 && newCol < 3) {
                    List<Integer> newState = new ArrayList<>(currState);

                    newState.set(emptyindex, currState.get(newIndex));
                    newState.set(newIndex, 0);
                    if (!closelist.contains(newState)) {
                        openlist.add(newState);
                    }
                }
            }
        }
        return solution;
    }

    public static void main(String args[]) {

        List<Integer> startstate = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 0);
        List<Integer> goalstate = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 0, 8);
        List<List<Integer>> goal = solve(startstate, goalstate);

        for (List<Integer> state : goal) {
            System.out.println(state);
        }
    }
}