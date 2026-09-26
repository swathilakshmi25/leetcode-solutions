class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2; // avoids overflow

            if (nums[mid] == target) {
                return mid; // found
            } else if (nums[mid] < target) {
                low = mid + 1; // search right half
            } else {
                high = mid - 1; // search left half
            }
        }

        // if not found, low is the insert position
        return low;
    }
}