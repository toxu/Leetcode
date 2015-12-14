/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;
        int carry = 0;
        while(l1 != null || l2 != null || carry != 0){
        	int sum = carry;

        	if(l1){
        		sum += l1.val;
        		l1 = l1.next;
        	}

        	if(l2){
        		sum += l2.val;
        		l2 = l2.next;
        	}

        	int num = sum%10;
        	carry = sum/10;

        	current.next = new ListNode(num);
        	current = current.next;
        }
        return dummy.next;
    }
}