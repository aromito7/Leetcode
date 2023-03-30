/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    // let current = head
    // // console.log(Object.keys(head), Array.isArray(head))
    
    // // const nodes = new Set() 

    // const nodes = new Set()

    // while(current){
    //     if(nodes.has(current)) return true

    //     nodes.add(current)
    //     current = current.next
    // }

    // return false
    let fast = head;
    while (fast && fast.next) {
        head = head.next;
        fast = fast.next.next;
        if (head === fast) return true;
    }
    return false;
};
