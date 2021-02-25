Name: Olivia McNulty
Computing ID: ocm5uu
  
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] count = new int[1001];
        for (int num : arr1) {
            count[num] += 1;
        }

        int index = 0, ans[] = new int[arr1.length];
        for (int num : arr2) {
            while (count[num]-- > 0) {
                ans[index++] = num;
            }
        }
        for (int i = 0; i < count.length; i++) {
            while (count[i]-- > 0) {
                ans[index++] = i;
            }
        }
        return ans;
    }
}
