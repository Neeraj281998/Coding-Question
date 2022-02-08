#METHOD 1

#Without using memory 
#Using 2 loops 
#Run Time O(N^2)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 =head
        ptr2 =None
 
        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):
            ptr2=ptr1
            while ptr2.next!=None:
                if ptr1.val==ptr2.next.val:
                    ptr2.next=ptr2.next.next
                else:
                    ptr2=ptr2.next
            ptr1=ptr1.next
            
        return head
      
#METHOD 2
#Using dic Memory
#Run Time O(N) and space O(1)
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        memo={}
        memo[head.val]="None"
        current=head
        while current.next is not None:
            if current.next.val in memo:
                current.next=current.next.next
            else:
                memo[current.next.val]="None"
                current=current.next
        return head
