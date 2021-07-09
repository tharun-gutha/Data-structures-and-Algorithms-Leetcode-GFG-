class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
          if (nums.length == 0) {
            return new ArrayList<>();
        }
        List<Integer> resultList = new ArrayList<>();
        boolean[] result = new boolean[nums.length + 1];
        for (int num : nums) {
            result[num] = true;
        }
        for (int i = 1; i < nums.length; i++) {
            if (!result[i]) {
                resultList.add(i);
            }
        }
        return resultList;
    }
}