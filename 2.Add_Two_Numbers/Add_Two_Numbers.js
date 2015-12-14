/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var dummy = new ListNode(-1);
    var current = dummy;
    var carry = 0;
    while(l1 !== null || l2 !== null || carry !== 0){ //IMPORTANT!!! Different from another languages.
    	var sum = carry;

    	if(l1 !== null){
    		sum += l1.val;
    		l1 = l1.next;
    	}

    	if(l2 !== null){
    		sum += l2.val;
    		l2 = l2.next;
    	}

    	var num = sum%10;
    	carry = parseInt(sum/10); //IMPORTANT!!! Different from another languages.

    	current.next = new ListNode(num);
    	current = current.next;
    }
    current.next = null;
    return dummy.next;
};