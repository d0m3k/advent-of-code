package leet.code;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Djikstra algorithm based solution for https://leetcode.com/problems/word-ladder/
 */
public class DjikstraWords {

    public List<List<String>> groupAnagrams(String[] strs) {
//         you can consider something to be anagram if, when sorted, this is the same string
//     now group by this
        Map<String, List<String>> collect = Arrays.stream(strs)
                .collect(Collectors.groupingBy(DjikstraWords::getSortedString));
        return new ArrayList<>(collect.values());
    }
    public static String getSortedString(String toSort) {
        char[] toSortArray = toSort.toCharArray();
        Arrays.sort(toSortArray);
        return new String(toSortArray);
    }

        public int[] topKFrequent(int[] nums, int k) {
//          first, build frequency map:
            Map<Integer, Integer> numberToFrequency = new HashMap<>();

            for (int i : nums) {
                numberToFrequency.putIfAbsent(i, 1);
                numberToFrequency.put(i, numberToFrequency.get(i) + 1);
            }

//         then build priority queue based on what was frequency
            Queue<Map.Entry<Integer, Integer>> priorityQueue = new PriorityQueue<>(11, Comparator.comparingInt(x -> ((Map.Entry<Integer, Integer>) x).getValue()).reversed());

            for (Map.Entry<Integer, Integer> entry : numberToFrequency.entrySet()) {
                priorityQueue.add(entry);
            }

            List<Integer> result = new ArrayList<>();

            for (int i=0; i<k; i++) {
                result.add(priorityQueue.poll().getKey());
            }

            return result.toArray(new int[]);
        }

        // transformation allows changing a single letter in a fixed position
        // so we need to find words that would differ with current word just by single letter in a single position
        //   make function that would return list/set of such words
        // and then
        //   recursively traverse list (using the same solution) for as long as you get to the result word
        // in meantime, maintain a set of already visited words (why? revisiting the word might make path shorter)

        //  now the problem is that algorithm should find the shortest of these paths
        // here is where Djikstra jumps in:
        // algorithm would maintain info about prevs and distances
        // and choose only paths that are minimal

        public int ladderLength(String beginWord, String endWord, List<String> wordList) {
            Map<String, String> previousWord = new HashMap<>();
            Map<String, Integer> distanceFromRoot = new HashMap<>();

            // we should look for all options, so BFS, things in order -- priority queue
            // alternatively, we could force going the shortest path when looking for next element in queue, duh
            Queue<String> wordsToVisit = new PriorityQueue<>(
                    11,
                    Comparator.comparingInt(x -> distanceFromRoot.getOrDefault(x, 10000))
            );

            // initialize with first word
            wordsToVisit.add(beginWord);
            previousWord.put(beginWord, null);
            distanceFromRoot.put(beginWord, 0);

            // add FIRST all neighbors to queue
            wordsToVisit.addAll(wordList);

            while (!wordsToVisit.isEmpty()) {
//              let us make this a bit less elegant and force getting one with minimum distance
                String current = wordsToVisit.poll();
                // System.out.println("Current word is: " + current);

                //                      new base distance should be my distance + one
                int baseDistance = distanceFromRoot.getOrDefault(current, 10000);
                // System.out.println("Current word is: " + current + ", base distance: " + baseDistance + ", neighbors: " + getSingleLetterNeighbors(wordList, current));


                for (String neighbor : getSingleLetterNeighbors(wordList, current)) {
                    // Djikstra: find the distances and update if lower
                    if (baseDistance < distanceFromRoot.getOrDefault(neighbor, 10000)) {
                        // System.out.println("\tAdding " + neighbor + " with dist " + (baseDistance+1));
                        // recalculate priority
                        wordsToVisit.remove(neighbor);
                        wordsToVisit.add(neighbor);
                        // add Djikstra params
                        distanceFromRoot.put(neighbor, baseDistance + 1);
                        previousWord.put(neighbor, current);
                    }
                }
            }
            System.out.println("Found path: " + path(previousWord, endWord));
            return path(previousWord, endWord).size();
        }


        private List<String> path(Map<String, String> map, String init) {
            // edge case
            if (!map.containsKey(init)) {
                return new ArrayList<>();
            }

            List<String> path = new ArrayList<>();
            String current = init;
            do {
                if (current != null) {
                    path.add(current);
                }
                current = map.get(current);
            } while (current != null);
            return path;
        }

        private Set<String> getSingleLetterNeighbors(List<String> words, String word) {
            return words.stream()
                    .filter(x -> differByOne(word, x))
                    .collect(Collectors.toSet());
        }

        private boolean differByOne(String w1, String w2) {
            int differBy = 0;
            for(int i=0; i<w1.length(); i++) {
                if (!(w1.charAt(i) == w2.charAt(i))) {
                    differBy += 1;
                }
                if (differBy > 1) {
                    return false;
                }
            }
            return differBy == 1;
        }

}
