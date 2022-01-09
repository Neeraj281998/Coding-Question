class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 
        data=""
        while head:
            data+=str(head.val)
            head=head.next
        return int(data,2)