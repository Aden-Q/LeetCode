# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode(val=0, next=head)
        # convert it to a hashmap for fast lookup
        nums = set(nums)
        curr = dummyHead.next
        prev = dummyHead

        while curr:
            if curr.val in nums:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummyHead.next
